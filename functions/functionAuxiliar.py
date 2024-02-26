import allure

def capture_screenshot(context,tittle):
    allure.attach(context.driver.get_screenshot_as_png(), name=tittle, attachment_type=allure.attachment_type.PNG)