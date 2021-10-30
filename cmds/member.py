import discord
from discord.ext import commands
from core.classes import Cog_Extension

class Member(Cog_Extension):
    
    @commands.Cog.listener()
    async def on_member_join(self, member, guild):
        print(f'{member}joined')
        for channel in guild.text_channels:
            if "general" in channel.name:
                embed=discord.Embed(title="Welcome!", description=f"{member.mention} joined the server!", color=0x00ff00)
                embed.set_footer(text="Command Execute Successful")
                await channel.send(embed=embed)

    @commands.Cog.listener()
    async def on_member_remove(self, member, guild):
        print(f'{member}left')
        for channel in guild.text_channels:
            if "general" in channel.name:
                embed=discord.Embed(title="Bye!", description=f"{member.mention} left the server!", color=0x00ff00)
                embed.set_footer(text="Command Execute Successful")
                await channel.send(embed=embed)
        
def setup(bot):
    bot.add_cog(Member(bot))
