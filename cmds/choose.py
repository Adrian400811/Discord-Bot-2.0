import discord
from discord.ext import commands
import random
from core.classes import Cog_Extension

class Choose(Cog_Extension):
    @commands.command()
    async def choose(self, ctx, *, selections):
        li = list(selections.split(" "))
        await ctx.send(random.choice(li))

def setup(bot):
    bot.add_cog(Choose(bot))