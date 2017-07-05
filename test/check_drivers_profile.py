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

#open Events menu
main_menu = driver.find_element_by_accessibility_id("Open navigation drawer").click()
button_menu = driver.find_elements_by_id("com.motorsport.forix:id/design_menu_item_text")

for button in button_menu:

    if button.get_attribute("text") == "Events":
        button.click()
        break


#open Results by Series
results_by_series_button=driver.find_element_by_id("com.motorsport.forix:id/button_with_arrow_text").click()
series_button = driver.find_element_by_id("com.motorsport.forix:id/title").click()

#open Drivers menu
button_racers_array = driver.find_elements_by_id("com.motorsport.forix:id/button_with_arrow_text")

for button in button_racers_array:

    if button.get_attribute("text") == "Drivers":
        button.click()
        break

#open Drivers profile and swipe
racer_button=driver.find_element_by_id("com.motorsport.forix:id/button_with_arrow_text").click()
time.sleep(1)
drivers_swipe = driver.swipe(500, 1800, 500, 350, 1500)

#return to Home page
main_motion.back_root_home(driver)

#quit from app
driver.quit()