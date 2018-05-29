'''
Henry Huang
Created 12/16/2017
'''
import random
import asyncio
import string
import discord
from weather_getter_discord import Coordinates, Weather
from urllib.error import HTTPError
from discord.ext import commands
import urllib.request
import key
if not discord.opus.is_loaded():
    discord.opus.load_opus('opus')

bot = commands.Bot(command_prefix = commands.when_mentioned_or('!'))

@bot.command()
async def weather(location):
    coords = Coordinates(location)
    if str(coords) == "Location not found":
        await bot.say(coords)
        return
    else:
        weather_info = Weather(coords.get_lat, coords.get_lon)
        await bot.say(str(coords) + '\n' + str(weather_info))
    
@bot.command()
async def imgur():
    def url_maker():
        """Creates random imgur url"""
        chars = string.ascii_lowercase + string.ascii_uppercase + string.digits
        tempchar = [random.choice(chars) for n in range(5)]
        return "http://i.imgur.com/" + "".join(tempchar)
    opener = urllib.request.build_opener()
    while True:
        url = url_maker()
        try:
            opener.open(url)
            await bot.say(url)
            break
        except HTTPError:
            continue

@bot.event
async def on_ready():
    """Prints ready confirmation"""
    print('Logged in as')
    print(bot.user.name)
    print(bot.user.id)
    print('------')
bot.run(key.Bot_Token)
