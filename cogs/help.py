import datetime

import discord
from discord import app_commands
from discord.ext import commands
from discord.app_commands import Choice


class help(commands.Cog):
  def __init__(self, bot: commands.Bot) -> None:
    self.bot = bot

  @app_commands.command(name = "help", description = "List all commands")
  async def help(self, interaction: discord.Interaction):
    await interaction.response.send_message("```ahk\nGeneral\n  /define - Define any word in the English dictionary\n  /yearprogress - Show the progress through the current year in %\n  /run - Run code in any programming language\n  /rps - Play rock paper scissors\n  /chatgpt - Talk with ChatGPT through Discord\n  /convertcur - Convert currencies with accurate, up to date rates\n\nAnime & Manga\n  /mangalatest - Show the latest chapter of any manga, and a link to read\n\nAniList\n  /alpair - Pair an AL account\n  /alunpair - Unpair an AL account\n  /alprofile - Display basic info of your AL profile\n\nEconomy\n  /beg - Gain 0 to 10 tokens\n  /bal - Check token balance\n  /coinflip - 50/50 chance to win or lose your gamble```", ephemeral=True)
# cog setup

async def setup(bot: commands.Bot) -> None:
  await bot.add_cog(
    help(bot),
    guilds = [discord.Object(id = 489331089341415454), discord.Object(id = 1040458176123916318)])