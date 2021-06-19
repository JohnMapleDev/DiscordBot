# B3ngT, The bot
# Bot
# Bot?
# Bot!

# bot.py
import os

# bot.py
import os

import discord

class CustomClient(discord.Client):
    async def on_ready(self):
        print(f'{self.user} has connected to Discord!')

client = CustomClient()
client.run(TOKEN)