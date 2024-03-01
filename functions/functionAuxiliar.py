import allure

def capture_screenshot(context, title):
    for browser_name, driver in context.driver.items():
        allure.attach(driver.get_screenshot_as_png(), name=f'{title}_{browser_name}', attachment_type=allure.attachment_type.PNG)
