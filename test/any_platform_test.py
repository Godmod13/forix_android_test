import time
import test.setup
import test.main_motion

# #initialization
test.setup.application()

#swipe News on dasboard
time.sleep(1)
first_news = test.setup.driver.swipe(800, 800, 100, 800)
# test.main_motion.swipe_right()
# #time.sleep(1)
# test.main_motion.swipe_left()
# #time.sleep(1)
# test.main_motion.scroll_down()
# #time.sleep(1)
# test.main_motion.scroll_up()
# #time.sleep(1)


#return to Home page
test.main_motion.back_root_home()


#quit from app
test.setup.driver.quit()
