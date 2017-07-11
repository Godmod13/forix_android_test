
import test.setup
import test.main_motion


#initialization
test.setup.launch_app()

#open Events menu
main_menu = test.setup.driver.find_element_by_accessibility_id("Open navigation drawer").click()
button_menu = test.setup.driver.find_elements_by_id("com.motorsport.forix:id/design_menu_item_text")

for button in button_menu:

    if button.get_attribute("text") == "Events":
        button.click()
        break



#open event

events = test.setup.driver.find_elements_by_id("com.motorsport.forix:id/title")
print(events)
