import discord
from discord.ext import commands
from core.classes import Cog_Extension
from discord.ext.commands import *

class Say(Cog_Extension):  
    
	@commands.command(brief="Send specific message in specific channel (Admin only)", description="")
	async def say(self,ctx,channel,*,msg):
		channel = channel[:-1][2:]
		channel_id = self.bot.get_channel(int(channel))
		await channel_id.send(msg)
		await ctx.send(f'Sent "{msg}" in channel <#{channel}> ')

def setup(bot):
	bot.add_cog(Say(bot))
