import telegram
from token import api_key
# pip install python-telegram-bot

bot = telegram.Bot(token=api_key)

# 새로운 메시지 확인
# for i in bot.getUpdates():
#     print(i.message)

# 메시지 전송
bot.send_message(chat_id=1955432261, text='test telegram bot')

