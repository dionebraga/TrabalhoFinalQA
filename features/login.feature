Feature: Login no Sistema
  Como colaborador
  Quero fazer login no sistema
  Para acessar as funcionalidades do backoffice

  Scenario: Login bem-sucedido
    Given que eu estou na página de login
    When eu insiro credenciais válidas
    Then eu devo ser redirecionado para o dashboard
