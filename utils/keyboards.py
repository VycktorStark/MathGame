from imports import *
keyboard_main = InlineKeyboardMarkup(inline_keyboard=[
[dict(text='👥 Add em grupos', url='https://t.me/{}?startgroup=iniciar'.format(bot['username'])),
dict(text='👁‍🗨 Canal Oficial', url='https://t.me/ProjectsStark')],
[InlineKeyboardButton(text='⚙ Comandos', callback_data='ajuda')]
])
keyboard_plugins = InlineKeyboardMarkup(inline_keyboard=[[
##InlineKeyboardButton(text='🗜 Ferramentas', callback_data='Ferramentas'),
InlineKeyboardButton(text='🎮 Jogo', callback_data='game')
],[InlineKeyboardButton(text='◀️ Voltar', callback_data='main')]])

keyboard_jogo = InlineKeyboardMarkup(inline_keyboard=[[
InlineKeyboardButton(text='💻 View Code', url='https://github.com/nickoala/telepot/blob/master/examples/callback/quiz.py'),
InlineKeyboardButton(text='🎮 Jogar', callback_data='Jogar')
],[InlineKeyboardButton(text='◀️ Voltar', callback_data='ajuda')]])