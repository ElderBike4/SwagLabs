from selenium import webdriver

def before_all(context):
    # Configura la URI de Selenium Grid en el contenedor Docker
    selenium_uri = "http://localhost:4444"
    
    # Inicializa el controlador del navegador

    chrome_options = webdriver.ChromeOptions()
    context.chrome_driver = webdriver.Remote(command_executor=selenium_uri,
                                             options=chrome_options)
    firefox_options = webdriver.FirefoxOptions()
    context.firefox_driver = webdriver.Remote(command_executor=selenium_uri,options=firefox_options)

    edge_options = webdriver.EdgeOptions()
    context.edge_driver = webdriver.Remote(command_executor=selenium_uri,options=edge_options)

    context.driver = {
        "chrome": context.chrome_driver,
        "firefox": context.firefox_driver,
        "edge": context.edge_driver
        
    }

def after_all(context):
    # Cierra el controlador del navegador
    context.chrome_driver.quit()
    context.firefox_driver.quit()
    context.edge_driver.quit()
