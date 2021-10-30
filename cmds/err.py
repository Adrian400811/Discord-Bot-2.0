import discord
from discord.ext import commands
from discord.ext.commands import CommandError, has_permissions, MissingPermissions
from core.classes import Cog_Extension

class Err(Cog_Extension): 
    @commands.Cog.listener()
    async def on_command_error(self, ctx, error):
        if isinstance(error, commands.CommandError):
            if isinstance(error, commands.CommandNotFound):
                embed=discord.Embed(title="Command not found", description=f"{error}", color=0xff0000)
                embed.set_footer(text="err=CommandNotFound")
                await ctx.send(embed=embed)
                print(f"{error}")
            elif isinstance(error, commands.MissingRequiredArgument):
                embed=discord.Embed(title="Missing arguement", description=f"{error}", color=0xff0000)
                embed.set_footer(text="err=MissingRequiredArgument")
                await ctx.send(embed=embed)
                print(f"{error}")
            elif isinstance(error, commands.MissingPermissions):
                embed=discord.Embed(title="Missing permissions", description=f"{error}", color=0xff0000)
                embed.set_footer(text="err=MissingPermissions")
                await ctx.send(embed=embed)
            elif isinstance(error, commands.BotMissingPermissions):
                embed=discord.Embed(title="Bot Missing permissions", description=f"{error}", color=0xff0000)
                embed.set_footer(text="err=BotMissingPermissions")
                await ctx.send(embed=embed)
            elif isinstance(error, commands.ExtensionError):
                embed=discord.Embed(title="Extension error", description=f"{error}", color=0xff0000)
                embed.set_footer(text="err=ExtensionError")
                await ctx.send(embed=embed)
            elif isinstance(error, commands.ExtensionAlreadyLoaded):
                embed=discord.Embed(title="Extension already loaded", description=f"{error}", color=0xff0000)
                embed.set_footer(text="err=ExtensionAlreadyLoaded")
                await ctx.send(embed=embed)
            elif isinstance(error, commands.ExtensionFailed):
                embed=discord.Embed(title="Extension failed", description=f"{error}", color=0xff0000)
                embed.set_footer(text="err=ExtensionFailed")
                await ctx.send(embed=embed)
            elif isinstance(error, commands.ExtensionNotFound):
                embed=discord.Embed(title="Extension not found", description=f"{error}", color=0xff0000)
                embed.set_footer(text="err=ExtensionNotFound")
                await ctx.send(embed=embed)
            elif isinstance(error, commands.ExtensionNotLoaded):
                embed=discord.Embed(title="Extension not loaded", description=f"{error}", color=0xff0000)
                embed.set_footer(text="err=ExtensionNotLoaded")
                await ctx.send(embed=embed)
            elif isinstance(error, commands.NotOwner):
                embed=discord.Embed(title="Not Owner", description=f"{error}", color=0xff0000)
                embed.set_footer(text="err=NotOwner")
                await ctx.send(embed=embed)
            print(f"{error}")


def setup(bot):
    bot.add_cog(Err(bot))