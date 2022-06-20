from selenium.webdriver.remote.webdriver import WebDriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webelement import WebElement
from selenium.webdriver.support.ui import Select
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import StaleElementReferenceException, NoSuchElementException
from selenium.webdriver.common.keys import Keys
import time

class Kroger():
    """
    Class to browse through Kroger's Comforts Brand products.
    """
    def __init__(self, driver:WebDriver):
        self.driver = driver
        self.product_boxes = None
        self.products = []     # WebElements
        print("\nNow checking Kroger")

    def fight_popup(self):
        # popup = self.driver.find_element(By.ID, "kds-Modal-l4kcnr1d")
        self.driver.implicitly_wait(9)
        popup = self.driver.find_element(By.CLASS_NAME, 'kds-Modal-actionButton--secondary')
        time.sleep(5)
        popup.click()
    
    def find_products(self):
        """
        Finds all the products from the first page of Kroger search.
        """
        # search_box = self.driver.find_element(By.CLASS_NAME,
            # 's-main-slot')
        self.driver.refresh()
        self.product_boxes = self.driver.find_elements(By.CLASS_NAME, "AutoGrid-cell.min-w-0")
        print(len(self.products))

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
        
        print(f"Analyzing {len(self.product_boxes)} Products")
        for each_box in self.product_boxes:
            product_name = each_box.find_element(By.CSS_SELECTOR, 'div[class="flex-grow w-full h-64"]').get_attribute('innerHTML')      # WORKING DONT DELETE
            # product_available = each_box.find_element(By.CSS_SELECTOR, 'span[class="a-size-small"]').get_attribute('innerHTML')
            # if product_available == 'Out of Stock':                
            #     stock = "Out of Stock"
            # else:
            #     stock = "In Stock"
            # product_url = each_box.find_element(By.TAG_NAME, 'a').get_attribute('href')
            # price = each_box.find_element(By.CSS_SELECTOR, 'span[class="a-offscreen"]').get_attribute('innerHTML')
            # # price = price[0]
            # store = __class__.__name__
            
            print(product_name)
            # self.products.append([
            #     product_name,
            #     stock,
            #     price,
            #     store,
            #     product_url
            #     ])
        print('Completed Kroger Search')

    
    def get_product_summary(self):
        return self.products

    def print_product_summary(self):
        for count, item in enumerate(self.products):
            print(count, item)
