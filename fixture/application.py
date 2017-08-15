from appium import webdriver
from fixture.navigation import NavigationHelper
from fixture.motion import MotionHelper
from fixture.item import ItemHelper


class Application:

    def __init__(self, platform):
        if platform == "Android":
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
        elif platform == "iOS":
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
        else:
            raise ValueError("Unrecognized platform %s" % platform)

        self.navigation = NavigationHelper(self)
        self.motion = MotionHelper(self)
        self.item = ItemHelper(self)
        self.platform = platform



    def is_valid(self):
        try:
            pass
            return True
        except:
            return False


    def destroy(self):
        self.driver.quit()