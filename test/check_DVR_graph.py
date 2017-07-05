# This sample code uses the Appium python client
# pip install Appium-Python-Client
# Then you can paste this into a file and simply run with Python

from appium import webdriver
import time
import main_motion


#initialization
caps = {}
caps["platformName"] = "Android"
caps["platformVersion"] = "7.0"
caps["deviceName"] = "Samsung Galaxy S7"
caps["app"] = "/Users/antonzapekin/Downloads/app/build/outputs/apk/app-debug.apk"
driver = webdriver.Remote("http://localhost:4723/wd/hub", caps)

#open Analytics menu
main_menu = driver.find_element_by_xpath("//android.widget.ImageButton[@content-desc=\"Open navigation drawer\"]").click()
analytics_title = driver.find_element_by_xpath("/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.support.v4.widget.DrawerLayout/android.widget.FrameLayout[1]/android.support.v7.widget.RecyclerView/android.support.v7.widget.LinearLayoutCompat[5]").click()

#open Formula 1 series
all_series = driver.find_element_by_id("com.motorsport.forix:id/series").click()

#scroll graphics
graphics_swipe = driver.swipe(1000, 1000, 300, 1000, 500)
time.sleep(1)
graphics_swipe = driver.swipe(1000, 1000, 300, 1000, 500)
time.sleep(1)
graphics_swipe = driver.swipe(1000, 1000, 300, 1000, 500)
time.sleep(1)

#open another graphic
map_chart = driver.find_elements_by_class_name("android.widget.HorizontalScrollView")
click_map2 = driver.tap([(350, 500), (350,500)],500)
time.sleep(1)

#scroll graphic
graphics_swipe_reverse = driver.swipe(300, 1000, 1000, 1000, 500)
time.sleep(1)
graphics_swipe_reverse = driver.swipe(300, 1000, 1000, 1000, 500)
time.sleep(1)
graphics_swipe_reverse = driver.swipe(300, 1000, 1000, 1000, 500)
time.sleep(1)

#return to Home page
main_motion.back_root_home(driver)
#quit from app
driver.quit()