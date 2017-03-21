# -*- coding:utf-8 -*-
from imports import *
from utils.requests import *
import json, re
def uptime(self):
    uptime = datetime.datetime.now().strftime(self)
    return uptime
def gameMat(self):
    x = random.randint(1,50)
    y = random.randint(1,50)
    sign, op = random.choice([('+', lambda a,b: a+b),
                              ('-', lambda a,b: a-b),
                              ('x', lambda a,b: a*b)])
    answer = op(x,y)
    question = '%d %s %d = ?' % (x, sign, y)
    choices = sorted(list(map(random.randint, [-96]*3, [250]*2)) + [answer])
    keyboard = InlineKeyboardMarkup(inline_keyboard=[
    list(map(lambda c: InlineKeyboardButton(text=str(c), callback_data=str(c)), choices)),
    [InlineKeyboardButton(text='📊 Estatísticas', callback_data='status'),
    InlineKeyboardButton(text='◀️ Voltar', callback_data='game')]])
    self.editor.editMessageText(question,reply_markup=keyboard)
    return answer
            
def gsub(get, self, output):
    clean = re.compile(get) ## REMOVING ERROR UTF8
    output = re.sub(clean, self, output)
    return output
           
def NSFW(self):
    if self == "fap":
        self = random.choice(['boobs','butts'])
    url_api = 'http://api.o{}.ru/noise/1'.format(self)
    params = {}
    res_obj, res_str = request_json(url=url_api, params=params)
    url = res_str[0]["preview"]
    return 'http://media.o{}.ru/{}'.format(self, url)
           
def URL_JSON(self):
    url_api = self
    params = {}
    res_obj, res_str = request_json(url=url_api, params=params)
    return res_obj, res_str
           
def SendType(self, text):
  global texto
  if 'photo' in self: texto = "{}a foto."
  elif 'sticker' in self: texto = "{} Sticker."
  elif 'voice' in self: texto = "{} voz."
  elif 'audio' in self: texto = "{} Áudio."
  elif 'video' in self: texto = "{} Vídeo."
  elif 'document' in self and self['document']['mime_type']:
      document = self['document']['mime_type']
      if document == "video/mp4":
          texto = "{} Gif."
      elif document == "application/x-bittorrent":
          texto = "{} Arquivo em pdf."     
      elif document == "application/vnd.android.package-archive":
          texto = "{} Aplicativo."     
      elif document == "application/x-rar":
          texto = "{} Arquivo em RAR."     
      elif document == "application/x-zip":
          texto = "{} Arquivo em Zip."     
      elif document == "text/x-python":
          texto = "{} Script em python."     
      elif document == "text/plain":
          texto = "{} Script de texto simples."     
      elif document == "application/x-shellscript":
          texto = "{} Script em shell."     
      elif document == "text/x-lua":
          texto = "{} Script em lua."     
      elif document == "text/html":
          texto = "{} Script em HTML."     
      elif document == "application/json":
          texto = "{} Script em JSON."     
      elif document == "application/javascript":
          texto = "{} Script em JavaScript."     
      elif document == "application/octet-stream":
          texto = "{} Script em octet-stream."     
      elif document == "text/markdown":
          texto = "{} Script em Markdown."     
      elif document == "application/x-yaml":
          texto = "{} Script em yaml."
      else: texto = "Documento"
  else: texto = "ERROR"
  return texto.format(text)

def conversor(self):
    if self < 1000:
        return '%i' % self + 'B'
    elif 1000 <= self < 1000000:
        return '%.2f' % float(self/1000) + 'KB'
    elif 1000000 <= self < 1000000000:
        return '%.2f' % float(self/1000000) + 'MB'
    elif 1000000000 <= self < 1000000000000:
        return '%.2f' % float(self/1000000000) + 'GB'
    elif 1000000000000 <= self:
        return '%.2f' % float(self/1000000000000) + 'TB'
           
def Viewer(self, msg):
    hora = uptime("%H:%M:%S")
    data = uptime("%d/%m/%Y")
    texto = "\033[0;0m[\033[0;31m{}\033[0;0m] Notificação de um".format(hora)
    if self == "Callback":
        info_user = "\n\033[02;36mUsuário: \033[0;0m{} (ID: \033[02;34m{}\033[0;0m)\n"\
        .format(msg['message']['from']['first_name'], str(msg['message']['from']['id']))
        if msg['message']['chat']['type']:
            if msg['message']['chat']['type'] == "private":  texto = "{} chat privado {}".format(texto, info_user)
            else: texto = "{} super grupo\n\033[02;36mGrupo:\033[0;0m {} (ID: \033[02;34m{}\033[0;0m){}"\
                .format(texto, msg['message']['chat']['title'], str(msg['message']['chat']['id']), info_user)
            texto = "{}\033[01;34mBotão Selecionado: \033[0;31m{}\033[01;0m".format(texto,str(msg['data']))
            
    if self == "Bot":
        info_user = "\n\033[02;36mUsuário: \033[0;0m{} (ID: \033[02;34m{}\033[0;0m)\n"\
        .format(msg['from']['first_name'], str(msg['from']['id']))
        if msg['chat']['type']:
            if msg['chat']['type'] == "private": texto = "{} chat privado {}".format(texto, info_user)
            else: texto = "{} super grupo\n\033[02;36mGrupo:\033[0;0m {} (ID: \033[02;34m{}\033[0;0m){}"\
                .format(texto, msg['chat']['title'], str(msg['chat']['id']), info_user)
        if 'new_chat_member' in msg: texto = texto + "\033[01;34mAdicionou um novo membro do grupo."
        elif 'left_chat_member' in msg: texto = texto + "\033[01;34mRemoveu um membro do grupo."
        elif 'text' in msg:
            if 'entities' in msg:
                if msg['entities'][0]['type'] == "bot_command":
                    texto = '{}\033[01;34mExecutou um Comando: \033[0;31m{}\033[01;0m'.format(texto,msg['text'])
                elif msg['entities'][0]['type'] == "url": 
                    texto = '{}\033[01;34mEnviou um Link: \033[02;34m{}\033[01;0m'.format(texto,msg['text'])
            else:
                 texto = '{}\033[01;34mEnviou uma Mensagem: \033[0;0m{}'.format(texto,msg['text']\
                 .encode('utf8').decode('utf8'))
        else: texto = "{}{}\033[0;0m".format(texto, SendType(msg, '\033[02;32mEnviou um'))
    return texto