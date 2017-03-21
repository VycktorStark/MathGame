from imports import *
class midia:
    def __init__(self,sender, base, texto):
        self.sender = sender
        self.base = base
        self.texto = texto
    def type(self):
        if self.texto.startswith('/info'):
            typo = SendType(self.base, '')
            if 'document' in self.base:
                document = self.base['document']
                nome = document['file_name'] 
                tamanho = conversor(document['file_size'] )
                texto = "\
                \nℹ️ | <b>Isto é um {}</b>\
                \n📁 | <b>Nome:</b> <code>{}</code>\
                \n⚖ | <b>Tamanho:</b> <code>{}</code>".format(typo,nome,tamanho)
                self.sender.sendMessage(texto, "HTML")
            
            elif 'photo' in self.base:
                photo = self.base['photo']
                if photo[3]: photo = photo[3]
                else: photo[1]
                tamanho = conversor(photo['file_size'] )
                dimensao = "{}x{}".format(photo['height'],photo['width'])
                texto = "\
                \nℹ️ | <b>Isto é um{}</b>\
                \n⚖ | <b>Tamanho:</b> <code>{}</code>\
                \n🔎 | <b>Dimensões:</b> <code>{}</code>".format(typo,tamanho, dimensao)
                if 'caption' in self.base: texto = "{}\n💬 | <b>Legenda:</b> {}".format(texto,self.base['caption'])
                self.sender.sendMessage(texto, "HTML")
            elif 'audio' in self.base:
                audio = self.base['audio']
                nome = audio['title']
                duration = "{:.2f}".format(audio['duration'] / 60) 
                tamanho = conversor(audio['file_size'])
                '''"\n👤 | Artista"'''
                texto = "\
                \nℹ️ | <b>Isto é um arquivo de {}</b>\
                \n🎶 | <b>Nome:</b> <code>{}</code>\
                \n⚖ | <b>Tamanho:</b> <code>{}</code>\
                \n🔎 | <b>Duração:</b> <code>{}</code>".format(typo,nome, tamanho, duration)
                if 'performer' in audio: texto = "{}\n👤 | <b>Artista:</b> {}".format(texto,audio['performer'])
                self.sender.sendMessage(texto, "HTML")
            else:
                 self.sender.sendMessage(typo, "HTML")