import discord
from discord import app_commands
from discord.ext import commands
from discord.app_commands import Choice

import datetime

class help(commands.Cog):
  def __init__(self, bot: commands.Bot) -> None:
    self.bot = bot

  @app_commands.command(name = "help", description = "List all commands, or get help for a specific command")
  @app_commands.describe(command = "Insert the command you need help with, or insert 'all' for all commands")
  @app_commands.choices(command=[Choice(name="all",value='all')])
  async def help(self, interaction: discord.Interaction, command: str):
    if command == 'all':
      await interaction.response.send_message("```ahk\n  /define\n  /yearprogress```", ephemeral=True)
    if command == 'define' or command == 'Define':
      await interaction.response.send_message("```ahk\nExample usage:\n  /define <word>\n  /define discord```", ephemeral=True)
    if command == 'yearprogress' or command == 'YearProgress' or command == 'Yearprogress':
      await interaction.response.send_message("```ahk\nExample usage:\n  /yearprogress```", ephemeral=True)


async def setup(bot: commands.Bot) -> None:
  await bot.add_cog(
    help(bot),
    guilds = [discord.Object(id = 489331089341415454)]
  )