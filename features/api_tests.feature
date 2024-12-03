Feature: Testar API do sistema de produtos
  Como desenvolvedor
  Quero testar a API do sistema
  Para garantir que está funcionando corretamente

  Scenario: Criar produto via API
    Given que a API está funcional
    When eu envio uma requisição POST para criar um produto
    Then o produto deve ser criado com sucesso
