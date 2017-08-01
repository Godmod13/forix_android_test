from optparse import OptionParser
import time


class MotionHelper:

    def __init__(self,app):
        self.app = app


    def height_res(self):
        driver = self.app.driver
        windows_size = self.app.driver.get_window_size()
        screen_height = windows_size.get('height')
        return screen_height

    def weight_res(self):
        driver = self.app.driver
        windows_size = self.app.driver.get_window_size()
        screen_weight = windows_size.get('weight')
        return screen_weight

    def swipe_left(self):
        driver = self.app.driver
        startx = self.weight_res()
        print(startx)
        endx = None
        starty = None
        endy = None
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