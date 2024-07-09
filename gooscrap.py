import csv
import time
import os
from selenium import webdriver
from selenium.common.exceptions import NoSuchElementException, StaleElementReferenceException
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By

class GoogleMapScraper:
    def __init__(self):
        self.output_file_name = "google_map_business_data.csv"
        self.headless = False
        self.driver = None
        self.unique_check = []

    def config_driver(self):
        options = webdriver.ChromeOptions()
        if self.headless:
            options.add_argument("--headless")
        webdriver_path = "C:\\Users\\Admin\\.wdm\\drivers\\chromedriver\\win64\\126.0.6478.126\\chromedriver-win32\\chromedriver.exe"
        service = Service(webdriver_path)
        self.driver = webdriver.Chrome(service=service, options=options)

    def save_data(self, data):
        header = ['company_name', 'rating', 'reviews_count', 'address', 'category', 'phone', 'website']
        file_exists = os.path.isfile(self.output_file_name)
        with open(self.output_file_name, 'a', newline='', encoding="utf-8") as csvfile:
            writer = csv.writer(csvfile)
            if not file_exists:
                writer.writerow(header)
            writer.writerow(data)

    def parse_contact(self, business):
        try:
            contact = business.find_elements(By.CLASS_NAME, "W4Efsd")[3].text.split("·")[-1].strip()
        except:
            contact = ""
        return contact

    def parse_rating_and_review_count(self, business):
        try:
            reviews_block = business.find_element(By.CLASS_NAME, 'AJB7ye').text.split("(")
            rating = reviews_block[0].strip()
            reviews_count = reviews_block[1].split(")")[0].strip()
        except:
            rating = ""
            reviews_count = ""
        return rating, reviews_count

    def parse_address_and_category(self, business):
        try:
            address_block = business.find_elements(By.CLASS_NAME, "W4Efsd")[2].text.split("·")
            if len(address_block) >= 2:
                address = address_block[1].strip()
                category = address_block[0].strip()
            elif len(address_block) == 1:
                address = ""
                category = address_block[0]
        except:
            address = ""
            category = ""
        return address, category

    def get_business_info(self):
        time.sleep(2)
        for business in self.driver.find_elements(By.CLASS_NAME, 'THOPZb'):
            name = business.find_element(By.CLASS_NAME, 'fontHeadlineSmall').text
            rating, reviews_count = self.parse_rating_and_review_count(business)
            address, category = self.parse_address_and_category(business)
            contact = self.parse_contact(business)
            try:
                website = business.find_element(By.CLASS_NAME, "lcr4fd").get_attribute("href")
            except NoSuchElementException:
                website = ""
            unique_id = "".join([name, rating, reviews_count, address, category, contact, website])
            if unique_id not in self.unique_check:
                data = [name, rating, reviews_count, address, category, contact, website]
                self.save_data(data)
                self.unique_check.append(unique_id)

    def load_companies(self, url):
        print("Getting business info", url)
        self.driver.get(url)
        time.sleep(5)
        panel_xpath = '//*[@id="QA0Szd"]/div/div/div[1]/div[2]/div/div[1]/div/div/div[2]/div[1]'
        while True:
            try:
                scrollable_div = self.driver.find_element(By.XPATH, panel_xpath)
                # scrolling
                flag = True
                i = 0
                while flag:
                    print(f"Scrolling to page {i + 2}")
                    self.driver.execute_script('arguments[0].scrollTop = arguments[0].scrollHeight', scrollable_div)
                    time.sleep(2)
                    if "You've reached the end of the list." in self.driver.page_source:
                        flag = False
                    self.get_business_info()
                    i += 1
                break
            except StaleElementReferenceException:
                print("StaleElementReferenceException encountered. Retrying...")

urls = [
    "https://www.google.com/maps/search/+course+bangalore+/@12.9462051,77.4633342,11z?entry=ttu"
]

business_scraper = GoogleMapScraper()
business_scraper.config_driver()
for url in urls:
    business_scraper.load_companies(url)
