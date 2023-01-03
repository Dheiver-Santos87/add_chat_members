import telegram
from telegram.error import TelegramError

# Configure o bot
bot = telegram.Bot(token='SEU_TOKEN_DE_BOT_AQUI')

# Obtenha a lista de membros do grupo de origem
membros = bot.get_chat_members(chat_id='@grupo_origem')

# Itere os membros e adicione-os ao novo grupo
for membro in membros:
  try:
    bot.add_chat_members(chat_id='@novo_grupo', user_id=membro.user.id)
  except TelegramError as e:
    print(f'Erro ao adicionar membro {membro.user.username}: {e}')
