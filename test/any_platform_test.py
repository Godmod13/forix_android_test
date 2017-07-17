import time
import test.setup
import test.main_motion

# #initialization
test.setup.launch_app()

#swipe News on dasboard
time.sleep(1)
first_news = test.setup.driver.swipe(600, 600, 100, 600)
second_news = test.setup.driver.swipe(600, 600, 100, 600)
third_news = test.setup.driver.swipe(600, 600, 100, 600)

#return to Home page
test.main_motion.back_root_home()


#quit from app
test.setup.driver.quit()