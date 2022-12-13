import os
from keep_alive import keep_alive

import discord
from discord.ext import commands
from discord import app_commands

# pref
activity = discord.Streaming(name="/help", url="https://www.twitch.tv/xqc")

class LunchTime(commands.Bot):
  def __init__(self):
    super().__init__(
      command_prefix = ',',
      intents = discord.Intents.all(),
      application_id = 1050257284204347394,
      activity=activity
    )

    # init cogs
    
    self.initial_extensions = [
      "cogs.misc",
      "cogs.help",
      "cogs.games",
      "cogs.economy",
      "cogs.fun"
    ]

  async def setup_hook(self):
    for ext in self.initial_extensions:
      await self.load_extension(ext)
    await bot.tree.sync(guild = discord.Object(id = 489331089341415454))
    await bot.tree.sync(guild = discord.Object(id = 1040458176123916318))

  # bot ready
  
  async def on_ready(self):
    print(f'{self.user} has connected to Discord')
  print("bot ready")

# start bot

keep_alive()
bot = LunchTime()
    
try:
  bot.run(os.environ['token'])
except discord.errors.HTTPException:
  os.system('kill 1')
  os.system("python restarter.py")