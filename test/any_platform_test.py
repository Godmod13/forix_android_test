import time


#swipe News on dasboard
# def test_swipe_news(app):
#     time.sleep(1)
#     app.motion.swipe_left()
#     app.motion.swipe_left()
#     app.motion.swipe_left()
#
#
# def test_swipe_news_back(app):
#     time.sleep(1)
#     app.motion.swipe_right()
#     app.motion.swipe_right()



# def test_windows_size(app):
#     time.sleep(1)
#     app.navigation.open_events_page()
#     # app.motion.swipe_left()
#     # app.motion.swipe_right()
#     app.motion.scroll_down()
#     # time.sleep(1)
#     # app.motion.scroll_up()


def test_random_open_element(app):
    app.navigation.open_events_page()
    app.item.open_some_event_item()
