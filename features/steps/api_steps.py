from behave import given, when, then

@given('que a API está funcional')
def step_check_api_status(context):
    response = context.session.get(f"{context.api_base_url}/health-check")
    assert response.status_code == 200

@when('eu envio uma requisição POST para criar um produto')
def step_post_product(context):
    product_data = {
        "name": "Produto Teste",
        "description": "Descrição Teste",
        "price": 100.00
    }
    context.response = context.session.post(f"{context.api_base_url}/products", json=product_data)

@then('o produto deve ser criado com sucesso')
def step_check_product_creation(context):
    assert context.response.status_code == 201
