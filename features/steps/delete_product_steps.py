from behave import given, when, then
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

@given('que estou na página de lista de produtos')
def step_open_product_list(context):
    context.driver.get(f"{context.base_url}/products")

@when('eu seleciono um produto para deletar')
def step_select_product_to_delete(context):
    delete_button = WebDriverWait(context.driver, 10).until(
        EC.element_to_be_clickable((By.XPATH, "//button[text()='Deletar']"))
    )
    delete_button.click()

@then('vejo uma mensagem "Produto deletado com sucesso"')
def step_check_delete_success_message(context):
    success_message = WebDriverWait(context.driver, 10).until(
        EC.presence_of_element_located((By.CLASS_NAME, "success-message"))
    )
    assert "Produto deletado com sucesso" in success_message.text
