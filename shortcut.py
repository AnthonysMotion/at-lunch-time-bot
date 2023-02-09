import datetime
import re
import requests

def yearprogress_sc():
  current_date = datetime.datetime.now()
  year_start = datetime.datetime(current_date.year, 1, 1)
  days_passed = (current_date - year_start).days
  total_days = 365 if current_date.year % 4 != 0 else 366
  progress = round((days_passed / total_days) * 100, 2)
  return progress

def define_sc(word):
  response = requests.get(f'https://api.dictionaryapi.dev/api/v2/entries/en/{word}')
  data = response.json()
  definition = data[0]['meanings'][0]['definitions'][0]['definition']
  return f"```Definition of {word.title()}``` {definition}"