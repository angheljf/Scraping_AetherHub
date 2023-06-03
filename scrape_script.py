# Imports
""" This script scrapes deck lists from AetherHub.com and saves them as .txt files."""
import time
from tkinter import Tk
from collections import Counter
from splinter import Browser
from bs4 import BeautifulSoup as soup
from webdriver_manager.chrome import ChromeDriverManager
import pandas as pd


def scrape_deck_info(deck_info, url, end_range):
    """Scrape deck info from AetherHub.com and return a list of dictionaries with the deck name, link, and format."""
    executable_path = {'executable_path': ChromeDriverManager().install()}
    browser = Browser('chrome', **executable_path, headless=False)
    browser.visit(url)
    partial_url = 'https://aetherhub.com'
    for i in range(0, end_range):
        html = browser.html
        decks_soup = soup(html, 'html.parser')
        table = decks_soup.find('table', id='metaHubTable')
        time.sleep(5)
        table_body = table.find('tbody')
        time.sleep(5)
        table_rows = table_body.find_all('tr')
        time.sleep(5)
        for i in table_rows:
            table_titles = i.find_all('a')
            table_href = i.find_all('a', href=True)
            # Find text with class 'text-muted'
            table_format = i.find_all('span', class_='text-muted')
            deck_info.append(
                {'name': table_titles[0].text, 'link': partial_url + table_href[0]['href'], 'format': table_format[0].text})
            # Check if there are duplicates in the link key inside the list of dictionaries
            # If there are, stop the loop
            if len(Counter([i['link'] for i in deck_info])) < len(deck_info):
                break
        time.sleep(5)
        # Click the '>' button, except for the last page, then stop the loop
        try:
            browser.links.find_by_partial_text('>').click()
        except:
            break
        decks_soup = soup(html, 'html.parser')
    deck_info_df = pd.DataFrame(deck_info)
    # Remove quotes from the name column
    deck_info_df['name'] = deck_info_df['name'].str.replace('"', '')
    deck_info_df.to_csv('deck_info.csv', index=False)
    return deck_info[0:5]


def scrape_deck_lists(deck_info_df, start_range: int):
    """Scrape deck lists from AetherHub.com and save them as .txt files."""
    executable_path = {'executable_path': ChromeDriverManager().install()}
    browser = Browser('chrome', **executable_path, headless=False)
    for i in deck_info_df['link'][start_range:]:
        time.sleep(3)
        browser.visit(i)
        browser.links.find_by_partial_text('Export').click()
        time.sleep(3)
        try:
            browser.find_by_css('a[href="#importModal"]').click()
        except:
            browser.links.find_by_partial_text('Text List').click()
        time.sleep(3)
        # Click button with id "exportListbtn"
        browser.find_by_id('exportListbtn').click()
        time.sleep(1)
        text = Tk().clipboard_get()
        text = text.split('\n')
        # Make the name of the file based on the 'name' column
        file_name = i.split('/')[-1]
        file_name = file_name.replace('-', '_')
        file_name = file_name.replace(' ', '_')
        with open(f'deck_lists/{file_name}.txt', 'w') as f:
            for i in text:
                f.write(i + '\n')
