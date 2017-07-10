# This sample code uses the Appium python client
# pip install Appium-Python-Client
# Then you can paste this into a file and simply run with Python

import time
import test.setup


# #initialization
test.setup.launch_app()

#swipe News on dasboard
time.sleep(1)
first_news = test.setup.driver.swipe(800, 800, 100, 800)
second_news = test.setup.driver.swipe(800, 800, 100, 800)
third_news = test.setup.driver.swipe(800, 800, 100, 800)


#open all News
button_array = test.setup.driver.find_elements_by_id("com.motorsport.forix:id/base_button")
for button in button_array:

    if button.get_attribute("text") == "ALL NEWS":
        button.click()
        break

#swipe news list
drivers_swipe = test.setup.driver.swipe(500, 1800, 500, 350, 1500)

#open anyone news
time.sleep(1)
click_news = test.setup.driver.find_element_by_id("com.motorsport.forix:id/news_text").click()

#return to Home page
test.main_motion.back_root_home()


#quit from app
test.setup.driver.quit()