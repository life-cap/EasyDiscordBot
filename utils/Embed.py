from typing import Optional, Dict
import discord


class Embed:

    def __init__(
        self,
        json: Optional[dict] = None
    ):
        if json is None:
            self.embed = None

        else:
            self.json: Dict[str] = json
            self.title: Optional[str] = json.get("title")
            self.description: Optional[str] = json.get("description")
            self.color: Optional[hex] = json.get("color") if json.get("color", False) else 0x00ff00
            self.fields: Optional[dict] = json.get("fields")
            self.embed: Optional[
                discord.Embed
            ] = None if self.title is None and self.description is None else discord.Embed(
                                                                                 title=self.title,
                                                                                 description=self.description,
                                                                                 color=self.color
                                                                             )

            if self.fields is not None:
                for key, value in self.fields.items():
                    self.embed.add_field(name=key, value=value)

    @property
    def get(self) -> Optional[discord.Embed]:
        return self.embed
