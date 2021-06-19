# B3ngT, The bot
# Bot
# Bot?
# Bot!
import discord
import json
import aiohttp
import random
import requests
from aiohttp import ClientSession

import koden  # Discord Bot Token

from discord.ext import commands

bot = commands.Bot(command_prefix='!')


@bot.event
async def on_ready():
    print(f'{bot.user.name} has connected to Discord!')


@bot.event
async def BaseActivity():
    await bot.change_presence(activity=discord.Activity(type=discord.ActivityType.watching, name="snuskiga filmer"))


@bot.command(name='hej', help='Svarar med ett sött meddelande')
async def greetings_response(ctx):
    greetingsList = [
        'Hejsan hoppsan',
        'Du är lika mycket värd som en trasig toffla <3'
    ]
    responseGreeting = random.choice(greetingsList)
    await ctx.send(responseGreeting)
    print(responseGreeting)


@bot.command(name="img", help="Visar en slumpmässig bild, ex !img Forest")
async def img(ctx, arg):
    embed = discord.Embed(
        title='Random Image 🐈',
        description='Random',
        colour=discord.Colour.purple()
    )
    embed.set_image(url='https://source.unsplash.com/1600x900/?{}'.format(arg))
    embed.set_footer(text="")
    await ctx.send(embed=embed)
    print("Image sent, unsplash")


@bot.command(name="cat", help="Visar en slumpmässig bild på en katt!")
async def cat(ctx):
    response = requests.get('https://aws.random.cat/meow')
    data = response.json()
    embed = discord.Embed(
        title='Kitty Cat 🐈',
        description='Cat',
        colour=discord.Colour.purple()
    )
    embed.set_image(url=data['file'])
    embed.set_footer(text="")
    await ctx.send(embed=embed)
    print("Image sent, cat")


@bot.command(name="meme", help="Slumpmässig bild från r/dankmemes new",pass_context=True)
async def meme(ctx):
    embed = discord.Embed(title="", description="")

    async with aiohttp.ClientSession() as cs:
        async with cs.get('https://www.reddit.com/r/dankmemes/new.json?sort=new') as r:
            res = await r.json()
            embed.set_image(url=res['data']['children'] [random.randint(0, 25)]['data']['url'])
            await ctx.send(embed=embed)
            print("Sent random meme, new")


@bot.command(name="shot", help="Vem ska ta en shot?")
async def shot(ctx):

    shotTaker = ["<@219427025281220609>", "<@219823742963023872>"]
    random_num = str(random.choice(shotTaker))
    await ctx.send("Grattis, "+random_num+ " måste ta en shot :tumbler_glass:")
    print("Mention sent.")

bot.run(koden.TOKENDisc)
