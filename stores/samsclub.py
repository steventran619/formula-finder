from selenium.webdriver.remote.webdriver import WebDriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time


class SamsClub():
    def __init__(self, driver:WebDriver):
        self.driver = driver
    
    def byPassNoBots(self):
        t_end = time.time() + 10
        popUp = self.driver.find_element(By.CSS_SELECTOR, 'button[aria-label="close  modal"]')
        # header = self.driver.find_element(By.CSS_SELECTOR, 'div')
        WebDriverWait(self.driver, 30).until(
            self.driver.find_element(By.CSS_SELECTOR, 'button[aria-label="close  modal"]')
        )
        popUp = self.driver.find_element(By.CSS_SELECTOR, 'button[aria-label="close  modal"]')
        popUp.click()
        # WebDriverWait()
        # # instances = 0
        # while time.time() < t_end:
        # #     instances += 1
        #     header.send_keys(Keys.ESCAPE)
        #     # popUp.send_keys(Keys.ESCAPE)
        # # popUp.click()
        #     time.sleep(2)
        #     instances += 1
        #     print(f"{instances}Pressing Escape")


        # while time.time() < t_end:
        #     instances += 1
        #     if popUp:
        #         popUp.send_keys(Keys.ESCAPE)
        #         popUp.click()
        #         time.sleep(2)
        #         instances += 1
        #         print(f"{instances}Pressing Escape")