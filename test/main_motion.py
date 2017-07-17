import time
import test.setup
from selenium.common.exceptions import NoSuchElementException
from optparse import OptionParser


parser = OptionParser()
parser.add_option("-p", "--platform", action="store", type="string")
(options, arguments) = parser.parse_args()


def back_root_home():
        if options.platform == "Android":
            main_menu = None
            button_found = False
            while button_found != True:
                try:
                    main_menu = test.setup.driver.find_element_by_accessibility_id("Open navigation drawer")
                except NoSuchElementException:
                    test.setup.driver.press_keycode(4)
                    time.sleep(1)
                else:
                    button_found = True

            main_menu.click()
            analytics_title = test.setup.driver.find_element_by_xpath(
                "/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.support.v4.widget.DrawerLayout/android.widget.FrameLayout[1]/android.support.v7.widget.RecyclerView/android.support.v7.widget.LinearLayoutCompat[1]").click()


        elif options.platform == "iOS":
            main_menu = test.setup.driver.find_element_by_accessibility_id("Dashboard").click()
