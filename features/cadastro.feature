Feature: Cadastro de Produtos
  Como usuário
  Quero adicionar novos produtos
  Para gerenciar o inventário

  Scenario: Adicionar um novo produto com sucesso
    Given que estou na página de cadastro de produtos
    When eu insiro os detalhes do produto
      | Nome         | Descrição              | Preço  |
      | Produto Teste | Produto de Teste       | 100.00 |
    And clico no botão "Salvar"
    Then vejo uma mensagem "Produto cadastrado com sucesso"

  Scenario: Tentar cadastrar um produto com informações inválidas
    Given que estou na página de cadastro de produtos
    When eu insiro os detalhes do produto
      | Nome         | Descrição | Preço |
      |              |           | 0.00  |
    And clico no botão "Salvar"
    Then vejo uma mensagem de erro "Preencha todos os campos obrigatórios"
