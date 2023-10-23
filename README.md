# Teste de bot para telegram via Python Script
Script com foco de testar um bot para automações de mensagens pelo Telegram.

O Script em questão tem a função de fornecer a mensagem que o BOT irá enviar. Para que isto seja possível inicialmente você precisará criar um bot no Telegram e obter o token de acesso. 
Siga as etapas abaixo:

1 - Abra o aplicativo Telegram e procure o BotFather.<br />
2 - Inicie uma conversa com o BotFather e use o comando /newbot para criar um novo bot.<br />
3 - Siga as instruções do BotFather para escolher um nome de usuário e receber um token de acesso para o seu bot.

A Token de acesso ficará na seguinte seção do Script: <br />
#Configuração do token do seu bot<br />
TOKEN = "TOKEN_DO_BOT"

Após a criação, para realizar o teste você deverá ir no seu telegram pessoal e criar um grupo adicionando o Bot criado no grupo para realização de testes.

Já estando com o grupo criado você deverá identificar o ID do do Chat do grupo, a forma mais rápide de realizar esta ação é:<br />
Envie uma mensagem no grupo em que você cirou junto ao seu Bot depois encaminhe esta mensagem pesquisando no telegram pelo contato "Get My ID", este contato é um bot que informa o ID do chat de onde a mensagem se originou.

O ID do chat ficará na seguinte seção do Script:<br />
#ID do chat onde você deseja enviar a mensagem<br />
chat_id = "ID_DO_TELEGRAM"

Estando em posse da Token do Bot e do ID do chat você poderá testar o script sem dificuldades.

Obs.: Para o script funcionar normalmente você deverá ter a biblioteca python-telegram-bot instalada no seu Python.<br />
Comando para instalação: pip install python-telegram-bot
