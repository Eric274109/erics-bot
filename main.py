#Eric's Bot (✔)#1045

import discord
import os
client = discord.Client()
from replit import db

@client.event
async def on_ready():
  print('We have logged in as {0.user}'.format(client))

@client.event
async def on_message(message):
  if message.author == client.user:
    return
  authorid = str(message.author.id)
  try: 
    db[authorid] += 1
  except:
    db[authorid] = 1
  if not message.guild:
    await message.channel.send(db[authorid])
  #if None == if False
  print(message.content)
  if message.content.startswith('secret'):
    await message.channel.send('pss... hello')


client.run(os.environ['TOKEN'])