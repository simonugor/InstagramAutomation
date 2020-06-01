
from selenium import webdriver
import time
import datetime

def login(username, password):
    chromedriver = "/Users/simonugor/Desktop/FH Krems SS20/Programming/Instagram Automation/Instabot/chromedriver"
    driver = webdriver.Chrome(chromedriver)
    try:
        driver.get("https://www.instagram.com/?hl=sk")
        time.sleep(3)

        # opening login page
        try:
            login_page = driver.find_element_by_xpath('//*[@id="react-root"]/section/main/article/div[2]/div[2]/p/a')
            login_page.click()
            time.sleep(2)
        except:
            pass

        # typing in username
        username_field = driver.find_element_by_tag_name("input")
        username_field.send_keys(username)
        time.sleep(2)

        # typing in password
        password_field = driver.find_elements_by_tag_name("input")
        password_field[1].send_keys(password)
        time.sleep(2)

        # clicking login button
        login_button = driver.find_element_by_xpath(
            '//*[@id="react-root"]/section/main/article/div[2]/div[1]/div/form/div[4]/button')
        login_button.click()
        time.sleep(5)

        # clicking button "not now" for turning on notifications popup
        try:
            notnow_button = driver.find_element_by_xpath('/html/body/div[4]/div/div/div[3]/button[2]')
            notnow_button.click()
            time.sleep(3)
        except:
            pass

        print(str(datetime.datetime.now().time())[0:8], "Login done")

        time.sleep(2)

        driver.close()

        return True
    except:
        time.sleep(2)
        driver.close()
        return False
