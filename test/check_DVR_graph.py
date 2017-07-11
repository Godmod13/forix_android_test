# This sample code uses the Appium python client
# pip install Appium-Python-Client
# Then you can paste this into a file and simply run with Python

import time
import test.main_motion


#initialization
test.setup.launch_app()

#open Analytics menu
main_menu = test.setup.driver.find_element_by_accessibility_id("Open navigation drawer").click()
analytics_title = test.setup.driver.find_element_by_xpath("/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.support.v4.widget.DrawerLayout/android.widget.FrameLayout[1]/android.support.v7.widget.RecyclerView/android.support.v7.widget.LinearLayoutCompat[5]").click()

#open Formula 1 series
all_series = test.setup.driver.find_element_by_id("com.motorsport.forix:id/series").click()

#scroll graphics
graphics_swipe = test.setup.driver.swipe(1000, 1000, 300, 1000, 500)
time.sleep(1)
graphics_swipe = test.setup.driver.swipe(1000, 1000, 300, 1000, 500)
time.sleep(1)
graphics_swipe = test.setup.driver.swipe(1000, 1000, 300, 1000, 500)
time.sleep(1)

#open another graphic
map_chart = test.setup.driver.find_elements_by_class_name("android.widget.HorizontalScrollView")
click_map2 = test.setup.driver.tap([(350, 500), (350,500)],500)
time.sleep(1)

#scroll graphic
graphics_swipe_reverse = test.setup.driver.swipe(300, 1000, 1000, 1000, 500)
time.sleep(1)
graphics_swipe_reverse = test.setup.driver.swipe(300, 1000, 1000, 1000, 500)
time.sleep(1)
graphics_swipe_reverse = test.setup.driver.swipe(300, 1000, 1000, 1000, 500)
time.sleep(1)

#return to Home page
test.main_motion.back_root_home()
#quit from app
test.setup.driver.quit()