import datetime

import discord
from discord import app_commands
from discord.ext import commands
from discord.app_commands import Choice


class help(commands.Cog):
  def __init__(self, bot: commands.Bot) -> None:
    self.bot = bot

  @app_commands.command(name = "help", description = "List all commands, or get help for a specific command")
  @app_commands.describe(command = "Insert the command you need help with, or insert 'all' for all commands")
  @app_commands.choices(command=[Choice(name="all",value='all'),Choice(name="/define",value='define'),Choice(name="/yearprogress",value='yearprogress'),Choice(name="/run",value='run'),Choice(name="/rps",value='rps'),Choice(name="/anilist",value='anilist')])
  async def help(self, interaction: discord.Interaction, command: str):
    if command == 'all':
      await interaction.response.send_message("```ahkGeneral commands\n  /define\n  /yearprogress\n  /run\n  /rps\nAniList commands\n  /alpair\n  /alunpair\n  /alacc\n  /alprofile```", ephemeral=True)
    if command == 'define' or command == 'Define':
      await interaction.response.send_message("```ahk\nExample usage:\n  /define <word>\n  /define discord```", ephemeral=True)
    if command == 'yearprogress' or command == 'YearProgress' or command == 'Yearprogress':
      await interaction.response.send_message("```ahk\nExample usage:\n  /yearprogress```", ephemeral=True)
    if command == 'run' or command == 'Run':
      await interaction.response.send_message("```ahk\nExample usage:\n  /run <lang> <code>\n  /run python print('Hello world')```", ephemeral=True)
    if command == 'rps':
      await interaction.response.send_message("```ahk\nExample usage:\n  /rps rock```", ephemeral=True)
# cog setup

async def setup(bot: commands.Bot) -> None:
  await bot.add_cog(
    help(bot),
    guilds = [discord.Object(id = 489331089341415454)]
  )