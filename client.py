import discord
import os
import random
from dotenv import load_dotenv

load_dotenv()
TOKEN = os.environ['TOKEN']
GUILD = os.getenv('GUILD')

client = discord.Client()

@client.event
async def on_ready():
    print(f'{client.user.name} has connected to Discord!')

@client.event
async def on_member_join(member):
    await member.create_dm()
    await member.dm_channel.send(
        f'Hi {member.name}, welcome to my PKT MC Discord server!'
    )

@client.event
async def on_message(message):
    if message.author == client.user:
        return
    
    if message.content == '?rick':
        response = "https://www.youtube.com/watch?v=dQw4w9WgXcQ"
        await message.channel.send(response)
    elif message.content == 'raise-exception':
        raise discord.DiscordException

@client.event
async def on_error(event, *args, **kwargs):
    with open('err.log', 'a') as f:
        if event == 'on_message':
            f.write(f'Unhandled message: {args[0]}\n')
        else:
            raise
            
client.run(TOKEN)