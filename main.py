import discord
from discord.ext import commands
import token
import json

bot = commands.Bot(command_prefix=None)

@bot.command()
async def ping(ctx):
    await ctx.send('nigga')

with open('config.json', 'r') as cfg:
  data = json.load(cfg) 

bot.run(data["token"])