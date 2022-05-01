from discord.ext import commands
from utils.Button import Button
from dotenv import load_dotenv
from utils.Embed import Embed
import discord
import json
import os

load_dotenv()

intents = discord.Intents().all()

with open('commands.json', 'r') as f:
    command = json.load(f)


class MyBot(commands.Bot):
    async def on_ready(self):
        print('Logged on as', self.user)

    async def on_message(self, ctx):
        if ctx.author == self.user:
            return

        if ctx.content in command:
            content = command[ctx.content].get('message')
            embed = Embed(command[ctx.content].get('embed')).get
            view = Button(command[ctx.content].get('button'))
            await ctx.reply(content=content, embed=embed, view=view)


client = MyBot(command_prefix='!', intents=intents)
client.run(os.environ.get('TOKEN'))
