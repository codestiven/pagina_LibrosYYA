import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time

# verificacion sin entra
def test_prueba01(driver):
    driver.get("https://librosyya.000webhostapp.com")
    driver.maximize_window()
    print("entrada con exito")
    
    
       # Capturar una captura de pantalla
    screenshot_path = "prueba01.png"
    driver.save_screenshot(screenshot_path)

# verificacion de funcionalidad de carrusel principal
def test_prueba02(driver):
    driver.get("https://librosyya.000webhostapp.com")
    elevador = 0
    while elevador < 5:
        boton_siguiente = driver.find_element(By.CLASS_NAME, "carousel-control-next")
        boton_siguiente.click()
        time.sleep(1)
        print("movimiento correcto")
        elevador = elevador + 1
    elevador = 0
    while elevador < 5:
        boton_siguiente = driver.find_element(By.CLASS_NAME, "carousel-control-prev")
        boton_siguiente.click()
        time.sleep(1)
        print("movimiento correcto")
        elevador = elevador + 1
        
    
       # Capturar una captura de pantalla
    screenshot_path = "prueba02.png"
    driver.save_screenshot(screenshot_path)

# verificacion de el carrusel de productos
def test_prueba03(driver):
    driver.get("https://librosyya.000webhostapp.com")
    
    elevador = 0
    while elevador < 5:
        boton_siguiente = driver.find_element(By.CLASS_NAME, "selectores")
        boton_siguiente.click()
        time.sleep(1)
        print("funciono")
        elevador = elevador + 1
        
        
        
       # Capturar una captura de pantalla
    screenshot_path = "prueba03.png"
    driver.save_screenshot(screenshot_path)

#entrada a funciones de botones
def test_prueba04(driver):
    driver.get("https://librosyya.000webhostapp.com")
    driver.maximize_window()
    
    driver.execute_script("window.scrollBy(0, 1200);")
    # Encontrar el elemento usando XPath
    element_xpath = "/html/body/div[3]/ul/li[2]"
    elemento = driver.find_element(By.XPATH, element_xpath)
    elemento.click()
    time.sleep(1)
    
    element_xpath = "/html/body/div[3]/ul/li[3]"
    elemento = driver.find_element(By.XPATH, element_xpath)
    elemento.click()
    time.sleep(1)

    element_xpath = "/html/body/div[3]/ul/li[2]"
    elemento = driver.find_element(By.XPATH, element_xpath)
    elemento.click()
    time.sleep(1)
    
    element_xpath = "/html/body/div[3]/ul/li[1]"
    elemento = driver.find_element(By.XPATH, element_xpath)
    elemento.click()
    time.sleep(1)
    
       # Capturar una captura de pantalla
    screenshot_path = "prueba04.png"
    driver.save_screenshot(screenshot_path)
    
#verificacion de carrusel segundario
def test_prueba05(driver):
    driver.get("https://librosyya.000webhostapp.com") 
    elevador = 0
    while elevador < 5:
        boton_siguiente = driver.find_element(By.CLASS_NAME, "carousel-control-next")
        time.sleep(1)
        boton_siguiente.click()
        time.sleep(1)
        print("movimiento correcto")
        elevador = elevador + 1
    elevador = 0
    while elevador < 5:
        boton_siguiente = driver.find_element(By.CLASS_NAME, "carousel-control-prev")
        time.sleep(1)
        boton_siguiente.click()
        time.sleep(1)
        print("movimiento correcto")
        elevador = elevador + 1
    
       # Capturar una captura de pantalla
    screenshot_path = "prueba05.png"
    driver.save_screenshot(screenshot_path)

    
    
#cambio de pagina a productos
def test_prueba06(driver):
    driver.get("https://librosyya.000webhostapp.com")  # Necesitas navegar aquí de nuevo ya que cada prueba comienza con una instancia fresca del controlador

    # web_element = driver.find_element(By.NAME, "nombre")
    # web_element.send_keys("cositas", Keys.ENTER)

    time.sleep(1)
    print("entrada exitosa")
    
       # Capturar una captura de pantalla
    screenshot_path = "prueba06.png"
    driver.save_screenshot(screenshot_path)


# verificacion de carga total
def test_prueba07(driver):
    driver.get("https://librosyya.000webhostapp.com/plantillas/productos/productos.php")
    driver.maximize_window()
    
    # Hacer scroll hacia abajo de manera más lenta
    movimiento_arriba = 5000
    scroll_increment = 200  # Puedes ajustar este valor según tus necesidades
    while movimiento_arriba > 0:
        driver.execute_script("window.scrollBy(0, {});".format(scroll_increment))
        time.sleep(0.5)  # Aumenta el tiempo de espera para hacer el scroll más lento
        movimiento_arriba -= scroll_increment
    
    print("entrada con éxito")
    
       # Capturar una captura de pantalla
    screenshot_path = "prueba07.png"
    driver.save_screenshot(screenshot_path)
    time.sleep(5)
#cambio de pagina a autores
def test_prueba08(driver):
    driver.get("https://librosyya.000webhostapp.com/ver_autores.php")  # Necesitas navegar aquí de nuevo ya que cada prueba comienza con una instancia fresca del controlador


    time.sleep(1)
    
    
#entrada a autores
def test_prueba09(driver):
    driver.get("https://librosyya.000webhostapp.com/ver_autores.php") 
    print("entro correctamente")
    
    
       # Capturar una captura de pantalla
    screenshot_path = "prueba09.png"
    driver.save_screenshot(screenshot_path)

#verificacion de carga total
def test_prueba10(driver):
    driver.get("https://librosyya.000webhostapp.com/ver_autores.php")
    driver.maximize_window()
    
    movimiento_arriba = 5000
    scroll_increment = 200 
    while movimiento_arriba > 0:
        driver.execute_script("window.scrollBy(0, {});".format(scroll_increment))
        time.sleep(0.5)
        movimiento_arriba -= scroll_increment
    
    print("entrada con éxito")
    time.sleep(5)
    
       # Capturar una captura de pantalla
    screenshot_path = "prueba010.png"
    driver.save_screenshot(screenshot_path)


#ingreso de datos en el reporte
def test_prueba011(driver):
    driver.get("https://librosyya.000webhostapp.com/contacto.html")
    driver.maximize_window()
    time.sleep(1.5)


    web_element = driver.find_element(By.NAME , "nombre")
    web_element.send_keys("Stiven")
    time.sleep(1.5)
    

    web_element = driver.find_element(By.NAME , "correo")
    web_element.send_keys("codestiven@gmail.com")
    time.sleep(1.5)
    
    
    web_element = driver.find_element(By.NAME , "asunto")
    web_element.send_keys("Lorem Ipsum")
    time.sleep(1.5)
    
    
    web_element = driver.find_element(By.NAME , "comentario")
    web_element.send_keys("Lorem Ipsum is simply dummy text of the printing and typesetting industry. Lorem Ipsum has been the industry's standard dummy text ever since the 1500s, when an unknown printer took a galley of type and scrambled it to make a type specimen book. It has survived not only five centuries, but also the leap into electronic typesetting, remaining essentially unchanged. It was popularised in the 1960s with the release of Letraset sheets containing Lorem Ipsum passages, and more recently with desktop publishing software like Aldus PageMaker including versions of Lorem Ipsum.",Keys.ENTER)

    
    
    
    

    driver.execute_script("window.scrollBy(0, 1000);")
    
       # Capturar una captura de pantalla
    screenshot_path = "prueba011.png"
    driver.save_screenshot(screenshot_path)
