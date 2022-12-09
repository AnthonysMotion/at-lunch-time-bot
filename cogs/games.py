import discord
from discord import app_commands
from discord.ext import commands
from discord.app_commands import Choice

import datetime
import random

class games(commands.Cog):
  def __init__(self, bot: commands.Bot) -> None:
    self.bot = bot

  @app_commands.command(name = "rps", description = "Play rock paper scissors vs Lunch Time")
  @app_commands.choices(choice=[Choice(name="Rock",value='rock'),Choice(name="Paper",value='Paper'),Choice(name="Scissors",value='scissors')])
  async def help(self, interaction: discord.Interaction, choice: str):
    user_choice = choice
    bot_choice = random.choice(['rock', 'paper', 'scissors'])
    if (user_choice == 'rock' and bot_choice == 'scissors') or (user_choice == 'paper' and bot_choice == 'rock') or (user_choice == 'scissors' and bot_choice == 'paper'):
      winner = 'user'
    elif (bot_choice == 'rock' and user_choice == 'scissors') or (bot_choice == 'paper' and user_choice == 'rock') or (bot_choice == 'scissors' and user_choice == 'paper'):
      winner = 'bot'
    else:
      winner = 'none'
    if winner == 'user':
      await interaction.response.send_message(f'You chose {user_choice} and I chose {bot_choice}. You win!')
    elif winner == 'bot':
      await interaction.response.send_message(f'You chose {user_choice} and I chose {bot_choice}. You lose!')
    else:
      await interaction.response.send_message(f"You chose {user_choice} and I chose {bot_choice}. It's a tie!")

async def setup(bot: commands.Bot) -> None:
  await bot.add_cog(
    games(bot),
    guilds = [discord.Object(id = 489331089341415454)]
  )