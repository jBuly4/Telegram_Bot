import os
from collections import defaultdict
from dotenv import load_dotenv
import telebot


load_dotenv()
bot_token = os.getenv('BOT_TOKEN')
bot = telebot.TeleBot(bot_token)
LOCATIONS = defaultdict(lambda: {})  # all new locations will be created with empty dict


def get_state(message):
    return USER_STATE[message.chat.id]


