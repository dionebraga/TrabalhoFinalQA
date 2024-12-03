from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from utils.config import BASE_URL

def test_automate_product():
    driver = webdriver.Chrome()
    driver.get(BASE_URL)

    product = {
        "name": "Produto Automação",
        "description": "Descrição do Produto Automação",
        "price": 50.0,
        "image_url": "http://example.com/image.jpg"
    }

    driver.find_element(By.NAME, "nome").send_keys(product["name"])
    driver.find_element(By.NAME, "descricao").send_keys(product["description"])
    driver.find_element(By.NAME, "preco").send_keys(str(product["price"]))
    driver.find_element(By.NAME, "imagem").send_keys(product["image_url"])
    driver.find_element(By.XPATH, "//button[contains(text(), 'Adicionar Produto')]").click()

    success_message = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.XPATH, "//div[contains(text(), 'Produto adicionado com sucesso')]"))
    )
    assert success_message is not None
    driver.quit()
