from appium import webdriver
from optparse import OptionParser
import time


class Application:

    def __init__(self):

        caps = {}
        caps["platformName"] = "Android"
        caps["platformVersion"] = "7.0"
        caps["deviceName"] = "Samsung Galaxy S7"
        caps["fullReset"] = False
        caps["noReset"] = True
        caps["appPackage"] = "com.motorsport.forix"
        caps["appActivity"] = "activity.MainActivity"
        caps["app"] = "/Users/antonzapekin/app-debug.apk"
        self.driver = webdriver.Remote("http://localhost:4723/wd/hub", caps)



    def swipe_news(self):
        driver = self.driver
        time.sleep(1)
        driver.swipe(800, 800, 100, 800)




    def destroy(self):
        self.driver.quit()