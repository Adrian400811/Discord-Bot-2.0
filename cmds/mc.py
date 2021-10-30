import discord
from discord.ext import commands
from mcstatus import MinecraftServer
from core.classes import Cog_Extension

class mc(Cog_Extension):

    @commands.command()
    async def mc(self, ctx, host):
        try:
            server = MinecraftServer.lookup(host)
            status = server.status()
            ponline = status.players.online
            pmax = status.players.max
            ping = status.latency
            version = status.version.name
            des = status.description["text"]
            
        
        except:
            embed=discord.Embed(title="Minecraft Server Status", description=f"{host}", color=0xff0000)
            embed.add_field(name="Server time out", value=f"The server didn't response. Are you sure {host} is the correct address?", inline=False)
            embed.set_footer(text="err=timeout")
            await ctx.send(embed=embed)
            
        else:
            embed=discord.Embed(title="Minecraft Server Status", description=f"online", color=0x00ff00)
            embed.add_field(name="Description", value=f"{des}", inline=False)
            embed.add_field(name="Version", value=f"{version}", inline=False)
            embed.add_field(name="players", value=f"{ponline}/{pmax}", inline=False)
            embed.add_field(name="Latency", value=f"{ping}ms", inline=False)
            embed.set_footer(text=f"host: {host}")
            await ctx.send(embed=embed)

def setup(bot):
    bot.add_cog(mc(bot))