import time


#swipe News on dasboard
def test_swipe_news(app):
    time.sleep(1)
    app.motion.swipe_left()
    app.motion.swipe_left()
    app.motion.swipe_left()


#return to Home page


