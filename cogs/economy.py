import datetime
import random
from replit import db

import discord
from discord import app_commands
from discord.ext import commands
from discord.app_commands import Choice

class economy(commands.Cog):
  def __init__(self, bot: commands.Bot) -> None:
    self.bot = bot

  @app_commands.command(name = "bal", description = "Check your lunch token balance")
  async def bal(self, interaction: discord.Interaction):
    id = interaction.user.id
    t = random.randrange(0,10)
    try:
      value = db[f"{id}_bal"]
    except KeyError:
      db[f"{id}_bal"] = 0
      value = db[f"{id}_bal"]
    await interaction.response.send_message(f"You have {value} lunch tokens")

  @app_commands.command(name = "beg", description = "Gain between 0 - 10 lunch tokens")
  async def beg(self, interaction: discord.Interaction):
    id = interaction.user.id
    t = random.randrange(0,10)
    db[f"{id}_bal"] += int(t)
    await interaction.response.send_message(f"You gained {str(t)} lunch tokens!")

  @app_commands.command(name = "coinflip", description = "Bet on a coinflip to potentially 2x your Lunch Tokens")
  async def coinflip(self, interaction: discord.Interaction, amount: int):
    id = interaction.user.id
    t = random.randrange(0,2)
    if t == 1:
      db[f"{id}_bal"] -= amount
      await interaction.response.send_message(f"Unlucky. You lost {str(amount)} lunch tokens")
    else:
      db[f"{id}_bal"] += amount
      await interaction.response.send_message(f"Congratulations! You won {str(amount)} lunch tokens")
      
# cog setup

async def setup(bot: commands.Bot) -> None:
  await bot.add_cog(economy(bot),guilds = [discord.Object(id = 489331089341415454), discord.Object(id = 1040458176123916318)])