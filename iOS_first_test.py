from appium import webdriver

caps = {}
caps["platformName"] = "iOS"
caps["platformVersion"] = "10.2"
caps["deviceName"] = "iPhone"
caps["app"] = "/Users/antonzapekin/Forix.ipa"
caps["udid"] = "e0f15d6cba4f6c4b695b739fd104e6dcf66e0ac7"
caps["xcodeOrgId"] = "TU2MR5WU46"
caps["xcodeSigningId"] = "iPhone"
caps["fullReset"] = False
caps["noReset"] = True

driver = webdriver.Remote("http://localhost:4723/wd/hub", caps)


el1 = driver.find_element_by_accessibility_id("News").click()
el2 = driver.find_element_by_accessibility_id("News").click()
el3 = driver.find_element_by_accessibility_id("Events").click()
el4 = driver.find_element_by_accessibility_id("Event 3").click()
