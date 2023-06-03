# Scraping Deck Information from AetherHub

## scrape_deck_info

This Python function scrapes deck information from the AetherHub website and saves it to a CSV file. The function takes three arguments: `deck_info`, a list of dictionaries that will be populated with the scraped deck information; `url`, the URL of the website to scrape; and `end_range`, the number of pages of deck information to scrape.

## scrape_deck_lists

This Python function scrapes deck lists from a website using Selenium and the Chrome web driver. It takes two arguments: `deck_info_df`, which is a Pandas DataFrame, and `start_range`, which is an integer. The function loops through the URLs in the `link` column of the `deck_info_df` DataFrame, visits each URL, clicks on the "Export" button, and then clicks on the "Text List" button if the "Import" button is not found. It then clicks on the "Export to text" button, copies the text to the clipboard, and saves it to a file in the `deck_lists` directory with a name based on the URL. Finally, the function returns `None`.

## Installation

To use this function, you will need to have Python 3 installed on your computer. You will also need to install the following packages:

- `selenium`
- `beautifulsoup4`
- `pandas`
- `splinter`
- `webdriver_manager`

You can install these packages using pip:

```python
pip install selenium beautifulsoup4 pandas splinter webdriver_manager
```

## Usage

To use this `scrape_deck_info`, you will need to import it into your Python script:

```python
from scrape_deck_info import scrape_deck_info
```

You can then call the function, passing in the three required arguments:

```python
deck_info = []
url = 'https://aetherhub.com/User/LegenVD/Decks'
end_range = 5
scrape_deck_info(deck_info, url, end_range)
```

This will scrape the first 5 pages of deck information from the AetherHub website and save it to a CSV file called `deck_info.csv`. The function will also return the first 5 elements of the `deck_info` list.

To use the `scrape_deck_lists` function, you will need to import it into your Python script:

```python
from scrape_deck_info import scrape_deck_lists
```

You can then call the function, passing in the two required arguments:

```python
# Load the deck info DataFrame
deck_info_df = pd.read_csv('deck_info.csv')
start_range = 0
scrape_deck_lists(deck_info_df, start_range)
```

## License

This function is licensed under the MIT License.
