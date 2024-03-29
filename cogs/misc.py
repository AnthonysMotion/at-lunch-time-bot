import datetime
import requests
from pyston import PystonClient, File #upm package(aiopyston)
from chatgpt import Conversation
import json
import asyncio
from bs4 import BeautifulSoup
import re

from discord import ui
import discord
from discord import app_commands
from discord.ext import commands
from discord.app_commands import Choice
from bs4 import BeautifulSoup

import shortcut

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

  # /ping
  @app_commands.command(name = "ping", description = "Show bot latency")
  async def ping(self, interaction: discord.Interaction):
    await interaction.response.send_message(f"{round(self.bot.latency * 1000)}ms")

  # /yearprogress
  @app_commands.command(name = "yearprogress", description = "Calculates how far we are into the current year")
  async def yearprogress(self, interaction: discord.Interaction):
    await interaction.response.send_message(f"We are {shortcut.yearprogress_sc()}% into the year")

  # /define
  @app_commands.command(name = "define", description = "Defines any given word in the English dictionary")
  async def define(self, interaction: discord.Interaction, word: str):
    await interaction.response.send_message(shortcut.define_sc(word))

  # /run
  @app_commands.command(name = "run", description = "Runs multiple lines of code in 20+ languages, all in Discord")
  async def run(self, interaction: discord.Interaction, lang: str, code: str):
    client = PystonClient()
    output = await client.execute(f"{lang}", [File(f"{code}")])
    await interaction.response.send_message(f"```{output}```")

  @app_commands.command(name = "convertcur", description = "Convert currency with up to date exchange rates")
  #@app_commands.describe(command = "To convert 100 NZ Dollars to JP YEN: /convertcur 100 NZD YEN")
  async def convertcur(self, interaction: discord.Interaction, amount: int, _from: str, _to: str):
    url = f"https://api.apilayer.com/exchangerates_data/convert?to={_to}&from={_from}&amount={amount}"
    payload = {}
    headers= {
      "apikey": "cQqGdzwECAIXQSqKdDEBPpH9HjJWWVKr"
    }
    response = requests.request("GET", url, headers=headers, data = payload)
    data = response.json()
    converted_amount = data['result']
    await interaction.response.send_message(f"{amount} {_from.upper()} to {_to.upper()} is {converted_amount}")

  # /mangalatest
  @app_commands.command(name = "mangalatest", description = "Check MangaBuddy for latest chapter of selected manga")
  async def mangalatest(self, interaction: discord.Interaction, title: str):
    url = f'https://mangabuddy.com/{title.replace(" ","-")}'
    resp = requests.get(url)
    soup = BeautifulSoup(resp.text, 'lxml')
    productDivs = soup.findAll('ul', attrs={'class' : 'chapter-list'})
    for div in productDivs:
      link = div.find('a')['href']
      ye = div.find('a')['title']
    try:
      daysago = soup.find('time', attrs={'class': 'chapter-update'}).get_text()
    except:
      await interaction.response.send_message('No search results')
    try:
      await interaction.response.send_message(f'**{ye}**\nLast Updated: `{daysago}`\n\n Read: https://mangabuddy.com/{link}')
    except:
      await interaction.response.send_message('No search results')
    
# cog setup
async def setup(bot: commands.Bot) -> None:
  await bot.add_cog(
    misc(bot),
    guilds = [discord.Object(id = 489331089341415454), discord.Object(id = 1040458176123916318)])