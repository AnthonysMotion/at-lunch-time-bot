# Discord
import discord
from discord import app_commands
from discord.ext import commands

# Misc
import json


intents = discord.Intents.default()
bot = discord.Client(intents=intents)
tree = app_commands.CommandTree(bot)

@bot.command()
async def ping(ctx):
    await ctx.send('nigga')

with open('config.json', 'r') as cfg:
  data = json.load(cfg) 

bot.run(data["token"])