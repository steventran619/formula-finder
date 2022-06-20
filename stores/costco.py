from selenium.webdriver.remote.webdriver import WebDriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webelement import WebElement
from selenium.webdriver.support.ui import Select

class Costco():
    """
    Class to browse through Costco's products.
    """
    def __init__(self, driver:WebDriver):
        self.driver = driver
        self.product_boxes = None
        self.products = None     # WebElements
        print("\nNow checking Costco")


    def SortBy(self):
        """Sort products by price (low to high) for non-members."""
        sorter = self.driver.find_element(By.ID, "sort_by")
        sorter.click()
        yes = Select(sorter)
        yes.select_by_visible_text('Price (Low to High)')
    
    def find_products(self):
        """
        Finds all the products from the first page of Costco search.
        """
        self.product_boxes = self.driver.find_elements(By.CSS_SELECTOR,
            'div[class="col-xs-6 col-lg-4 col-xl-3 product"]')
        # print(len(self.product_boxes))
        # def get_products(self):
        #     return self.product_boxes
        #     # print(len(self.product_boxes))

    def pull_product_attributes(self):
        """
        Obtains product names, availiability, pricing, and the URL and stores
        them as products.
        """
        print(f"> Analyzing {len(self.product_boxes)} Products")
        products = []
        for box in self.product_boxes:
            product_name = box.find_element(By.CSS_SELECTOR, 'span[class="description"]').text
            product_url = box.find_element(By.TAG_NAME, 'a').get_attribute('href')
            product_available = box.find_element(By.CSS_SELECTOR, 'a[class="product-image-url"]')
            try:
                if product_available.find_element(By.CSS_SELECTOR, 'img[class="product-out-stock-overlay"]'):
                    product_available = 'Out of Stock'
            except Exception as error:
                if 'no such element' in str(error):
                    product_available = 'In Stock'
            if product_available == 'In Stock':
                price = box.find_element(By.CSS_SELECTOR, 'div[class="price"]').text
                if price.strip() == '':
                    price = 'Members Pricing'
            else:
                price = 'N/A'
            products.append([product_name, product_available, price, __class__.__name__, product_url])
            # print('.', end ="")
        self.products = products
        
        print('> Completed Costco Search')
    
    def get_product_summary(self):
        """
        :return list: returns the Costco product summary
        """
        return self.products

# class CostcoReport():
#     def __init__(self, boxes_section_element: WebElement):
#         self.boxes_section_element = boxes_section_element
#         self.product_boxes = []

#     def pull_product_attributes(self):
#         print(self.boxes_section_element)
#         for box in self.boxes_section_element:
#             product_name = box.find_element(By.CSS_SELECTOR, 'span[class="description"]').get_attribute('innterHTML')
#             print(product_name)