from imports import *
class Callback(telepot.helper.CallbackQueryOriginHandler):
    def __init__(self, *args, **kwargs):
            super(Callback, self).__init__(*args, **kwargs)
            self._score = {True: 0, False: 0}
            self._answer = None
    def on_callback_query(self, msg):
        query_id, from_id, query_data = telepot.glance(msg, flavor='callback_query')
        print(Viewer('Callback', msg))
        if query_data == 'status':
            output = lang(query_data).pt_br() % (self._score[True], (self._score[False]),(self._score[True]+self._score[False]))
            api.answerCallbackQuery(query_id, text=output, show_alert=True)
        elif query_data == 'ajuda':
            self.editor.editMessageText(lang(query_data).cmd_br(), "HTML", reply_markup=keyboard_plugins)
        elif query_data == 'main':
            self.editor.editMessageText(lang(query_data).pt_br(), "HTML", reply_markup=keyboard_main)
        elif query_data == 'game':
            self.editor.editMessageText(lang(query_data).pt_br(), "HTML", reply_markup=keyboard_jogo)
        else:
            if query_data == 'Jogar':
               self._answer = gameMat(self)
            else:
                self._score[self._answer == int(query_data)] += 1
                self._answer = gameMat(self)  
#def on__idle(self, event):
     #self.editor.editMessageText('Jogo encerrado')
                