#!/usr/bin/env python3

# Kurisu by 916253 & ihaveamac
# license: Apache License 2.0
# https://github.com/916253/Kurisu

description = """
Kurisu, the bot for the 3DS Hacking Discord! Slowly replacing Saber as it is is no longer actively developed.
"""

# import dependencies
import os
from discord.ext import commands
import discord
import datetime, re
import json, asyncio
import copy
import configparser
import logging
import traceback
import sys
import os
from collections import Counter

# sets working directory to bot's folder
dir_path = os.path.dirname(os.path.realpath(__file__))
os.chdir(dir_path)

# read config for token
config = configparser.ConfigParser()
config.read("config.ini")

prefix = ['.']
bot = commands.Bot(command_prefix=prefix, description=description, pm_help=None)

@bot.event
async def on_ready():
    # this bot should only ever be in one server anyway
    for server in bot.servers:
        await bot.send_message(discord.utils.get(server.channels, name="mods"), "{} has started!".format(bot.user.name))
        break

# outputs errors to a log file, clears every run to save space
logger = logging.getLogger('discord')
logger.setLevel(logging.ERROR)
handler = logging.FileHandler(filename='kurisu_output.log', encoding='utf-8', mode='w')
handler.setFormatter(logging.Formatter('%(asctime)s:%(levelname)s:%(name)s: %(message)s'))
logger.addHandler(handler)

# loads extensions
addons = [
    'addons.memes',
    'addons.rules',
    'addons.assistance',
    'addons.mod',
    'addons.logs',
    'addons.load',
    'addons.ctrerr',
    'addons.ninerr',
]

for extension in addons:
    try:
        bot.load_extension(extension)
    except Exception as e:
        print('{} failed to load.\n{}: {}'.format(extension, type(e).__name__, e))

# Execute
print('Bot directory: ', dir_path)
bot.run(config['Main']['token'])
