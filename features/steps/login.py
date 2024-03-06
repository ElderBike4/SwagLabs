from selenium import webdriver
from features import environment
import time
from behave import *
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from functions.functionAuxiliar import (
    capture_screenshot
)

@given('Que estoy en la página de login')
def step_impl(context):
    try:
        for browser_name, driver in context.driver.items():
            driver.get("https://www.saucedemo.com/")
            botones = driver.find_elements(By.ID,"login-button")
            if botones:
                print("El boton de login existe")
            else:
                raise AssertionError("El botón no existe en la página.")
            capture_screenshot(context, f'Login_{browser_name}')
        time.sleep(2)
    except AssertionError as ae:
        raise ae  
    except Exception as e:
        print("Error:", e)

@when('Ingreso mis credenciales válidas "{username}" "{pwd}"')
def step_impl(context, username, pwd):
    try:
        for browser_name, driver in context.driver.items():
            element = WebDriverWait(driver, 10).until(
                EC.presence_of_element_located((By.ID, "user-name"))
            )
            element.send_keys(username)

            element = WebDriverWait(driver, 10).until(
                EC.presence_of_element_located((By.ID, "password"))
            )
            element.send_keys(pwd)
            capture_screenshot(context, f'Ingreso_de_credenciales_{browser_name}')
    except Exception as e:
        print("Error:", e)

@when('Hago click en el botón de inicio de sesión')
def step_impl(context):
    try:
        for browser_name, driver in context.driver.items():
            element = WebDriverWait(driver, 10).until(
                EC.element_to_be_clickable((By.ID, "login-button"))
            )
            element.click()
    except Exception as e:
        print("Error:", e)

@then('Se muestra la página principal')
def step_impl(context):
    try:
        for browser_name, driver in context.driver.items():
            capture_screenshot(context, f'Menu_{browser_name}')
            if driver.title!="Swag Labs":
                raise AssertionError("El titulo de la pagina no es el esperado")
            if driver.current_url != "https://www.saucedemo.com/inventory.html":
                raise AssertionError("La URL actual no coincide con la esperada.")
            print('Captura realizada')
            time.sleep(2)
            driver.close()
    except AssertionError as ae:
        raise ae  
    except Exception as e:
        print("Error:", e)