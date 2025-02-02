from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains
from selenium.common.exceptions import NoSuchElementException, TimeoutException
from selenium.common.exceptions import ElementClickInterceptedException, NoSuchElementException
from datetime import datetime
import time
import pandas

USERNAME = "YOURINSTAID"
PASSWORD = "YOURPASSWORD"


class Birthday:
    def __init__(self):
        chrome_options = webdriver.ChromeOptions()
        chrome_options.add_experimental_option("detach", True)
        self.driver = webdriver.Chrome(options=chrome_options)

    def login(self):
        url = "https://www.instagram.com/accounts/login/"
        self.driver.get(url)
        time.sleep(4.2)  

 
        try:
            username = self.driver.find_element(By.NAME, "username")
            password = self.driver.find_element(By.NAME, "password")
            username.send_keys(USERNAME)
            password.send_keys(PASSWORD)
            time.sleep(2.1)
            password.send_keys(Keys.ENTER)
            print("Login details entered.")
        except NoSuchElementException as e:
            print(f"Error finding login fields: {e}")


        time.sleep(9)  
        try:
            notifications_prompt = self.driver.find_element(By.XPATH, "/html/body/div[2]/div/div/div[2]/div/div/div[1]/div[1]/div[1]/section/main/div/div/div/div")
            notifications_prompt.click()
            print("Notifications prompt clicked.")
        except NoSuchElementException as e:
            print(f"Error finding notifications prompt: {e}")

    def sendmessage(self, ID, message):
        try:
            time.sleep(10)  
            searchbutton = self.driver.find_element(By.XPATH, value='/html/body/div[1]/div/div/div[2]/div/div/div[1]/div[1]/div[2]/div/div/div/div/div[2]/div[2]/span/div/a')                                          
            searchbutton.click()
        except TimeoutException as e:
            print(f"Timeout error: {e}")
        
        try:
            time.sleep(8)
            input_field = self.driver.find_element(By.XPATH, value="//input[@placeholder= 'Search']")
            input_field.send_keys(ID)
            input_field.send_keys(Keys.ENTER)
        
        except NoSuchElementException as e:
            print(f"Error finding notifications prompt: {e}")

        
        try:
            time.sleep(8)  
            first_person = self.driver.find_element(By.XPATH, value='/html/body/div[1]/div/div/div[2]/div/div/div[1]/div[1]/div[2]/div/div/div[2]/div/div/div[2]/div/div/div[2]/div/a[1]')

               
            self.driver.execute_script("arguments[0].scrollIntoView(true);", first_person)

                
            first_person.click()
        except ElementClickInterceptedException:
            print("ElementClickInterceptedException: An overlay is blocking the click.")
        try:
            
            overlay = self.driver.find_element(By.CLASS_NAME, value='x1qjc9v5')  
            self.driver.execute_script("arguments[0].click();", overlay)
            print("Overlay dismissed.")
            
            first_person.click()
        except NoSuchElementException:
            print("No overlay found to dismiss.")
        except NoSuchElementException as e:
            print(f"Error finding the first person element: {e}")


        try:
            time.sleep(8)
            message_button = self.driver.find_element(By.XPATH, value="//div[contains(text(), 'Message')]")
            message_button.click()
        except NoSuchElementException as e:
            print(f"Error finding the first person element: {e}")


        time.sleep(8)  

        try:
            not_now_button = self.driver.find_element(By.CLASS_NAME, '_a9--')

            not_now_button.click()
        
        except Exception as e:
            print(f"An error occurred: {e}")      

        time.sleep(5)
        try:

            message_box = self.driver.find_element(By.XPATH, value='/html/body/div[1]/div/div/div[2]/div/div/div[1]/div[1]/div[1]/section/main/section/div/div/div/div[1]/div/div[2]/div/div/div[1]/div/div/div/div[2]/div/div/div[2]/div/div/div[2]/div/div[1]')
            message_box.send_keys(f'{message}')
            message_box.send_keys(Keys.ENTER)


        except Exception as e:
            print(f"An error occurred: {e}")  

    def check_birthdate(self):
        today = datetime.now()
        today_tupple = (today.month, today.day)

        data = pandas.read_csv("birthdays.csv")
        birthdays_dict = {(data_row["MONTH"], data_row["DAY"]): data_row for (index, data_row) in data.iterrows()}

        if today_tupple in birthdays_dict:
            self.login()
            self.sendmessage(birthdays_dict[today_tupple]["ID"], "Happy Birthday" ) 
        

            
bot = Birthday()
bot.check_birthdate()

