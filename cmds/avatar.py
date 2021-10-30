import discord
from discord.ext import commands
from core.classes import Cog_Extension

class Avatar(Cog_Extension):  
    @commands.command()
    async def avatar(self, ctx, *,  avamember : discord.Member=None):
        userAvatarUrl = avamember.avatar_url
        await ctx.send(userAvatarUrl)

def setup(bot):
    bot.add_cog(Avatar(bot))