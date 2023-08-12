import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time
from test import *














# Este fixture configurará y cerrará una instancia de Selenium WebDriver
@pytest.fixture(scope="module")
def driver():  # Renombramos la función del fixture para evitar confusiones con la variable a nivel de módulo
    # Inicializamos el Selenium WebDriver (es posible que necesites ajustar la ruta del controlador)
    driver = webdriver.Chrome()  # Reemplaza 'ruta_al_controlador_de_chrome' con la ruta real
    yield driver
    # No cerramos el WebDriver aquí para mantenerlo abierto entre pruebas

# Ejecutamos las pruebas y generamos un informe HTML
if __name__ == '__main__':
    # Usa el siguiente comando para ejecutar las pruebas y generar un informe HTML:
    # pytest -v --html=report.html <nombre_de_archivo>.py
    pytest.main(['-v', '--html=report.html', __file__])
