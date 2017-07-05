from appium import webdriver
#from fixture.session import SessionHelper

import time

class Application:

    def __init__(self, device):
        if device == "Android":
            caps = {}
            caps["platformName"] = "Android"
            caps["platformVersion"] = "7.0"
            caps["deviceName"] = "Samsung Galaxy S7"
            caps["app"] = "/Users/antonzapekin/Downloads/app/build/outputs/apk/app-debug.apk"
            driver = webdriver.Remote("http://localhost:4723/wd/hub", caps)


        elif device =="iOS":
            pass
        else:
            raise ValueError("Unrecognized device %s" % device)

        self.wd.implicitly_wait(1)
        # self.session = SessionHelper(self)
        # self.group = GroupHelper(self)
        # self.contact = ContactHelper(self)
        # self.base_url = base_url


    # def is_valid(self):
    #     try:
    #         self.wd.current_url
    #         return True
    #     except:
    #         return False
    #
    #
    # def open_home_page(self):
    #         wd = self.wd
    #         wd.get(self.base_url)
    #         #time.sleep(2)


    def destroy(self):
        self.driver.quit()