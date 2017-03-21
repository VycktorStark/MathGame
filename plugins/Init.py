from imports import *
class help:
    def __init__(self, sender, base, texto, input_texto, nome_user, msg_id):
        self.sender = sender
        self.base = base
        self.texto = texto
        self.input_texto = input_texto
        self.nome_user = nome_user
        self.msg_id= msg_id
    def cmd(self):
        if self.texto.startswith('/start'):
            self.sender.sendMessage(lang('start').pt_br().format(self.nome_user, bot_name), "HTML", reply_markup=keyboard_main)
        if self.texto.startswith('/ajuda') or self.texto.startswith('/help'):
                if self.input_texto.lower() == "dado" or self.input_texto.lower() == "1" :
                       self.sender.sendMessage(lang.ptdesc.format("/dados",desc=lang.ptdescDados), 'HTML', reply_to_message_id=self.msg_id)
                elif self.input_texto.lower() == 'id' or self.input_texto.lower() == "2":
                    self.sender.sendMessage(lang.ptdesc.format("/id",desc=lang.ptdescID), 'HTML', reply_to_message_id=self.msg_id)
                elif self.input_texto.lower() == 'senha' or self.input_texto.lower() == "3":
                    self.sender.sendMessage(lang.ptdesc.format("/senha",desc=lang.ptdescSenha), 'HTML', reply_to_message_id=self.msg_id)
                elif self.input_texto.lower() == 'NSFW' or self.input_texto.lower() == "4":
                    self.sender.sendMessage(lang.ptdesc.format("/fap e /boobs e /buuts",desc=lang.ptdescNSFW), 'HTML', reply_to_message_id=self.msg_id)
                else:
                    self.sender.sendMessage(lang('ajuda').cmd_br(), 'HTML', reply_to_message_id=self.msg_id)
        