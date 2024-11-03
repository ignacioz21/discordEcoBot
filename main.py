import discord
import random
from discord.ext import commands
from challenges import *
description = 'This is a discord bot to reach awareness'
prefix = '^'

intents = discord.Intents.default()
intents.members = True
intents.message_content = True

bot = commands.Bot(command_prefix=prefix, description=description, intents=intents)

@bot.event
async def on_ready():
    print('El bot ha sido loggeado con exito')

@bot.command(name='challengeDaily')
async def challengeDaily(ctx):
    challenge = random.choice(eco_challenges)
    embed = discord.Embed(
        title= '**Reto del dia  :fire:**',
        description=challenge,
        color=discord.Color.green()
    )
    embed.set_footer(text='Gracias por aportar tu granito de arena por un mundo mas verde 🌎')
    await ctx.send(embed=embed)

@bot.command(name='ecoTips')
async def ecpTips(ctx):
    tip = random.choice(eco_tips)
    embed = discord.Embed(
        title='**Tip del dia  :recycle: **',
        description=tip,
        color=discord.Color.brand_green()
    )
    embed.set_footer(text='Gracias por aportar tu granito de arena por un mundo mas verde 🌎')
    await ctx.send(embed=embed)

bot.run('***')