import time


class MotionHelper:

    def __init__(self,app):
        self.app = app


    def height_res(self):
        driver = self.app.driver
        windows_size = self.app.driver.get_window_size()
        screen_height = windows_size.get('height')
        return screen_height

    def width_res(self):
        driver = self.app.driver
        windows_size = self.app.driver.get_window_size()
        screen_width = windows_size.get('width')
        return screen_width

    def swipe_left(self):
        driver = self.app.driver
        startx = self.width_res() * 0.8
        endx = self.width_res() * 0.2
        starty = self.height_res() * 0.45
        endy = self.height_res() * 0.45
        if self.app.platform == "iOS":
            print(startx,starty,endx, endy)
            self.app.driver.swipe(startx,starty,endx-startx,endy-starty,1000)
        elif self.app.platform == "Android":
            self.app.driver.swipe(startx,starty,endx,endy,1000)

    def swipe_right(self):
        driver = self.app.driver
        startx = self.width_res() * 0.2
        endx = self.width_res() * 0.8
        starty = self.height_res() * 0.45
        endy = self.height_res() * 0.45
        if self.app.platform == "iOS":
            print(startx,starty,endx, endy)
            self.app.driver.swipe(startx,starty,endx-startx,endy-starty,1000)
        elif self.app.platform == "Android":
            self.app.driver.swipe(startx,starty,endx,endy,1000)


    def scroll_down(self):
        driver = self.app.driver
        startx = self.width_res() * 0.45
        endx = self.width_res() * 0.45
        starty = self.height_res() * 0.9
        endy = self.height_res() * 0.15
        if self.app.platform == "iOS":
            print(startx,starty,endx, endy)
            self.app.driver.swipe(startx,starty,endx-startx,endy-starty,1000)
        elif self.app.platform == "Android":
            self.app.driver.swipe(startx,starty,endx,endy,1500)


    def scroll_up(self):
        driver = self.app.driver
        startx = self.width_res() * 0.45
        endx = self.width_res() * 0.45
        starty = self.height_res() * 0.19
        endy = self.height_res() * 0.9
        if self.app.platform == "iOS":
            print(startx,starty,endx, endy)
            self.app.driver.swipe(startx,starty,endx-startx,endy-starty,1000)
        elif self.app.platform == "Android":
            self.app.driver.swipe(startx,starty,endx,endy,1500)