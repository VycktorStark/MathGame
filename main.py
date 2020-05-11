#!/usr/bin/env python3
import random, os, json, tools as cfg
from telepot.namedtuple import InlineKeyboardMarkup, InlineKeyboardButton, KeyboardButton
from telepot.delegate import (per_chat_id, per_callback_query_origin, create_open, pave_event_space)

class message_(cfg.TLP.helper.ChatHandler):
    def __init__(self, *args, **kwargs):
        super(message_, self).__init__(*args, **kwargs)
        self.lang = False
    def on_chat_message(self, msg):
        try:
            self.lang = cfg.LN.LANG[msg['from']['language_code'][:2]]
        except Exception:
            self.lang = cfg.LN.LANG['en']
        if ('text' in msg) and ('/start' in msg['text'].split()):
                self.sender.sendMessage(self.lang['startinggame'], "HTML", reply_markup=cfg.KeyboardJogo(InlineKeyboardMarkup, InlineKeyboardButton,
                                                                                                         buttonviewcodeorg=self.lang['buttonviewcodeorg'],
                                                                                                         buttongamestarting=self.lang['buttongamestarting'],
                                                                                                         buttonviewcode=self.lang['buttonviewcode']))

class Callback(cfg.TLP.helper.CallbackQueryOriginHandler):
    def __init__(self, *args, **kwargs):
            super(Callback, self).__init__(*args, **kwargs)
            self._score = {True: 0, False: 0}
            self._answer, self.lang, self.query_id, self.from_id, self.query_data = None, False, False, False, False
    def on_callback_query(self, msg):
        try:
            self.lang = cfg.LN.LANG[msg['from']['language_code'][:2]]
        except Exception:
            self.lang = cfg.LN.LANG['en']
        self.query_id, self.from_id, self.query_data = cfg.TLP.glance(msg, flavor='callback_query')
        if self.query_data == 'status':
            output = self.lang[self.query_data].format(self._score[True], (self._score[False]),(self._score[True]+self._score[False]))
            cfg.API.answerCallbackQuery(self.query_id, text=output, show_alert=True)
        elif self.query_data == 'startinggame':
            self.editor.editMessageText(self.lang[self.query_data], "HTML", reply_markup=cfg.KeyboardJogo(InlineKeyboardMarkup, InlineKeyboardButton,
                                                                                                     buttonviewcodeorg=self.lang['buttonviewcodeorg'],
                                                                                                     buttongamestarting=self.lang['buttongamestarting'],
                                                                                                     buttonviewcode=self.lang['buttonviewcode']))
        else:
            if self.query_data == 'Jogar':
               self._answer = self.gameMat()
            else:
                result = (self._answer == int(self.query_data))
                self._score[result] += 1
                self._answer = self.gameMat()
                cfg.API.answerCallbackQuery(self.query_id, text=self.lang['gameresult'][0][result])


    def on__idle(self, event):
        self.editor.editMessageText(self.lang['stopinggame'].format(self._score[True], (self._score[False]),(self._score[True]+self._score[False])))
    def gameMat(self):
        try:
            x, y = random.randint(1,50), random.randint(1,30)
            sign, op = random.choice([('+', lambda a,b: a+b),('-', lambda a,b: a-b),('x', lambda a,b: a*b)])
            answer = op(x,y)
            choices = sorted(list(map(random.randint, [answer-6]*3, [answer]*2)) + [answer])
            self.editor.editMessageText(cfg.answerite(self.lang, x, y, sign), reply_markup=InlineKeyboardMarkup(inline_keyboard=[
                                            list(map(lambda cpy: InlineKeyboardButton(text=str(cpy), callback_data=str(cpy)), choices)),[
                                            InlineKeyboardButton(text=self.lang['buttonstatistics'], callback_data='status'),
                                            InlineKeyboardButton(text=self.lang['buttonback'], callback_data='startinggame')]]))
            return answer
        except Exception:
            cfg.API.answerCallbackQuery(self.query_id, text=self.lang['buttonss'], show_alert=True)

if __name__ == '__main__':
    tp = 3600
    while True:
        cfg.TLP.DelegatorBot(os.environ['TOKEN'], [pave_event_space()(per_chat_id(), create_open, message_, timeout=tp*3600),pave_event_space()(per_callback_query_origin(), create_open, Callback, timeout=60)]).message_loop(run_forever=cfg.LN.__starting__)
