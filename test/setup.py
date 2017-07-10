from appium import webdriver


def launch_app():
    global driver
    caps = {}
    caps["platformName"] = "Android"
    caps["platformVersion"] = "7.0"
    caps["deviceName"] = "Samsung Galaxy S7"
    caps["noReset"] = "True"
    caps["fullReset"] = "False"
    caps["appPackage"] = "com.motorsport.forix"
    caps["appActivity"] = "activity.MainActivity"
    # caps["app"] = "/Users/antonzapekin/Downloads/app/build/outputs/apk/app-debug.apk"
    driver = webdriver.Remote("http://localhost:4723/wd/hub", caps)
    # driver.start_activity("com.motorsport.forix","activity.MainActivity")