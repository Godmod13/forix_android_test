from appium import webdriver
from optparse import OptionParser
import time


class Application:

    def __init__(self):

        global driver
        parser = OptionParser()
        parser.add_option("-p", "--platform", action="store", type="string")
        (options, arguments) = parser.parse_args()

        if options.platform == "iOS":
            caps = {}
            caps["platformName"] = "iOS"
            caps["platformVersion"] = "10.2"
            caps["deviceName"] = "iPhone"
            caps["app"] = "/Users/antonzapekin/Forix.ipa"
            caps["udid"] = "e0f15d6cba4f6c4b695b739fd104e6dcf66e0ac7"
            caps["xcodeOrgId"] = "TU2MR5WU46"
            caps["xcodeSigningId"] = "iPhone"
            caps["fullReset"] = False
            caps["noReset"] = True
            self.driver = webdriver.Remote("http://localhost:4723/wd/hub", caps)
        elif options.platform == "Android":
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