import telepot, lang, random, os
LN, TLP, API = lang, telepot, telepot.Bot(os.environ['TOKEN'])
def KeyboardJogo(InlineKeyboardMarkup, InlineKeyboardButton, buttonviewcodeorg, buttongamestarting, buttonviewcode):
    return InlineKeyboardMarkup(inline_keyboard=[[InlineKeyboardButton(text=buttonviewcode, url=lang.__sourcecode__),
                                                  InlineKeyboardButton(text=buttongamestarting, callback_data='Jogar')
                                                  ],
                                                 [InlineKeyboardButton(text=buttonviewcodeorg, url=lang.__sourceoriginalcode__)]
                                                 ])
def answerite(tr, x, y, sign):
    _nam, _prod, _return = tr["name"], tr["product"], tr['answer'][0][sign]
    if ("{_produto}" in _return) and ("{_nome}" in _return):
        _produts = random.choice(_prod)
        if (int(x) > int(1)): _produts ="{}s".format(_produts)
        return _return.format(item0=x, item1=y, _nome=random.choice(_nam), _produto=_produts)
    elif ("{_nome}" in _return):
        return _return.format(item0=x, item1=y, _nome=random.choice(_nam))
    else:
        return _return.format(item0=x, item1=y)
