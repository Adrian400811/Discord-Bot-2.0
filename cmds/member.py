import discord
from discord.ext import commands
from core.classes import Cog_Extension
import json

with open('setting.json',mode='r',encoding='utf8') as jfile:
    jdata = json.load(jfile)

class Member(Cog_Extension):
    
    @commands.Cog.listener()
    async def on_member_join(self, member):
        print(f'{member}joined')
        channel = self.bot.get_channel(int(jdata['MAIN_CHANNEL']))
        embed=discord.Embed(title="Welcome!", description=f"{member.mention} joined the server!", color=0x00ff00)
        embed.set_footer(text="Command Execute Successful")
        await channel.send(embed=embed)

    @commands.Cog.listener()
    async def on_member_remove(self, member):
        print(f'{member}left')
        channel = self.bot.get_channel(int(jdata['MAIN_CHANNEL']))
        embed=discord.Embed(title="Bye!", description=f"{member.mention} left the server!", color=0x00ff00)
        embed.set_footer(text="Command Execute Successful")
        await channel.send(embed=embed)

def setup(bot):
    bot.add_cog(Member(bot))
