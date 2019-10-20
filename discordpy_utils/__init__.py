import discord
import random
import datetime


name = "discordpy_utils"

def randomColor():
    clist = ['blue', 'blurple', 'dark_blue', 'dark_gold', 'dark_green', 'dark_grey', 'dark_magenta', 'dark_orange', 'dark_purple', 'dark_red', 'dark_teal', 'darker_grey', 'gold', 'green', 'greyple', 'light_grey', 'lighter_grey', 'magenta', 'orange', 'purple', 'red', 'teal']
    return eval(f"discord.Color.{random.choice(clist)}")

def randomColour():
    return randomColor()

def setTimestamp(embed : discord.Embed):
    embed.timestamp = datetime.datetime.now() #This might come in handy for some people who dont know how to do this
    return embed

