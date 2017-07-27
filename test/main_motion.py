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
            main_menu = test.setup.driver.find_element_by_accessibility_id("home_screen").click()

def swipe_right():
    d = test.setup.driver.get_window_size()
    max_width = d.get_Width()
    max_height = d.get_Height()

    print(max_width)
    print(max_height)
    test.setup.driver.swipe(250, 150, 100, 150,1000)


def swipe_left():
    test.setup.driver.swipe(100, 250, 250, 250,1000)


def scroll_down():
    test.setup.driver.swipe(300, 600, 300, 300,1000)


def scroll_up():
    test.setup.driver.swipe(300, 500, 300, 100,1000)
