import datetime
from selenium import webdriver
from selenium.webdriver.common.by import By

import discord
from discord import app_commands
from discord.ext import commands
from discord.app_commands import Choice


class fun(commands.Cog):
  def __init__(self, bot: commands.Bot) -> None:
    self.bot = bot


# cog setup

async def setup(bot: commands.Bot) -> None:
  await bot.add_cog(
    fun(bot),
    guilds = [discord.Object(id = 489331089341415454), discord.Object(id = 1040458176123916318)])