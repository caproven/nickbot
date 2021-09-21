import os

import discord
from discord.ext import commands

TOKEN = os.getenv('DISCORD_TOKEN')
if not TOKEN:
    raise Exception('DISCORD_TOKEN not found')

bot = commands.Bot(command_prefix='!', case_insensitive=True)

@bot.event
async def on_ready():
    print(f'{bot.user} has connected to Discord!')

@bot.command(name='hello', help='Says hello')
async def hello(ctx: commands.Context):
    await ctx.send('Hello!')

@bot.command(name='changenick', help='Change someone\'s nickname')
@commands.has_guild_permissions(administrator=True)
async def changenick(ctx: commands.Context, member: discord.Member, nickname: str):
    print(f'Changing {member} nickname to {nickname}')
    await member.edit(nick=nickname)

bot.run(TOKEN)
