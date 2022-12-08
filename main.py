# Discord
import discord
from discord.ext import commands

# Misc
import os
import json
from replit import db

bot = commands.Bot()

@bot.slash_command(name="test", guild_ids=[489331089341415454])
async def test(ctx): 
    await ctx.respond("hi")

for filename in os.listdir('./cogs'):
    if filename.endswith('.py'):
        bot.load_extension(f'cogs.{filename[0:-3]}')

bot.run(os.environ['token'])