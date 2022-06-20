from selenium.webdriver.remote.webdriver import WebDriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webelement import WebElement
from selenium.webdriver.support.ui import Select
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import StaleElementReferenceException, NoSuchElementException
from selenium.webdriver.common.keys import Keys
import time
class Target():
    """
    Class to browse through Target's products.
    """
    def __init__(self, driver:WebDriver):
        self.driver = driver
        self.product_boxes = None
        self.products = []     # WebElements
        print("\nNow checking Target")

    def SortBy(self):
        """Sort products by price (low to high) for non-members."""
        sorter = self.driver.find_element(By.ID, "sort_by")
        sorter.click()
        yes = Select(sorter)
        yes.select_by_visible_text('Price (Low to High)')
    
    def find_products(self):
        """
        Finds all the products from the first page of Target search.
        """
        self.product_boxes = self.driver.find_elements(By.CSS_SELECTOR,
            'div[class="styles__StyledCol-sc-ct8kx6-0 ebNJlV"]')



    def wait_for_element_by_class(self, e_class, time=6):
        """
        Uses webdriver(d) to wait for page title(title) to become visible
        """
        return WebDriverWait(self.driver, time).until(
            EC.presence_of_element_located((By.CSS_SELECTOR, e_class))
        )
        
    def wait_for_all_elements(self, e_class, time=6):
        """
        Uses webdriver(d) to wait for page title(title) to become visible
        """
        return WebDriverWait(self.driver, time).until(
            EC.presence_of_all_elements_located((By.CSS_SELECTOR, e_class))
        )

    def pull_product_attributes(self):
        """
        Obtains product names, availiability, pricing, and the URL and stores
        them as products.
        """
        htmlelement= self.driver.find_element(By.TAG_NAME, 'html')
        for i in range(4):
            time.sleep(1)
            htmlelement.send_keys(Keys.END)
            htmlelement.send_keys(Keys.HOME)
        # try:
        product_boxes = self.driver.find_elements(By.CSS_SELECTOR, 'div[class="styles__StyledCol-sc-ct8kx6-0 ebNJlV"]')        
        print(f"> Analyzing {len(self.product_boxes)} Products")
        for each_box in product_boxes:
            product_name = each_box.find_element(By.CLASS_NAME, 'h-display-flex').text      # WORKING DONT DELETE
            product_available = each_box.find_element(By.CSS_SELECTOR, 'div[class="styles__AddToCartButtonWrapper-sc-1iglypx-2 bkwcjs"]')
            if product_available.find_element(By.TAG_NAME, 'button').text == 'Add to cart':
                stock = "In Stock"
            else:
                stock = "Out of Stock"
            product_url = each_box.find_element(By.TAG_NAME, 'a').get_attribute('href')
            price = each_box.find_element(By.CSS_SELECTOR, 'div[data-test="current-price"]').text.split()
            price = price[0]
            store = __class__.__name__
            self.products.append([
                product_name,
                stock,
                price,
                store,
                product_url
                ])
            # print('.', end ="")
        print('> Completed Target Search')

    def get_product_summary(self):
        return self.products

    def print_product_summary(self):
        for count, item in enumerate(self.products):
            print(count, item)