from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from prettytable import PrettyTable

from stores.costco import Costco
from stores.target import Target
from stores.amazon import Amazon
from stores.kroger import Kroger
import stores.constants as const
import os

STORESPATH = os.path.dirname(__file__)
RELATIVEPATH = "input_files"
DRIVERSPATH = os.path.join(STORESPATH, "..", RELATIVEPATH)

class Stores(webdriver.Chrome):
    def __init__(self, driverPath = DRIVERSPATH, teardown = False):
        self.driver_path = driverPath
        self.teardown = teardown
        os.environ['PATH'] += os.pathsep + self.driver_path
        # Removes annoying Chrome Developer prompts 
        options = webdriver.ChromeOptions()
        options.add_experimental_option('excludeSwitches', ['enable-logging'])
        super(Stores, self).__init__(options=options)
        # Wait number of seconds specified:
        self.implicitly_wait(5)
        # self.maximize_window()

    def __exit__(self, *args):
        """
        Exits upon completion when previous class actions are complete.
        """
        if self.teardown:
            self.quit()
    
    def runSamsClub(self):
        """
        Sams Club still in work. Webpage prevents currently prevents 'robots'.
        """
        self.get(const.SAMS_URL)
        # self.refresh()
        # sams = SamsClub(driver = self)
        # header = self.find_element(By.TAG_NAME, 'HTML')
        sams = SamsClub(driver = self)
        # sams.byPassNoBots()

    def runCostco(self) -> list:
        """
        Analyzes costco.com analysis on baby formula.

        :return list: product details of baby formula
        """
        self.get(const.COSTCO_URL)
        priceClub = Costco(driver = self)
        priceClub.SortBy()
        priceClub.find_products()
        priceClub.pull_product_attributes()
        return priceClub.get_product_summary()

    def runTarget(self)->list:
        """
        Analyzes Target.com products

        :return list: list of lists containing product information
        """
        self.get(const.TARGET_URL)
        target = Target(driver = self)
        target.find_products()
        target.wait_for_all_elements('div[class="children"]')
        target.pull_product_attributes()
        return target.get_product_summary()

    def runAmazon(self)->list:
        """
        Analyzes Amazon Baby Mama infant formula

        :return list: list of lists containing product information
        """
        self.get(const.AMAZON_URL)
        amzn = Amazon(driver = self)
        amzn.searchBar('mama bear infant formula')
        amzn.find_products()
        amzn.pull_product_attributes()
        return amzn.get_product_summary()

    def runKroger(self)->list:
        """
        Analyzes Kroger Comforts brand infant formula. Easily IP blocked.

        :return list: list of lists containing product information
        """
        self.get(const.KROGER_URL)
        krgr = Kroger(driver = self)
        krgr.fight_popup()
        krgr.find_products()
        # krgr.pull_product_attributes()
        # return krgr.get_product_summary()

    def report_results(self) -> PrettyTable:
        """
        Queries multiple stores and generates the results into a Pretty Table.
        """
        table = PrettyTable(
            field_names = ['Product', 'Availability', 'Price', 'Store', 'URL']
        )
        # Costco - General
        # costcoQ = self.runCostco()
        # table.add_rows(costcoQ)
        
        # Target - General
        # targetQ = self.runTarget()
        # table.add_rows(targetQ)
        
        # Amazon - Mama Bear Brand
        amazonQ = self.runAmazon()
        table.add_rows(amazonQ)

        # Kroger - Comforts Brand - Under construction
        # krogerQ = self.runKroger()
        # table.add_rows(krogerQ)
        
        # self.get_JSON_table(table)
        # self.get_HTML_table(table)
        # self.display_file("table.json")
        # self.display_file("table.html")
        # self.display_results(table)
        print("\n>>> Search Complete <<<\n")
        return table
    
    def display_results(self, table: PrettyTable):
        print(table)

    def get_JSON_table(self, table: PrettyTable) -> None:
        """Returns the Pretty Table as a json string"""
        jsonFormat = table.get_json_string()
        f = open("table.json", 'w')
        f.write(jsonFormat)
        f.close()

    def get_HTML_table(self, table: PrettyTable) -> None:
        """Returns the Pretty Table as a HTML string"""
        htmlFormat = table.get_html_string()
        f = open("table.html", 'w')
        f.write(htmlFormat)
        f.close()
        return htmlFormat

    def display_file(self, filename: str):
        """Displays HTML table format"""
        f = open(filename, 'r')
        print(f.read())
        f.close()
    
    def get_CSV_table(self, table: PrettyTable):
        """Returns the Pretty Table as a CSV string"""
        return table.get_csv_string()

def main():
    test = Stores()

if __name__ == "__main__":
    main()