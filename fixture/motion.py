from optparse import OptionParser
import time


class MotionHelper:

    def __init__(self,app):
        self.app = app


    def swipe_left(self):
        driver = self.app.driver
        self.app.driver.swipe(800, 800, 100, 800,1000)



    def swipe_right(self):
        driver = self.app.driver
        self.app.driver.swipe(100, 800, 800, 800,1000)


    def scroll_down(self):
        driver = self.app.driver
        self.app.driver.swipe(500, 1500, 500, 500,1000)


    def scroll_up(self):
        driver = self.app.driver
        self.app.driver.swipe(500, 500, 500, 1500,1000)