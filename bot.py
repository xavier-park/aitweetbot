import discord
from discord.ext import commands

from dotenv import load_dotenv
import os

load_dotenv("important.env")

import aipost
import tweet

### UGLY UGLY UGLY UGLY UGLY UGLY UGLY UGLY UGLY UGLY UGLY UGLY UGLY UGLY UGLY


bot = commands.Bot(command_prefix = ">", intents = discord.Intents.all())

@bot.event
async def on_ready():
    await bot.change_presence(activity = discord.activity.Game(name="SpaceX Crash Simulator"))
    print(f"{bot.user.name} is online.")

@bot.command()
async def test(ctx):
    await ctx.send("hello")

@bot.command()
async def suggest(ctx):
    bot.newPost = aipost.genPost()
    await ctx.send("Post suggestion: \n\n" + bot.newPost)

@bot.command()
async def approve(ctx):
    if hasattr(bot, 'newPost'):  # Check if a new post has been suggested
        await tweet.post(bot.newPost)
        await ctx.send("Posted!\nhttps://twitter.com/opskittlez11")
        del bot.newPost  # Delete the new post after it's been posted

    else:
        await ctx.send("No post has been suggested.")

bot.run(os.getenv("bot_key"))
