import discord
from discord.ext import commands
from discord.ext.commands import CommandError, has_permissions, MissingPermissions
from core.classes import Cog_Extension

class Err(Cog_Extension): 
	@commands.Cog.listener()
	async def on_command_error(self, ctx, error):
        
		if isinstance(error, commands.CommandError):    
			print(f"{error}")
			await ctx.send(f'{error}')


def setup(bot):
	bot.add_cog(Err(bot))
