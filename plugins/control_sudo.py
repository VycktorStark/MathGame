from imports import *
class control_plugin:
    def __init__(self,sender, base, texto, nome_user, username_user, id_user, input_texto):
        self.sender = sender
        self.base = base
        self.texto = texto
        self.input_texto = input_texto
        self.nome_user = nome_user
        self.username_user = username_user
        self.id_user = id_user
    def control_plugin(self):
        if self.texto.startswith('/debug'):
            self.sender.sendMessage(self.base)