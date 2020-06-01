from selenium import webdriver
import time

def log_into_account_stats(username, password):
    try:
        chromedriver = "/Users/simonugor/Desktop/FH Krems SS20/Programming/Instagram Automation/Instabot/chromedriver"
        driver = webdriver.Chrome(chromedriver)
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
        notnow_button = driver.find_element_by_xpath('/html/body/div[4]/div/div/div[3]/button[2]')
        notnow_button.click()
        time.sleep(3)

        #print(str(datetime.datetime.now().time())[0:8], "Login done")

        toopen = ("https://www.instagram.com/" + str(username))
        time.sleep(1)
        driver.get(toopen)
        time.sleep(2)


        number_of_posts = driver.find_element_by_xpath('/html/body/div[1]/section/main/div/header/section/ul/li[1]/span/span').text
        number_of_followers = driver.find_element_by_xpath('/html/body/div[1]/section/main/div/header/section/ul/li[2]/a/span').text
        number_of_following = driver.find_element_by_xpath('/html/body/div[1]/section/main/div/header/section/ul/li[3]/a/span').text

        message_stats = "Your account currently has:"
        message_posts = (str(number_of_posts) + " posts")
        message_followers = (str(number_of_followers) + " followers")
        message_following = ("and you are following " + str(number_of_following) + " accounts.")

        time.sleep(1)

        driver.close()

        #maybe add followers to following ratio
        #try to do average post likes

        return message_stats, message_posts, message_followers, message_following
    except:
        time.sleep(2)
        driver.close()
        return False