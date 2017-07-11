# This sample code uses the Appium python client
# pip install Appium-Python-Client
# Then you can paste this into a file and simply run with Python


import time
import test.setup
import test.main_motion


#initialization
test.setup.launch_app()

#open Events menu
main_menu = test.setup.driver.find_element_by_accessibility_id("Open navigation drawer").click()
button_menu = test.setup.driver.find_elements_by_id("com.motorsport.forix:id/design_menu_item_text")

for button in button_menu:

    if button.get_attribute("text") == "Events":
        button.click()
        break


#open Results by Series
results_by_series_button = test.setup.driver.find_element_by_id("com.motorsport.forix:id/button_with_arrow_text").click()
series_button = test.setup.driver.find_element_by_id("com.motorsport.forix:id/title").click()

#open Drivers menu
button_racers_array = test.setup.driver.find_elements_by_id("com.motorsport.forix:id/button_with_arrow_text")

for button in button_racers_array:

    if button.get_attribute("text") == "Drivers":
        button.click()
        break

#open Drivers profile and swipe
racer_button = test.setup.driver.find_element_by_id("com.motorsport.forix:id/button_with_arrow_text").click()
time.sleep(1)
drivers_swipe = test.setup.driver.swipe(500, 1800, 500, 350, 1500)

#return to Home page
test.main_motion.back_root_home()

#quit from app
test.setup.driver.quit()