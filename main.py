from discord.ext import commands
from dotenv import load_dotenv
from utils import Button
from utils import Embed
import discord
import json
import os

intents = discord.Intents().all()

with open('commands.json', 'r') as f:
    command = json.load(f)


class MyBot(commands.Bot):
    async def on_ready(self):
        print('Logged on as', self.user)

    async def on_message(self, ctx):
        if ctx.author.bot:
            return

        if ctx.author == self.user:
            return

        if ctx.content in command:

            content = command[ctx.content].get('message')
            embed = Embed(command[ctx.content].get('embed')).get
            view = Button(ctx, command[ctx.content].get('button'))

            await ctx.reply(content=content, embed=embed, view=view)


load_dotenv()
bot = MyBot(command_prefix='!', intents=intents)
bot.run(os.environ.get('TOKEN'))
