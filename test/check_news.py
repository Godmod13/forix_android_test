# This sample code uses the Appium python client
# pip install Appium-Python-Client
# Then you can paste this into a file and simply run with Python

from appium import webdriver
import time
import main_motion


#initialization
caps = {}
caps["platformName"] = "Android"
caps["platformVersion"] = "7.0"
caps["deviceName"] = "Samsung Galaxy S7"
caps["app"] = "/Users/antonzapekin/Downloads/app/build/outputs/apk/app-debug.apk"
driver = webdriver.Remote("http://localhost:4723/wd/hub", caps)

#swipe News on dasboard
time.sleep(1)
first_news = driver.swipe(800, 800, 100, 800)
second_news = driver.swipe(800, 800, 100, 800)
third_news = driver.swipe(800, 800, 100, 800)


#open all News
button_array = driver.find_elements_by_id("com.motorsport.forix:id/base_button")
for button in button_array:

    if button.get_attribute("text") == "ALL NEWS":
        button.click()
        break

#swipe news list
drivers_swipe = driver.swipe(500, 1800, 500, 350, 1500)

#open anyone news
time.sleep(1)
click_news = driver.find_element_by_id("com.motorsport.forix:id/news_text").click()

#return to Home page
main_motion.back_root_home(driver)


#quit from app
driver.quit()