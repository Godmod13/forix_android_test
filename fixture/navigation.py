from selenium.common.exceptions import NoSuchElementException
from optparse import OptionParser
import time



class NavigationHelper:

    def __init__(self,app):
        self.app = app


    def open_news_page(self):
        driver = self.app.driver
        pass



    def open_events_page(self):
        driver = self.app.driver
        pass


    def open_live_page(self):
        driver = self.app.driver
        pass


    def open_analytics_page(self):
        driver = self.app.driver
        pass


    def open_settings_page(self):
        driver = self.app.driver
        pass


    def open_legals_page(self):
        driver = self.app.driver
        pass


    def back_root_home(self):
        driver = self.app.driver
        parser = OptionParser()
        parser.add_option("-p", "--platform", action="store", type="string")
        (options, arguments) = parser.parse_args()
        if options.platform == "Android":
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


        elif options.platform == "iOS":
            main_menu = self.app.driver.find_element_by_accessibility_id("home_screen").click()

