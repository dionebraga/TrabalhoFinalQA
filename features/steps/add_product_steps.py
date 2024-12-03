from behave import given, when, then
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

@given('que estou na página de adicionar produto')
def step_open_add_product_page(context):
    context.driver.get(f"{context.base_url}/products/add")

@when('eu insiro os detalhes do produto')
def step_insert_product_details(context):
    WebDriverWait(context.driver, 10).until(
        EC.presence_of_element_located((By.NAME, "name"))
    ).send_keys("Produto Teste")

    context.driver.find_element(By.NAME, "description").send_keys("Descrição Teste")
    context.driver.find_element(By.NAME, "price").send_keys("100.00")

@when('clico no botão de adicionar produto')
def step_click_add_product_button(context):
    context.driver.find_element(By.XPATH, "//button[text()='Adicionar']").click()

@then('vejo uma mensagem de sucesso "Produto adicionado com sucesso"')
def step_check_success_message(context):
    success_message = WebDriverWait(context.driver, 10).until(
        EC.presence_of_element_located((By.CLASS_NAME, "success-message"))
    )
    assert "Produto adicionado com sucesso" in success_message.text
