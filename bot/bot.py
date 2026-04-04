
import discord
from discord.ext import commands

class DebatinatorBot(commands.Bot):
    def __init__(self):
        intents = discord.Intents.default()
        intents.message_content = True
        super().__init__(command_prefix="!", intents=intents)
        self.user_service = None
    
    async def on_ready(self):
        print(f'Logged on as {self.user}!')

    async def setup_hook(self):
        await self.load_extension("cogs.general")
        await self.load_extension("cogs.ranking")