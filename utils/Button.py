from discord import Enum, ButtonStyle
from typing import Dict, Optional
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


class CustomButton(discord.ui.Button):
    def __init__(self, user: discord.User, label: str, callback: Optional[str], style: Optional[str]):
        if style is None:
            super().__init__(style=ButtonStyle.green, label=label)
        else:
            super().__init__(style=getButtonColor(style), label=label)
        self.user = user
        self._callback = callback if callback is not None else 'hello'

    async def callback(self, interaction: discord.Interaction):
        if self.user.id != interaction.user.id:
            return await interaction.channel.send('You can not use this button!')
        return await interaction.response.send_message(self._callback, ephemeral=True)


class Button(discord.ui.View):
    def __init__(self, user: discord.User, json: Optional[Dict] = None):
        self.user = user
        self.json = json
        super().__init__()
        if self.json is not None:
            for key, value in self.json.items():
                self.add_item(CustomButton(self.user, key, value.get('callback'), value.get('style')))
