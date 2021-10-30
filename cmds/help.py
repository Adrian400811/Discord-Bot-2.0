import discord
from discord.ext import commands
from core.classes import Cog_Extension


class Help(Cog_Extension):

    @commands.command()
    async def help(self, ctx, item="main"):
        xlist = ["main","avatar","forecast","mc","ping","qr","say","status","weather"]
        embed=discord.Embed(title="Help", description="0help <command> to get details of the command", color=0x00ff00)
        if item == "main":
            embed.add_field(name="Command List", value="avatar\nforecast\nmc\nping\nqr\nsay\nstatus\nweather\n", inline=False)
        if item == "avatar":
            embed.add_field(name="avatar <tag someone>", value="Get someone's avatar.", inline=False)
        if item == "forecast":
            embed.add_field(name="forecast <location(optional)>", value="Get daily weather forecast for a specific location.", inline = False)
        if item == "mc":
            embed.add_field(name="mc <ip:port/host>", value="Get minecraft server status", inline=False)
        if item == "ping":
            embed.add_field(name="ping", value="Get ping value between bot and discord server.", inline=False)
        if item == "qr":
            embed.add_field(name="qr <url>", value="Generate QR code", inline=False)
        if item == "say":
            embed.add_field(name="say <message>", value="Let the bot say something!", inline=False)
        if item == "status":
            embed.add_field(name="status", value="Get bot server status.", inline=False)
        if item == "weather":
            embed.add_field(name="weather <location(optional)>", value="Get current weather information for a specific location.", inline=False)
        elif item not in xlist:
            embed.add_field(name="Command Doesn't exist", value=f"{item} is not a valid command", inline=False)
        embed.set_footer(text="Bot prefix: 0")
        await ctx.send(embed=embed)


def setup(bot):
    bot.add_cog(Help(bot))
