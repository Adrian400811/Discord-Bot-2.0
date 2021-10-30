import discord
from discord.ext import commands
from core.classes import Cog_Extension
import os
import platform
import socket

class Ping(Cog_Extension):  

    @commands.command()
    async def ping(self, ctx, target="Discord"):
        if target == "Discord":
            ms = round(self.bot.latency*1000)
        else:
            try:
                ip = socket.gethostbyname(target)
                ping = os.popen(f'ping {target} -c 1')
                result = ping.readlines()
                msLine = result[-1].strip()
                msres = (msLine.split(' = ')[-1])
                ms = (msres.split('/')[1])
            except:
                ip = "N/A"
                serverStatus = "Offline"
                ms = "N/A"
                color = 0xFF0000
                foot = 'Error. Did you type something like ".com" after domain name?'
            else:
                serverStatus = "Online"
                color = 0x00FF00
                foot = "Success"
        embed=discord.Embed(title="Ping", description=f"Target: {ip}", color=color)
        embed.add_field(name="Status", value=f"{serverStatus}", inline=False)
        embed.add_field(name="Latency:", value=f"{ms} ms", inline=False)
        embed.set_footer(text=foot)
        await ctx.send(embed=embed)
        

def setup(bot):
    bot.add_cog(Ping(bot))