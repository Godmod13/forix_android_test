import random


class ItemHelper:
    def __init__(self,app):
        self.app = app


    def open_some_event_item(self):
        driver = self.app.driver
        events_list = self.app.driver.find_elements_by_accessibility_id("event_item")
        print(random.choice(events_list))



