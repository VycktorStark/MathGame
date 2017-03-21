from imports import *
class simple:
    def __init__(self,sender, base, texto, nome_user, username_user, id_user, input_texto):
        self.sender = sender
        self.base = base
        self.texto = texto
        self.input_texto = input_texto
        self.nome_user = nome_user
        self.username_user = username_user
        self.id_user = id_user
    def simple(self):
        content_type, chat_type, chat_id, msg_date, msg_id = telepot.glance(self.base, long=True)
        if self.texto.startswith('/dados'):
            self.sender.sendMessage(lang('dados').cmd_br().format(random.randint(1,9)), "html")
        elif self.texto.startswith('/id'):
            self.sender.sendMessage(lang('id_user').cmd_br().format(self.nome_user, self.username_user, str(self.id_user)) , "HTML")
        elif self.texto.startswith('/fap') and chat_type == "private":
            self.sender.sendPhoto(NSFW('fap'))
        elif self.texto.startswith('/boobs') and chat_type == "private":
            self.sender.sendPhoto(NSFW('boobs'))
        elif self.texto.startswith('/butts') and chat_type == "private":
            self.sender.sendPhoto(NSFW('butts'))
        elif self.texto.startswith('/senha'):
            if self.input_texto != "16":
                self.sender.sendMessage(lang('senha').cmd_br().format(random.randint(00000000,99999999)))
            if self.input_texto == "16":
                self.sender.sendMessage(lang('senha').cmd_br().format(random.randint(0000000000000000,9999999999999999)))
        return