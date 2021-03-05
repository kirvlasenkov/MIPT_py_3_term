import telegram
import os
import re
import logging
import time
import random
from dotenv import load_dotenv
from telegram.ext import (Updater, CommandHandler,
                          MessageHandler, Filters,
                          ConversationHandler, CallbackContext)

from vk import authorize, get_wall_post, VK_LOGIN, VK_PASSWORD, GROUP_ID
from text_processing import prepare_phrases
from markov import produce_phrases
from db import SqlDataBase


# logger setup
logging.basicConfig(
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s', level=logging.INFO
)
logger = logging.getLogger(__name__)


# Downloading of environment variables
dotenv_path = os.path.join(os.path.dirname(__file__), '.env')
if os.path.exists(dotenv_path):
    load_dotenv(dotenv_path)

# telegram setup
TOKEN = os.getenv("TG_TOKEN")
START_MESSAGE = os.getenv("TG_START_MESSAGE")
HELP_MESSAGE = os.getenv("TG_HELP_MESSAGE")
DESCRIPTION_MESSAGE = os.getenv("TG_DESCRIPTION_MESSAGE")
GENERATOR_MEDITATIVE = [
    os.getenv("TG_GENERATOR_RESPONSE_" + str(i))
    for i in range(1, 6)
]

# file for generator

phrases = []
surnames = []


def setup():
    global phrases
    global surnames

    file = os.getenv("FILE")
    pr_file = os.getenv("PR_FILE")

    vk = authorize(VK_LOGIN, VK_PASSWORD)
    get_wall_post(vk, GROUP_ID, file)
    file, surnames = prepare_phrases(file, pr_file)

    phrases = produce_phrases(file)


class Command:
    """
    Class, just needed to
    unite all bot eventual commands
    """
    __slots__ = ["__commands_list"]

    def __init__(self):
        self.__commands_list = [Command.command_start, Command.command_help, Command.command_description,
                                Command.command_generate]

    def commands(self):
        return self.__commands_list

    @staticmethod
    def command_start(update: telegram.Update, context: CallbackContext):
        return context.bot.send_message(chat_id=update.effective_chat.id, text=START_MESSAGE,
                                        reply_markup=reply_markup)

    @staticmethod
    def command_help(update: telegram.Update, context: CallbackContext):
        return context.bot.send_message(chat_id=update.effective_chat.id, text=HELP_MESSAGE,
                                        reply_markup=reply_markup)

    @staticmethod
    def command_description(update: telegram.Update, context: CallbackContext):
        return context.bot.send_message(chat_id=update.effective_chat.id, text=DESCRIPTION_MESSAGE,
                                        reply_markup=reply_markup)

    @staticmethod
    def command_generate(update: telegram.Update, context: CallbackContext):
        context.bot.send_message(chat_id=update.effective_chat.id, text=random.choice(GENERATOR_MEDITATIVE),
                                 reply_markup=reply_markup)

        time.sleep(random.randint(1, 3))
        phrase = f"{random.choice(surnames)}: {random.choice(phrases)}"
        context.bot.send_message(chat_id=update.effective_chat.id, text=phrase)

    @staticmethod
    def parse_commands():
        return re.findall(r"\bcommand\w+", " ".join(dir(Command())))


custom_keyboard = [
    ["/generate"],
    ["/help", "/desc"]
]
reply_markup = telegram.ReplyKeyboardMarkup(custom_keyboard)


def main():
    updater = Updater(token=TOKEN, use_context=True)
    dispatcher = updater.dispatcher

    setup()

    commands = Command().commands()
    for command in commands:
        command_handler = CommandHandler(str(command).split(" ")[1].split("_")[1], command)
        dispatcher.add_handler(command_handler)

    updater.start_polling()
    updater.idle()


if __name__ == "__main__":
    print(" ".join(dir(Command())))
    print(Command.parse_commands())
    main()
