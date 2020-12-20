import discord
import os
import random
from discord.ext import commands
from keep_alive import keep_alive

client = commands.Bot(command_prefix='.')


@client.event
async def on_ready():
    print('ingelogd als: ' + client.user.name + "\n")


@client.command()
async def ping(ctx):
    await ctx.send(f'ping is: {round(client.latency * 1000)}ms')


@client.command(aliases=['8ball', 'test'])
async def _8ball(ctx, *, question):
    responses = ['Natuurlijk', 'Oja zeker.', 'Nee natuurlijk niet.']

    await ctx.send(f'Question: {question}\nAnswer: {random.choice(responses)}')


@client.command()
async def kick(ctx, member: discord.Member, *, reason=None):
    await member.kick(reason=reason)


@client.command()
async def ban(ctx, member: discord.Member, *, reason=None):
    await member.ban(reason=reason)

keep_alive()
client.run(os.getenv('TOKEN'))
