from imports import *
sudo = 186513800
maintenance = True
Chatsuporte = "-1001097459691"
TOKEN = ''
api = telepot.Bot(TOKEN)
bot = api.getMe()
bot_name = bot['first_name']
bot_username = '@{}'.format(bot['username'])
bot_id = str(bot['id'])
