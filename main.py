# bot.py
import os
import random
import discord
from discord.ext import commands
from dotenv import load_dotenv

load_dotenv()
TOKEN = os.getenv('TOKEN')

bot = commands.Bot(command_prefix='!')

@bot.command(name='rick')
async def rick(ctx):   
        response = "https://www.youtube.com/watch?v=dQw4w9WgXcQ"
        await ctx.send(response)

@bot.command(name='mom')
async def mom(ctx):   
        response = "Your mom"
        await ctx.send(response)

@bot.command(name = "online")
async def online(ctx):
       ip = "google.com"
       response =  os.system('ping ' + ip)
       await ctx.send(response)
    
@bot.command(name = 'doom')
async def dm(ctx, user: discord.User, *, value):
    # Send a message to the mentioned user!
    await user.send(f"**{value}**")
    await user.send(f"||Sent by {ctx.author.display_name} via PKTGamerBot.||")

@bot.command(name = "gay")
async def gay(ctx):
       response =  ctx.author.display_name + " is Gay"
       await ctx.send(response)    

@bot.command(pass_context=True)
async def yt(ctx, url):

    author = ctx.message.author
    voice_channel = author.voice_channel
    vc = await bot.join_voice_channel(voice_channel)

    player = await vc.create_ytdl_player(url)
    player.start()

bot.run(TOKEN)