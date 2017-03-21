#-*- coding: utf-8 -*-
from imports import *
class lang:
    ptdesc = "📖 <b>Ajuda para o comando:</b> <code>{}</code>\n{desc}"
    ptdescSenha = '''
Para que seja gerada uma sugestão de senha
<b>____________</b>
Exemplo:
<code>/senha 8</code> - gerar senha com 8 digitos
<code>/senha 16</code> - gerar senha com 16 digitos
'''
    ptdescDados = "Para girar o dado aleatoricamente e informar um resultado."
    ptdescID = "Para o bot retorna algumas informações sobre você."
    maintenance = '{} agora está em manutenção...'
    maintenance_not_sudo = '{} está em manutenção no momento.'
    not_maintenance = "{} saiu da manutenção e já está pronto para uso."
    not_sudo = "Ei, você não manda em mim!"
    not_privado = "Enviar uma mensagem no chat privado."
    ptdescNSFW = "<code>/boobs</code> - imagens aleatórias dos seios.\n<code>/butts</code> - imagens aleatórias de bundas."
    def __init__(self, get):
        self.get = get
    def pt_br(self):
        if self.get.lower() ==  "status":
            return '''
📊 Estatísticas do Game:

🏆 | Ganhou: %d
🙁 | Perdeu: %d
🕹 | Partidas: %d
_______________
@ProjectsStark
'''
        elif self.get.lower() ==  "start":
            return '''Olá, <b>{}</b>!
Eu sou o {} simples de multiplas funções.

 <b>O que posso fazer para você?</b>
            
- Eu tenho um monte de ferramentas úteis! que você pode conhecer visualizando meus comandos ao clicar no botão abaixo.'''
        elif self.get.lower() ==  "main":
            return '''Este é o menu principal!
Você sabia que meu desenvolvedor possui um canal e, se você não participar, convido você a participar clicando no botão abaixo:'''
        elif self.get.lower() ==  "game":
            return '''
<b>Jogo de cálculo matemático:</b>

Este é um jogo educacional - Onde você pratica suas habilidades de matemática e ainda se diverte no jogo, você pode ver suas estatísticas e mostrá-las aos seus amigos. Clique em jogar e começar agora!


Este joguinho foi criado pelo Nickoala, você poder visualizar clicando no botão de <code>View</code>'''
    def cmd_br(self):
        if self.get.lower() ==  "id_user":
            return '''
Nome: <b>{}</b>
Usuário: {}
ID: <code>{}</code>'''
        elif self.get.lower() ==  "init":
            return '''<b>{} iniciado!\n______________\n</b>🤖 | <b>Username:</b> {}\n🖥 | <b>ID:</b> <code>{}</code>\n<b>______________\n📆 Data de conexão:</b> <code>{}</code>\n⌚️ <b>Hora da conexão:</b> <code>{}</code>'''
        elif self.get.lower() ==  "dados":
            return '''O Dado parou no número: 🎲 <code>{}</code>'''
        elif self.get.lower() ==  "senha":
            return '''Senha gerada: \n{}'''
        elif self.get.lower() ==  "ajuda":
            return '''
📖 <b>Lista de Comandos:</b>
<code>1</code> - dado
<code>2</code> - id
<code>3</code> - senha
<code>4</code> - NSFW
<b>________________</b>
ℹ️ Envie <code>/ajuda [</code><b>nome</b><code>/</code><b>número</b><code>]</code> para saber como utilizar tal comando, ou clique sobre o atalho destacado.'''
    def info(self):
        if self.get.lower() == 'version':
            return str('3.0')
        elif self.get.lower() == 'create':
            return 'Vycktor Stark'