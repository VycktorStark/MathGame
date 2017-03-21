from telepot.namedtuple import InlineKeyboardMarkup, InlineKeyboardButton, ReplyKeyboardMarkup, KeyboardButton, InlineQueryResultArticle, InputTextMessageContent, ReplyKeyboardRemove, ForceReply, InlineQueryResultPhoto
from telepot.delegate import (
    per_chat_id, per_from_id, per_callback_query_origin, create_open, pave_event_space)
import random, telepot, telepot.helper, time, datetime, sys
from telepot.exception import BotWasBlockedError
from utils.config import *
from utils.utils import gameMat, Viewer, gsub, NSFW, URL_JSON, SendType, conversor, uptime
from utils.keyboards import *
from lang.lang import lang
from plugins.simple import simple
from plugins.Init import help
from plugins.Mediatype import midia
from plugins.control_sudo import control_plugin
from bot import main
from CallbackQuery import Callback
