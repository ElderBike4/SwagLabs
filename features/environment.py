from selenium import webdriver

def before_all(context):
    # Configura la URI de Selenium Grid en el contenedor Docker
    selenium_uri = "http://localhost:4444"
    
    # Inicializa el controlador del navegador
    options = webdriver.ChromeOptions()
    context.driver = webdriver.Remote(command_executor=selenium_uri,options=options)

def after_all(context):
    # Cierra el controlador del navegador
    context.driver.quit()
