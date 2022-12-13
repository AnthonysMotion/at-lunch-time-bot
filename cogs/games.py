import datetime
from datetime import datetime
import random
from replit import db
import requests
import json

import discord
from discord import app_commands
from discord.ext import commands
from discord.app_commands import Choice

class games(commands.Cog):
  def __init__(self, bot: commands.Bot) -> None:
    self.bot = bot

  # /rps
  
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

  # anilist pair
  @app_commands.command(name = "alpair", description = "Pair your AniList.com account")
  async def alpair(self, interaction: discord.Interaction, username: str):
    id = interaction.user.id
    db[f"{id}"] = f"{username}"
    acc = db[f"{id}"]
    await interaction.response.send_message(f"You're now paired to AniList as '{acc}'")

  # anilist unpair
  @app_commands.command(name = "alunpair", description = "Unpair your AniList.com account")
  async def alunpair(self, interaction: discord.Interaction):
    id = interaction.user.id
    name = db[f"{id}"]
    await interaction.response.send_message(f"You're now unpaired from {name}")
    del db[f"{id}"]

  # anilist acc
  @app_commands.command(name = "alacc", description = "Check what AniList account you're currently paired to")
  async def alacc(self, interaction: discord.Interaction):
    id = interaction.user.id
    acc = db[f"{id}"]
    await interaction.response.send_message(f"You're paired to {acc}")

  # anilist profile
  @app_commands.command(name = "alprofile", description = "Check your AniList profile")
  async def alprofile(self, interaction: discord.Interaction):
    id = interaction.user.id
    query = '''
    query ($name: String) {
        User (name: $name) {
            id
            name
            about
            donatorTier
            unreadNotificationCount
            createdAt
            avatar {
              large
            }
            statistics {
              anime {
                count
                episodesWatched
                minutesWatched
                meanScore
              }
              manga {
                count
                chaptersRead
                volumesRead
              }
            }
        }
    }
    '''
    variables = {
        'name': db[f"{id}"],
    }
    url = 'https://graphql.anilist.co'
    
    # Make the HTTP Api request
    response = requests.post(url, json={'query': query, 'variables': variables})
    data = json.loads(response.text)
    
    name = data['data']['User']['name']
    avatar = data['data']['User']['avatar']['large']
    count = data['data']['User']['statistics']['anime']['count']
    episodeswatched = data['data']['User']['statistics']['anime']['episodesWatched']
    minuteswatched = data['data']['User']['statistics']['anime']['minutesWatched']
    days = round(minuteswatched / 1440)
    mangacount = data['data']['User']['statistics']['manga']['count']
    chaptersRead = data['data']['User']['statistics']['manga']['chaptersRead']
    volumesRead = data['data']['User']['statistics']['manga']['volumesRead']
    meanScore = data['data']['User']['statistics']['anime']['meanScore']
    donatorTier = data['data']['User']['donatorTier']
    createdAt = data['data']['User']['createdAt']
    date = datetime.fromtimestamp(createdAt).strftime("%Y-%m-%d")
    year = date[:4]
    monthtemp = str(date[5:-3])
    day = date[8:]
    month = 'None'
    if monthtemp == '01':
      month = 'January'
    elif monthtemp == '02':
      month = 'February'
    elif monthtemp == '03':
      month = 'March'
    elif monthtemp == '04':
      month = 'April'
    elif monthtemp == '05':
      month = 'May'
    elif monthtemp == '06':
      month = 'June'
    elif monthtemp == '07':
      month = 'July'
    elif monthtemp == '08':
      month = 'August'
    elif monthtemp == '09':
      month = 'September'
    elif monthtemp == '10':
      month = 'October'
    elif monthtemp == '11':
      month == 'November'
    else:
      month == 'December'
    em = discord.Embed(title = name,description=f"Donator Tier: {str(donatorTier)}\nAccount Creation Date: {int(day)} {month} {year}")
    em.set_thumbnail(url = avatar)
    em.set_author(name = name, url = avatar, icon_url = avatar)
    em.add_field(name = "**Total Anime**", value = count)
    em.add_field(name = "**Episodes Watched**", value = episodeswatched)
    em.add_field(name = "**Days Watched**", value = days)
    em.add_field(name = "**Total Manga**", value = mangacount)
    em.add_field(name = "**Chapters Read**", value = chaptersRead)
    em.add_field(name = "**Volumes Read**", value = volumesRead)
    em.add_field(name = "**Mean Score**", value = meanScore)
    await interaction.response.send_message(embed = em)

      
# cog setup

async def setup(bot: commands.Bot) -> None:
  await bot.add_cog(
    games(bot),
    guilds = [discord.Object(id = 489331089341415454), discord.Object(id = 1040458176123916318)])