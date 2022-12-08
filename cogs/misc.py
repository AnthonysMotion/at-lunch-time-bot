import discord
from discord import app_commands
from discord.ext import commands
from discord.app_commands import Choice

import datetime
import requests

class misc(commands.Cog):
  def __init__(self, bot: commands.Bot) -> None:
    self.bot = bot

  @app_commands.command(name = "yearprogress", description = "Calculates how far we are into the current year")
  async def yearprogress(self, interaction: discord.Interaction):
    current_date = datetime.datetime.now()
    year_start = datetime.datetime(current_date.year, 1, 1)
    days_passed = (current_date - year_start).days
    total_days = 365 if current_date.year % 4 != 0 else 366
    progress = round((days_passed / total_days) * 100, 2)
    await interaction.response.send_message(f"We are {progress}% into the year")

  @app_commands.command(name = "define", description = "Defines any given word in the English dictionary")
  async def define(self, interaction: discord.Interaction, word: str):
    response = requests.get(f'https://api.dictionaryapi.dev/api/v2/entries/en/{word}')
    data = response.json()
    definition = data[0]['meanings'][0]['definitions'][0]['definition']
    await interaction.response.send_message(f"```Definition of {word.title()}``` {definition}")

async def setup(bot: commands.Bot) -> None:
  await bot.add_cog(
    misc(bot),
    guilds = [discord.Object(id = 489331089341415454)]
  )