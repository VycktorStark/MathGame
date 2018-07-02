* * *

                 ____       _                ____  _
                |  _ \ ___ | |__   ___      |  _ \| |__  
                | |_) / _ \| '_ \ / _ \     | | | | '_ \
                |  _ < (_) | |_) | (_) |    | |_| | |_) |  By: Vycktor Stark
                |_| \_\___/|_.__/ \___/     |____/|_.__/   Version: 3.0 Telegram-BOT

                
* * *

## Getting Started

These instructions provided you with information about this project to be used for development and testing purposes.

## What is it?

Robot Db version 3.0 is a project for Telegram, a BOT written in Python, its structure was made from the Telepot library which is based on the "Telegram-BOT-API", and all plugins in this base are made from the functions of this library, this makes it easier to manage the bot and its plugins and make the code much more organized.

* * *

## Configuring bot

You should have your machine updated, having Python (3.5 +) and pip (8.1+) installed, plus some libs: telepot, objectjson, requests, simplejson, and if you do not have it, you need to install it this way:

```
# Tested on Ubuntu 14.04, 15.04 and 16.04, Debian 7, Linux Mint 17.2

$ sudo apt-get update && sudo apt-get upgrade && sudo apt-get install python3 python3-pip && sudo pip install -r requirements.txt
```

Cloning the repository:

```bash
$ git clone https://github.com/VycktorStark/DbRobot-Python.git

```


**First of all, take a look at your bot settings:**

> • Make sure privacy is off (more information on the [Bots official FAQ page](https://core.telegram.org/bots/faq#what-messages-will-my-bot-get)). Send `/setprivacy` for [BotFather](http://telegram.me/BotFather) To check the current setting.

**Before doing anything, open the utils folder, and a text editor and make the following changes to the config.py file:**

> • Set your Telegram ID to admin (in the `sudo` field).
>
> • Set `TOKEN` with the authentication token received from the [BotFather](http://telegram.me/BotFather).
>

## Initialization process

To start the bot, execute `cd DbRobot-Python/ && sudo chmod 777 run.sh && ./run.sh`. To stop the bot, press `Ctrl + c` twice.

You can also start the bot with `cd DbRobot-Python/ && pyhton3 main.py`, but then it will not restart automatically.

* * *

## Dedication

I dedicate my sincere credits to [Tiago Danin](https://github.com/tiagodanin) for having created the request script for tablela that helped me to make some plugins, and for my brother [Adilson Cavalcante](https://github.com/Player4NoobWinner). :p

* * *

## [@DbRobot](telegram.me/DbRobot)
