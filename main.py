import discord 
import os
import random
from discord.ext import commands

client = commands.Bot(command_prefix = '.')

@client.event
async def on_ready():
  print ('Bot is klaar')

@client.command()
async def ping(ctx):
    await ctx.send(f'ping is: {round(client.latency * 1000)}ms')

@client.command(aliases=['8ball', 'test'])
async def _8ball(ctx, *, question):
    responses = ['Natuurlijk', 
                  'Oja zeker.',
                  'Nee natuurlijk niet.']

    await ctx.send(f'Question: {question}\nAnswer: {random.choice(responses)}')
    
client.run(os.getenv('TOKEN'))
