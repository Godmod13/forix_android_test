import time
import test.setup
from selenium.common.exceptions import NoSuchElementException


def back_root_home():
        main_menu = None
        button_found = False
        while button_found != True:
            try:
                main_menu = test.setup.driver.find_element_by_xpath("//android.widget.ImageButton[@content-desc=\"Open navigation drawer\"]")
            except NoSuchElementException:
                test.setup.driver.press_keycode(4)
                time.sleep(1)
            else:
                button_found = True

        main_menu.click()
        analytics_title = test.setup.driver.find_element_by_xpath(
            "/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.support.v4.widget.DrawerLayout/android.widget.FrameLayout[1]/android.support.v7.widget.RecyclerView/android.support.v7.widget.LinearLayoutCompat[1]").click()
