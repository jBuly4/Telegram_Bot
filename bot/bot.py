import os
import telebot

from dotenv import load_dotenv
from state_manager import StateManager, LocationManager


load_dotenv()
bot_token = os.getenv('BOT_TOKEN')
bot = telebot.TeleBot(bot_token)

states = StateManager()
locations = LocationManager()

