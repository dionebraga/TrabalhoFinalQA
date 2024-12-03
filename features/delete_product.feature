Feature: Deletar Produto
  Como usuário
  Quero deletar um produto
  Para manter o inventário atualizado

  Scenario: Deletar um produto com sucesso
    Given que estou na página de lista de produtos
    When eu seleciono um produto para deletar
    Then vejo uma mensagem "Produto deletado com sucesso"
