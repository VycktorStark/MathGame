* * *

                 ____       _                ____  _
                |  _ \ ___ | |__   ___      |  _ \| |__  
                | |_) / _ \| '_ \ / _ \     | | | | '_ \
                |  _ < (_) | |_) | (_) |    | |_| | |_) |  By: Vycktor Stark
                |_| \_\___/|_.__/ \___/     |____/|_.__/   Version: 3.0

                
* * *

## Getting Started

These instructions provided you with information about this project to be used for development and testing purposes.

## What is it?

Robot Db version 3.0 is a bot that uses the "Telegram-Bot-API" API written in Python, its structure was made from the Telepot library, and its plugins are made from the functions of this library.

This makes it easier to manage the bot and its plugins, allowing you to create new functions based on library functions and makes the code much more organized.

* * *

## Configuring bot

You should have your machine updated, having Python (3.5 +) and pip (8.1+) installed, plus some libs: telepot, objectjson, requests, simplejson.

What you need to do to install and use the project:

```
# Tested on Ubuntu 14.04, 15.04 and 16.04, Debian 7, Linux Mint 17.2

$ sudo apt-get update
$ sudo apt-get upgrade
## To install the libraries, just run run.sh and select option 5 or execute: 
$ sudo pip install -r requirements.txt
```

Cloning the repository:

```bash
# Cloning the repository and giving the permissions to start the initiation script

$ git clone https://github.com/VycktorStark/DbRobot-Py.git && sudo chmod 777 run.sh && ./run.sh

```


**First of all, take a look at your bot settings:**

> • Make sure privacy is off (more information on the [Bots official FAQ page](https://core.telegram.org/bots/faq#what-messages-will-my-bot-get)). Send `/setprivacy` for [BotFather](http://telegram.me/BotFather) To check the current setting.

**Before doing anything, open the DataConfig folder, and then open the Config-All folder and a text editor and make the following changes to the config.lua file:**

> • Set your Telegram ID to admin (in the `sudo` field).
>
> • Set `TOKEN` with the authentication token received from the [BotFather](http://telegram.me/BotFather).
>

## Initialization process

To start the bot, execute `cd DbRobot-Py/ && sudo chmod 777 run.sh && ./run.sh`. To stop the bot, press `Ctrl + c` twice.

You can also start the bot with `cd DbRobot-Py/ && pyhton3 main.py`, but then it will not restart automatically.

* * *

## Dedication

I dedicate my sincere credits to [Tiago Danin](https://github.com/tiagodanin) for having created the request script for tablela that helped me to make some plugins, and for my brother [Adilson Cavalcante](https://github.com/Player4NoobWinner). :p

* * *

## [@DbRobot](telegram.me/DbRobot)
