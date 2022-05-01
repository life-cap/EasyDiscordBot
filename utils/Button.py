from typing import Dict, Optional, Union
from discord import Enum, ButtonStyle
from discord.ext import commands
from utils import Embed
import discord


def getButtonColor(color: str) -> ButtonStyle:
    if color == 'red':
        return ButtonStyle.danger
    elif color == 'green':
        return ButtonStyle.green
    elif color == 'blurple':
        return ButtonStyle.blurple
    elif color == 'grey':
        return ButtonStyle.grey


class Button(discord.ui.View):
    def __init__(
            self,
            ctx: commands.Context,
            json: Optional[Dict] = None
    ):
        self.ctx = ctx
        self.json = json
        super().__init__()

        if self.json is not None:
            for key, value in self.json.items():
                self.add_item(CustomButton(self.ctx, key, value.get('callback'), value.get('style')))


class CustomButton(discord.ui.Button):
    def __init__(
            self,
            ctx: commands.Context,
            label: str,
            callback: Optional[Union[dict]],
            style: Optional[str]
    ):

        if style is None:
            super().__init__(style=ButtonStyle.green, label=label)

        else:
            super().__init__(style=getButtonColor(style), label=label)

        self.ctx = ctx
        self._callback = callback if callback is not None else 'hello'

    async def callback(self, interaction: discord.Interaction):

        if self.ctx.author.id != interaction.user.id:
            return await interaction.channel.send('You can not use this button!')

        content = self._callback.get('message')
        embed = Embed(self._callback.get('embed')).get
        view = Button(self.ctx, self._callback.get('button'))

        await interaction.response.send_message(content=content, embed=embed, view=view)
        self.view.stop()
