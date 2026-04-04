
from discord.ext import commands

class Ranking(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
        
    @commands.command()
    async def ranking(self, ctx):
        await ctx.send("Ranking command is not implemented yet.")
    
    @commands.command()
    async def ranking_update(self, ctx):
        print(ctx)
        await ctx.send(f"Updating ranking for user {5} with points {10}. (Not implemented yet)")
        
async def setup(bot):
    await bot.add_cog(Ranking(bot))