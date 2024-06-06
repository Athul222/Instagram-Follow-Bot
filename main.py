from time import sleep
from dotenv import dotenv_values
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.common.exceptions import ElementClickInterceptedException

config = {
    **dotenv_values("instagram follow bot/.env")
}
# instagram URL 
INSTAGRAM_PATH = "https://www.instagram.com/accounts/login/"
# `Your` instagram username and credentials
INSTAGRAM_USERNAME = config["USERNAME"]
INSTAGRAM_PASSWORD = config["PASSWORD"]
# Enter some random instagram id
SIMILAR_ACCOUNT = "crunchyroll"

chrome_options = webdriver.ChromeOptions()
chrome_options.add_experimental_option("detach", True)
chrome_driver = webdriver.Chrome(options= chrome_options)

class InstagramFollowerBot:
    def __init__(self):
        self.driver = chrome_driver
        
    def instagram_login(self):
        self.driver.get(url= INSTAGRAM_PATH)
        sleep(2)
        username_field = self.driver.find_element(By.NAME, value="username")
        username_field.send_keys(INSTAGRAM_USERNAME)
        password_field = self.driver.find_element(By.NAME, value="password")
        password_field.send_keys(INSTAGRAM_PASSWORD)
        password_field.send_keys(Keys.ENTER)
    
    def find_followers(self):
        sleep(3)
        notification_button = self.driver.find_element(By.XPATH, 
                                 value="//button[contains(text(), 'Not Now')]")
        sleep(3)
        notification_button.click()
        sleep(2)
        self.driver.get(url= "https://www.instagram.com/crunchyroll/followers/")
        
        # Scrowling down the pop up
        sleep(5.2)
        modal_xpath = '/html/body/div[6]/div[1]/div/div[2]/div/div/div/div/div[2]/div/div/div[2]'
        modal = self.driver.find_element(by=By.XPATH, value= modal_xpath)
        for i in range(10):
            self.driver.execute_script("arguments[0].scrollTop = arguments[0].scrollHeight", modal)
            sleep(2)
        
    def follow(self):
        followers_list = self.driver.find_elements(by=By.CSS_SELECTOR, 
                                value="body > div.x1n2onr6.xzkaem6 > div.x9f619.x1n2onr6.x1ja2u2z > div > div.x1uvtmcs.x4k7w5x.x1h91t0o.x1beo9mf.xaigb6o.x12ejxvf.x3igimt.xarpa2k.xedcshv.x1lytzrv.x1t2pt76.x7ja8zs.x1n2onr6.x1qrby5j.x1jfb8zj > div > div > div > div > div.x7r02ix.xf1ldfh.x131esax.xdajt7p.xxfnqb6.xb88tzc.xw2csxc.x1odjw0f.x5fp0pe > div > div > div._aano > div:nth-child(2) > div > div button")
        for user in followers_list:
            try:
                user.click()
                sleep(2)
            
            except ElementClickInterceptedException:
                cancel_button = self.driver.find_element(by=By.XPATH, 
                                                        value="//button[contains(text(), 'Cancel')]")
                cancel_button.click()
                sleep(1.1)

bot = InstagramFollowerBot()
bot.instagram_login()
bot.find_followers()
bot.follow()


