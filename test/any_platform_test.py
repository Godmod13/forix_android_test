import pytest
import time
#import test.main_motion
from selenium.common.exceptions import NoSuchElementException
from optparse import OptionParser
from test.application1 import Application


parser = OptionParser()
parser.add_option("-p", "--platform", action="store", type="string")
(options, arguments) = parser.parse_args()

@pytest.fixture
def app(request):
    fixture = Application()
    request.addfinalizer(fixture.destroy)
    return fixture


#swipe News on dasboard
def test_swipe_news(app):
    app.swipe_news()


#return to Home page
def back_root_home(app):
    if options.platform == "Android":
        main_menu = None
        button_found = False
        while button_found != True:
            try:
                main_menu = app.driver.find_element_by_accessibility_id("Open navigation drawer")
            except NoSuchElementException:
                app.driver.press_keycode(4)
                time.sleep(1)
            else:
                button_found = True

        main_menu.click()
        analytics_title = app.driver.find_element_by_xpath(
            "/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.support.v4.widget.DrawerLayout/android.widget.FrameLayout[1]/android.support.v7.widget.RecyclerView/android.support.v7.widget.LinearLayoutCompat[1]").click()


    elif options.platform == "iOS":
        main_menu = app.driver.find_element_by_accessibility_id("home_screen").click()

