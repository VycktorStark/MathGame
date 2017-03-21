import json
from imports import *
class main(telepot.helper.ChatHandler):
    def __init__(self, *args, **kwargs):
        super(main, self).__init__(*args, **kwargs)
    def on_chat_message(self, msg):
        global maintenance
        nome_user = msg['from']['first_name']
        content_type, chat_type, chat_id, msg_date, msg_id = telepot.glance(msg, long=True)
        print(Viewer('Bot', msg))
        if content_type == 'text':
            username_user = '{} não tem username'.format(nome_user)
            if 'last_name' in msg['from']: nome_user = "{} {}".format(nome_user, msg['from']['last_name'])
            if 'username' in msg['from']: username_user = "@{}".format(msg['from']['username'])
            id_user = msg['from']['id']
            chat_id = msg['chat']['id']
            texto = msg['text']
            msg_id = msg['message_id']
            input_texto = " ".join(texto.split()[1:])
            if texto.startswith('/remanut'):
                if id_user != sudo:
                    self.sender.sendMessage(lang.not_sudo)
                else:
                    maintenance = True
                    self.sender.sendMessage(lang.not_maintenance.format(bot_name))
            elif texto.startswith('/manut'):
                if id_user != sudo:
                    self.sender.sendMessage(lang.not_sudo)
                else:
                     maintenance = False
                     self.sender.sendMessage(lang.maintenance.format(bot_name))
            elif id_user == sudo or maintenance == True:
                simple(self.sender, msg, texto, nome_user, username_user, id_user, input_texto).simple()
                if id_user == sudo:
                    control_plugin(self.sender, msg, texto, nome_user, username_user, id_user, input_texto).control_plugin()
                if id_user == sudo and 'reply_to_message' in msg:
                    midia(self.sender, msg['reply_to_message'], texto).type()
                if 'private' in chat_type:
                    help(self.sender, msg, texto, input_texto, nome_user, msg_id).cmd()
            else:
                self.sender.sendMessage(lang.maintenance_not_sudo.format(bot_name))
            