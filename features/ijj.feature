# language: pt
Funcionalidade: Enviar mensagem na página de contato
  Como um usuário
  Quero acessar a página de contato
  Para enviar uma mensagem

  Cenário: Enviar mensagem com sucesso
    Dado que estou na página de contato do Instituto Joga Junto
    Quando preencho o formulário com "Dione Braga", "dionebraga.work@gmail.com", "Ser facilitador" e "Teste - Oi!"
    E clico no botão de enviar
    Então vejo a mensagem "Mensagem enviada com sucesso" e fecho o navegador
