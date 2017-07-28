from appium import webdriver
from test.fixture.navigation import NavigationHelper

from fixture.motion import MotionHelper


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
        self.navigation = NavigationHelper(self)
        self.motion = MotionHelper(self)


    def destroy(self):
        self.driver.quit()