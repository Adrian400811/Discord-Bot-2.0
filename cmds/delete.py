import discord
from discord.ext import commands
from discord.ext.commands import has_permissions
from core.classes import Cog_Extension

class Delete(Cog_Extension):  

    @commands.command(hidden = True)
    @has_permissions(manage_messages = True)
    async def delete(self,ctx,num:int):
        await ctx.channel.purge(limit=num+1)
        embed=discord.Embed(title="Delete", description=f"Deleted {num} messages", color=0x00ff00)
        embed.set_footer(text="Command Execute Successful")
        await ctx.send(embed=embed)
        print(f"{ctx.message.author} deleted {num} messages.")    

def setup(bot):
    bot.add_cog(Delete(bot))