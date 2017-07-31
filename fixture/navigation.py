from selenium.common.exceptions import NoSuchElementException
from optparse import OptionParser
import time



class NavigationHelper:

    def __init__(self,app):
        self.app = app


    def open_news_page(self,platform):
        driver = self.app.driver
        if platform == "Android":
            self.app.driver.find_element_by_accessibility_id("Open navigation drawer").click()
            self.app.driver.find_element_by_accessibility_id("news_screen").click()
        elif platform == "iOS":
            self.app.driver.find_element_by_accessibility_id("news_screen").click()


    def open_events_page(self,platform):
        driver = self.app.driver
        if platform == "Android":
            self.app.driver.find_element_by_accessibility_id("Open navigation drawer").click()
            self.app.driver.find_element_by_accessibility_id("events_screen").click()
        elif platform == "iOS":
            self.app.driver.find_element_by_accessibility_id("events_screen").click()


    def open_live_page(self,platform):
        driver = self.app.driver
        if platform == "Android":
            self.app.driver.find_element_by_accessibility_id("Open navigation drawer").click()
            self.app.driver.find_element_by_accessibility_id("live_screen").click()
        elif platform == "iOS":
            self.app.driver.find_element_by_accessibility_id("live_screen").click()


    def open_analytics_page(self,platform):
        driver = self.app.driver
        if platform == "Android":
            self.app.driver.find_element_by_accessibility_id("Open navigation drawer").click()
            self.app.driver.find_element_by_accessibility_id("analytics_screen").click()
        elif platform == "iOS":
            self.app.driver.find_element_by_accessibility_id("analytics_screen").click()


    def open_settings_page(self,platform):
        driver = self.app.driver
        if platform == "Android":
            self.app.driver.find_element_by_accessibility_id("Open navigation drawer").click()
            self.app.driver.find_element_by_accessibility_id("settings_button").click()
        elif platform == "iOS":
            self.app.driver.find_element_by_accessibility_id("menu_button").click()
            self.app.driver.find_element_by_accessibility_id("settings_button").click()

    def open_legals_page(self,platform):
        driver = self.app.driver
        if platform == "Android":
            self.app.driver.find_element_by_accessibility_id("Open navigation drawer").click()
            self.app.driver.find_element_by_accessibility_id("legals_button").click()
        elif platform == "iOS":
            self.app.driver.find_element_by_accessibility_id("menu_button").click()
            self.app.driver.find_element_by_accessibility_id("legals_button").click()


    def back_root_home(self,platfrom):
        driver = self.app.driver
        if platfrom == "Android":
            main_menu = None
            button_found = False
            while button_found != True:
                try:
                    main_menu = self.app.driver.find_element_by_accessibility_id("Open navigation drawer")
                except NoSuchElementException:
                    self.app.driver.press_keycode(4)
                    time.sleep(1)
                else:
                    button_found = True

            main_menu.click()
            analytics_title = self.app.driver.find_element_by_xpath(
                "/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.support.v4.widget.DrawerLayout/android.widget.FrameLayout[1]/android.support.v7.widget.RecyclerView/android.support.v7.widget.LinearLayoutCompat[1]").click()


        elif platfrom == "iOS":
            main_menu = self.app.driver.find_element_by_accessibility_id("home_screen").click()

