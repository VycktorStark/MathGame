#!/usr/bin/env python3
from imports import *
ru = lambda text: text

class Server:
    def about(self, title = ''):
        self.info = []
        self.info.append('''\033[02;34m
     ____       _             ____  _     
    |  _ \ ___ | |__   ___   |  _ \| |__  
    | |_) / _ \| '_ \ / _ \  | | | | '_ \ 
    |  _ < (_) | |_) | (_) | | |_| | |_) |  \033[01;0mBy: \033[01;36m{}\033[02;34m
    |_| \_\___/|_.__/ \___/  |____/|_.__/   \033[01;0mVersão: \033[02;36m{}'''.format(lang('create').info(),lang('version').info()))
        self.info.append("\n\033[0;0m______________")
        self.info.append('\n\033[0;36mNome: \033[01;0m{}'.format(bot_name))
        self.info.append('\n\033[0;36mUsername: \033[01;0m{}'.format(bot_username))
        self.info.append('\n\033[0;36mID: \033[01;0m{}'.format(bot_id))
        return ru("".join(self.info))

if __name__ == '__main__':
    ##api.sendMessage(Chatsuporte, lang('init').pt_br().format(bot_name, bot_username, bot_id, data, hora), "HTML")
    telepot.DelegatorBot(TOKEN, [
        pave_event_space()(
            per_chat_id(), create_open, main, timeout=3600 * 3600),
        pave_event_space()(
            per_callback_query_origin(), create_open, Callback, timeout=3600 * 3600),
    ]).message_loop(run_forever=Server().about())
while 1:
    time.sleep(10)