Feature: Adicionar Produto
  Como usuário
  Quero adicionar um produto
  Para gerenciar o inventário

  Scenario: Adicionar um novo produto
    Given que estou na página de adicionar produto
    When eu insiro os detalhes do produto
    And clico no botão de adicionar produto
    Then vejo uma mensagem de sucesso "Produto adicionado com sucesso"
