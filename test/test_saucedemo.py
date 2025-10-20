import pytest
from selenium.webdriver.common.by import By
import sys
import os

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__),'..')))
from utils.helpers import get_driver, login_saucedemo


@pytest.fixture
def driver():
    driver = get_driver()
    
    yield driver
    driver.quit()

def test_login(driver):
    login_saucedemo(driver)
    assert "/inventory.html" in driver.current_url
    driver.save_screenshot("login.png")
    titulo = driver.find_element(By.CSS_SELECTOR,"div.header_secondary_container .title").text
    assert titulo == "Products"

def test_catalogo(driver):
    login_saucedemo(driver)
    products  = driver.find_elements(By.CLASS_NAME, "inventory_item")
    assert len(products) == 6
    driver.save_screenshot("catalogo.png")

def test_carrito(driver):
    login_saucedemo(driver)
    products = driver.find_elements(By.CLASS_NAME, "inventory_item")
    total_products = len(products)
    if total_products >= 2:
        products[0].find_element(By.TAG_NAME, "button").click()
        products[1].find_element(By.TAG_NAME, "button").click()
        products[2].find_element(By.TAG_NAME, "button").click()
        products[3].find_element(By.TAG_NAME, "button").click()
        products[4].find_element(By.TAG_NAME, "button").click()
        products[5].find_element(By.TAG_NAME, "button").click()
        badge = driver.find_element(By.CLASS_NAME, "shopping_cart_badge").text

        assert badge == "6"
    driver.save_screenshot("carrito.png")