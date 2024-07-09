# Google Map Scraper

This project is a Python script for scraping business data from Google Maps. It uses Selenium WebDriver to automate the browser and extract information such as company name, rating, reviews count, address, category, phone, and website.

## Features

- Scrapes business data from Google Maps search results.
- Extracts company name, rating, reviews count, address, category, phone, and website.
- Saves the data to a CSV file.
- Handles dynamic content loading and stale element references.

## Prerequisites

- Python 3.12 or higher
- Google Chrome browser
- Selenium package
- ChromeDriver

## Setup

1. **Clone the repository:**
    ```bash
    git clone https://github.com/aswinsankarcp/GOOGLE-SCRAPE.git
    cd GOOGLE-SCRAPE
    ```

2. **Install required packages:**
    ```bash
    pip install selenium webdriver-manager
    ```

3. **Download ChromeDriver:**
    The script uses the `webdriver-manager` package to automatically manage the ChromeDriver version. If you need to manually specify the location, ensure you have downloaded ChromeDriver and updated the path in the script.

4. **Update the WebDriver location:**
    Edit the `config_driver` method in the script to specify the correct path to the ChromeDriver executable:
    ```python
    webdriver_path = "C:\\Users\\Admin\\.wdm\\drivers\\chromedriver\\win64\\126.0.6478.126\\chromedriver-win32\\chromedriver.exe"
    ```

## Usage

1. **Edit the Google Maps URL:**
    Update the `urls` list in the script with the desired Google Maps search URL:
    ```python
    urls = [
        "https://www.google.com/maps/search/+course+bangalore+/@12.9462051,77.4633342,11z?entry=ttu"
    ]
    ```

2. **Run the script:**
    ```bash
    python gooscrap.py
    ```

## Script Overview

The script consists of the following key components:

- **GoogleMapScraper class:**
    - `__init__`: Initializes the class attributes.
    - `config_driver`: Configures the Chrome WebDriver.
    - `save_data`: Saves the scraped data to a CSV file.
    - `parse_contact`: Extracts the contact information of the business.
    - `parse_rating_and_review_count`: Extracts the rating and reviews count of the business.
    - `parse_address_and_category`: Extracts the address and category of the business.
    - `get_business_info`: Retrieves the business information from the search results.
    - `load_companies`: Loads the companies from the Google Maps URL and handles dynamic content loading.

## Handling StaleElementReferenceException

The script includes handling for `StaleElementReferenceException` to ensure the scraping process is robust against dynamic changes on the Google Maps page.

## Contributing

Feel free to submit issues or pull requests if you have any improvements or bug fixes.

## License

This project is licensed under the MIT License.
