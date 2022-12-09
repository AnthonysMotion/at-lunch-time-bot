import datetime
import requests
from pyston import PystonClient, File #upm package(aiopyston)
from chatgpt import Conversation
import json
import asyncio

from discord import ui
import discord
from discord import app_commands
from discord.ext import commands
from discord.app_commands import Choice

class misc(commands.Cog):
  def __init__(self, bot: commands.Bot) -> None:
    self.bot = bot

  # /about
  
  @app_commands.command(name = "about", description = "About Lunch Time")
  async def about(self, interaction: discord.Interaction):
    em = discord.Embed(title = "About", description = "Lunch Time is an easy to use, multipurpose bot that aims to bring outside functions into Discord through the use of slash commands; all packaged in a lightweight bot with a cat having lunch as its mascot.\n\nFor example: instead of opening Google and searching up 'How far are we into the year?' then finding a website, just type </yearprogress:1050348276030898196> and you'll get the same result quicker.\n\nFollow development: https://github.com/AnthonysMotion/at-lunch-time-bot\n\nGet started: </help:1050366133917720647>")
    em.set_author(name = "Lunch Time", url = 'https://anthonythach.com/', icon_url = 'https://i.imgur.com/E0u8ceW.png')
    em.set_footer(text='anthonythach.com',icon_url="https://i.imgur.com/BjKLqF7.png")
    em.set_image(url='https://media.tenor.com/i-xS-A_DTCEAAAAM/pizza-food.gif')
    em.set_thumbnail(url='https://i.imgur.com/E0u8ceW.png')
    await interaction.response.send_message(embed = em)

  # /yearprogress
  
  @app_commands.command(name = "yearprogress", description = "Calculates how far we are into the current year")
  async def yearprogress(self, interaction: discord.Interaction):
    current_date = datetime.datetime.now()
    year_start = datetime.datetime(current_date.year, 1, 1)
    days_passed = (current_date - year_start).days
    total_days = 365 if current_date.year % 4 != 0 else 366
    progress = round((days_passed / total_days) * 100, 2)
    await interaction.response.send_message(f"We are {progress}% into the year")

  # /define
    
  @app_commands.command(name = "define", description = "Defines any given word in the English dictionary")
  async def define(self, interaction: discord.Interaction, word: str):
    response = requests.get(f'https://api.dictionaryapi.dev/api/v2/entries/en/{word}')
    data = response.json()
    definition = data[0]['meanings'][0]['definitions'][0]['definition']
    await interaction.response.send_message(f"```Definition of {word.title()}``` {definition}")

  # /run
  
  @app_commands.command(name = "run", description = "Runs multiple lines of code in 20+ languages, all in Discord")
  async def run(self, interaction: discord.Interaction, lang: str, code: str):
    client = PystonClient()
    output = await client.execute(f"{lang}", [File(f"{code}")])
    await interaction.response.send_message(f"```{output}```")

  # /chatgpt
  @app_commands.command(name = "chatgpt", description = "Talk to ChatGPT through Discord")
  async def chatgpt(self, interaction: discord.Interaction, message: str):
      conversation = Conversation('cogs/config.json')
      await interaction.response.defer()
      reply = conversation.chat(message)
      print(reply)
      await interaction.followup.send(f"{reply}")
  
# cog setup

async def setup(bot: commands.Bot) -> None:
  await bot.add_cog(
    misc(bot),
    guilds = [discord.Object(id = 489331089341415454)]
  )