from selenium.webdriver.remote.webdriver import WebDriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webelement import WebElement
from selenium.webdriver.support.ui import Select
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import StaleElementReferenceException, NoSuchElementException
from selenium.webdriver.common.keys import Keys
import time

class Amazon():
    """
    Class to browse through Amazon's Mamabear products.
    """
    def __init__(self, driver:WebDriver):
        self.driver = driver
        self.product_boxes = None
        self.products = []     # WebElements
        print("\nNow checking Amazon")


    def find_products(self):
        """
        Finds all the products from the first page of Amazon search.
        """
        search_box = self.driver.find_element(By.CLASS_NAME,
            's-main-slot')
        self.product_boxes = search_box.find_elements(By.CSS_SELECTOR, 'div[class="sg-col-4-of-12 s-result-item s-asin sg-col-4-of-16 sg-col s-widget-spacing-small sg-col-4-of-20"]')

    def filter_mamabear(self):
        """Filters for mama bear brand infant formula."""
        result = []
        for item in self.product_boxes:
            if "Mama Bear" in (item.find_element(By.CSS_SELECTOR, 'span[class="a-size-base-plus a-color-base a-text-normal"]').get_attribute('innerHTML')):
                result.append(item)
        return result

    def pull_product_attributes(self):
        """
        Obtains product names, availiability, pricing, and the URL and stores
        them as products.
        """
        mamaBear_products = self.filter_mamabear()       
        print(f"> Analyzing {len(mamaBear_products)} Products")
        for each_box in mamaBear_products:
            product_name = each_box.find_element(By.CSS_SELECTOR, 'span[class="a-size-base-plus a-color-base a-text-normal"]').get_attribute('innerHTML')      # WORKING DONT DELETE
            product_available = each_box.find_element(By.CSS_SELECTOR, 'span[class="a-size-small"]').get_attribute('innerHTML')
            if product_available == 'Out of Stock':                
                stock = "Out of Stock"
            else:
                stock = "In Stock"
            product_url = each_box.find_element(By.TAG_NAME, 'a').get_attribute('href')
            price = each_box.find_element(By.CSS_SELECTOR, 'span[class="a-offscreen"]').get_attribute('innerHTML')
            # price = price[0]
            store = __class__.__name__
            self.products.append([
                product_name,
                stock,
                price,
                store,
                product_url
                ])
        print('> Completed Amazon Search')
    
    def get_product_summary(self):
        return self.products

    def print_product_summary(self):
        for count, item in enumerate(self.products):
            print(count, item)
