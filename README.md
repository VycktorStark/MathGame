## Getting Started

These instructions will provide you with a copy of the project and show you how to get started using it for development and testing purposes.

## Configuring the bot to run on the terminal
You must have your machine up to date and have Python 3 installed, as well as some modules, such as: flask and requests, and of course the telepot, if you don't have it, you will need to install it this way here:
```
# Tested on Ubuntu 14.04, 15.04 and 16.04, Debian 7, Linux Mint 17.2
$ sudo apt-get update && sudo apt-get upgrade   
$ sudo apt install python3 && python3-pip
$ sudo pip3 install flask && requests && telepot
```
With everything installed, we will clone the repository like this:

```
$ git clone https://github.com/VycktorStark/MathGame.git
```

With the repository installed, you must have the bot token created by [BotFather](http://telegram.me/BotFather); if you don't have one, you'll need to create one (more information on [official robot FAQ page](https://core.telegram.org/bots/faq#what-messages-will-my-bot-get))

To add your token to the project, I advise you to configure your ".bashrc", putting something like:
```
export TOKEN="12918981:dFwnfweFw2oju28ru239r8389iEJOIJO"
```

Or just configure the `tools.py`

## Boot process

- To start the bot, run: sudo ./main.py
- To stop the bot, press Ctrl + C.
You can also start the bot with python3 main.py


## Configuring the bot to run on heroku

Click the button below and configure your language, also setting your bot's token.

[![Deploy to Heroku](https://www.herokucdn.com/deploy/button.svg)](https://heroku.com/deploy)

Only that, the project will already be working.
