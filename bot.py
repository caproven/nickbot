import os

import discord
from discord import app_commands
from discord.ext import commands

TOKEN = os.getenv("DISCORD_TOKEN")
if not TOKEN:
    raise Exception("env var DISCORD_TOKEN not found")

class Nickbot(discord.Client):
    def __init__(self):
        super().__init__(intents=discord.Intents.default())
        self.synced = False

    async def on_ready(self):
        await bot.wait_until_ready()
        if not self.synced:
            await tree.sync()
            self.synced = True
        print(f"{self.user} has connected to Discord")

bot = Nickbot()
tree = app_commands.CommandTree(bot)

@tree.command(name="changenick", description="change someone's nickname")
@commands.has_guild_permissions(administrator=True)
async def changenick(interaction: discord.Interaction, user: discord.Member, nickname: str):
    old = user.display_name
    await user.edit(nick=nickname)
    await interaction.response.send_message(f"Changed {user.name}'s nickname from [{old}] to [{nickname}]")

bot.run(TOKEN)
