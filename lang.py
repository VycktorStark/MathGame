__autor__ = "@VycktorStark"
__sourceoriginalcode__ = 'https://github.com/nickoala/telepot/blob/master/examples/callback/quiz.py'
__sourcecode__ = "https://github.com/VycktorStark/MathGame"
__starting__ = "START BOT"
LANG = dict()
LANG["en"] = {
    'startinggame': "<b>Mathematical calculation game:</b>\nThis is an educational game - where you practice your math skills and still have fun in the game, you can view your stats and show them to your friends. Click play and start now!\n\nThis game was created by Nickoala,and modified by @VycktorStark, you can view the original code<code>clicking here</code>",
    'status': "📊 Game Statistics:\n🏆 | Won: {}\n🙁 | lost: {}\n🕹 | Departures: {}\n_______________\nBy: " + __autor__,
    'stopinggame': "Game ended\n🏆 | Won: {}\n🙁 | lost: {}\n🕹 | Departures: {}\n_______________\nBy: " + __autor__,
    'buttonviewcodeorg': '💻 View Code original',
    'buttonviewcode': '💻 View Code',
    'buttongamestarting': '🎮 Play',
    'buttonback': '◀️ Come Back',
    'buttonstatistics': '📊 Statistics',
    'answer': [{
        'x':"{_nome} had {item0} and multiplied by {item1}\nWhat is the result?",
        '-': "{_nome} had {item0} {_produto}, and lost {item1}\nhow many {_produto}, does {_nome} have now?",
        '+': "{_nome} had {item0} {_produto}, and earn more {item1}\nhow many {_produto}, does {_nome} have now?",
    }],
    'buttonss': "Wait a moment, you're going too fast",
    'gameresult': [{
        True: "😃 You're right!!!",
        False: '😐 Unfortunately, you missed!'
    }],
    "product": ['laranja', 'maçã', 'uva', 'bala'],
    "name": ['Pedro', 'Carlos', 'Geovana', 'Larissa'],
}
LANG["pt"] = {
    'startinggame': "<b>Jogo de cálculo matemático:</b>\nEste é um jogo educacional - Onde você pratica suas habilidades de matemática e ainda se diverte no jogo, você pode ver suas estatísticas e mostrá-las aos seus amigos. Clique em jogar e começar agora!\n\nEste joguinho foi criado pelo Nickoala, e modificado por @VycktorStark, você pode visualizar o codigo original <code>clicando aqui</code>",
    'status': "📊 Estatísticas do Jogo:\n🏆 | Ganhou: {}\n🙁 | Perdeu: {}\n🕹 | Partidas: {}\n_______________\nBy: " + __autor__,
    'stopinggame': "Jogo encerrado\n🏆 | Ganhou: {}\n🙁 | Perdeu: {}\n🕹 | Partidas: {}\n_______________\nBy: " + __autor__,
    'buttonviewcodeorg': '💻 Ver Código original',
    'buttonviewcode': '💻 Ver Código',
    'buttongamestarting': '🎮 Jogar',
    'buttonback': '◀️ Voltar',
    'buttonstatistics': '📊 Estatísticas',
    'answer': [{
        'x':"{_nome} tinha {item0} e multiplicou por {item1}\nQual resultado?",
        '-': "{_nome} tinha {item0} {_produto}, e perdeu {item1}\nQuantas {_produto}, {_nome}  tem agora?",
        '+': "{_nome} tinha {item0} {_produto}, e ganhou mais {item1}\nQuantas {_produto}, {_nome}  tem agora?"
    }],
    'buttonss': 'Aguarde um momento, você está indo muito rapido',
    'gameresult': [{
        True: '😃 Você acertou!!!',
        False: '😐 Infelizmente, Você errou!'
    }],
    "product": ['laranja', 'maçã', 'uva', 'bala'],
    "name": ['Pedro', 'Carlos', 'Geovana', 'Larissa'],
}
LANG["es"] = {
    'startinggame': "<b>Juego de cálculo matemático:</b>\nEste es un juego educativo: donde practicas tus habilidades matemáticas y aún te diviertes en el juego, puedes ver tus estadísticas y mostrárselos a tus amigos. Haga clic en jugar y comience ahora.\n\nEste juego fue creado por Nickoala, y modificado por @VycktorStark, puedes ver el código original<code>haciendo clic aquí</code>",
    'status': "📊 Estadísticas de juego:\n🏆 | Ganó: {}\n🙁 | Perdido: {}\n🕹 | Salidas: {}\n_______________\nBy: " + __autor__,
    'stopinggame': "Juego terminado\n🏆 | Ganó: {}\n🙁 | Perdido: {}\n🕹 | Salidas: {}\n_______________\nBy: " + __autor__,
    'buttonviewcodeorg': '💻 Ver Código original',
    'buttonviewcode': '💻 Ver Código',
    'buttongamestarting': '🎮 Jugar',
    'buttonback': '◀️ Volver',
    'buttonstatistics': '📊 Estadísticas',
    'answer': [{
        'x': "{_nome} tenía {item0} y multiplicado por {item1}\n¿Cuál es el resultado?",
        '-': "{_nome} tenía {item0} {_produto} y perdió {item1}\ncuántos {_produto}, ¿tiene {_name} ahora?",
        '+': "{_nome} tenía {item0} {_produto}, y gana más {item1}\ncuántos {_produto}, ¿tiene {_name} ahora?"
    }],
    'buttonss': 'Espera un momento, vas demasiado rápido',
    'gameresult': [{
        True: '😃 Lo entendiste bien!!!',
        False: '😐 Lamentablemente, te perdiste!'
    }],
    "product": ['laranja', 'maçã', 'uva', 'bala'],
    "name": ['Pedro', 'Carlos', 'Geovana', 'Larissa'],
    }
