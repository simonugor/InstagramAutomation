from selenium import webdriver
import time

def login_follow_likers(username, password, account, time_interval, amount_of_accounts):
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

        ig_url = "https://www.instagram.com/" + str(account) + "/"
        driver.get(ig_url)
        time.sleep(3)

        #opening latest picture and likers of this picture
        try:
            latest_pic = driver.find_element_by_xpath('/html/body/div[1]/section/main/div/div[3]/article/div/div/div[1]/div[1]/a/div/div[2]')
            latest_pic.click()
        except:
            try:
                latest_pic = driver.find_element_by_xpath('/html/body/div[1]/section/main/div/div[3]/article/div/div/div[1]/div[1]/a/div/div[1]')
                latest_pic.click()
            except:
                print("not able to open picture")
                driver.close()
                return False

        time.sleep(5)

        try:
            likes_button = driver.find_element_by_xpath('/html/body/div[4]/div[2]/div/article/div[2]/section[2]/div/div/button')
            likes_button.click()
        except:
            try:
                likes_button = driver.find_element_by_xpath('/html/body/div[4]/div[2]/div/article/div[2]/section[2]/div/div[2]/button')
                likes_button.click()
            except:
                print("not able to open likers")
                driver.close()
                return False

        time.sleep(5)

        #getting usernames, scrolling and following them
        only_names = []
        try:
            window_to_scroll = driver.find_element_by_xpath('/html/body/div[5]/div/div[2]/div')

            scroll_value = 300
            for i in range(10):
                try:
                    #print("im here")
                    #print(scroll_value)
                    driver.execute_script("arguments[0].scrollTo(0, arguments[1])", window_to_scroll, scroll_value)
                    scroll_value = scroll_value + 300
                    #print("execute.script worked")
                except:
                    print("didnt")
                time.sleep(5)
        except:
            window_to_scroll = driver.find_element_by_xpath('/html/body/div[5]/div')
            scroll_value = 300
            for i in range(10):
                try:
                    #print("im here")
                    #print(scroll_value)
                    driver.execute_script("arguments[0].scrollTo(0, arguments[1])", window_to_scroll, scroll_value)
                    scroll_value = scroll_value + 300
                    #print("execute.script worked")
                except:
                    print("didnt")
                time.sleep(5)

        names = window_to_scroll.find_elements_by_tag_name("a")
        for name in names:
            if name.text != '':
                only_names.append(name.text)
        #print(only_names)
        #print(len(only_names))

        time.sleep(5)

        if amount_of_accounts <= len(only_names):
            for i in range(amount_of_accounts):
                try:
                    driver.get("https://www.instagram.com/" + only_names[i] + "/")
                    time.sleep(5)
                    try:
                        follow_button = driver.find_element_by_xpath('/html/body/div[1]/section/main/div/header/section/div[1]/button')
                        time.sleep(2)
                        follow_button.click()
                        time.sleep(time_interval)
                    except:
                        follow_button = driver.find_element_by_xpath('/html/body/div[1]/section/main/div/header/section/div[1]/div[1]/span/span[1]/button')
                        time.sleep(2)
                        follow_button.click()
                        time.sleep(time_interval)
                    print("Followed " + only_names[i])
                    print("Waiting " + time_interval + " seconds")
                except:
                    print("Error following " + only_names[i])
                    time.sleep(time_interval)
        elif amount_of_accounts > len(only_names):
            return "toomanyaccounts"

        driver.close()
        return True

    except:
        driver.close()
        return False