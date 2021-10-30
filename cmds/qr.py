import discord
from discord.ext import commands
import pyqrcode
import png
from pyqrcode import QRCode
from core.classes import Cog_Extension

class QR(Cog_Extension):

    @commands.command()
    async def qr(self, ctx, website):
        url = pyqrcode.create(website)
        url.png('qr.png', scale = 6)
        await ctx.send(file=discord.File("qr.png"))
        print(f"{ctx.message.author} generated qr code. url={website}")

def setup(bot):
    bot.add_cog(QR(bot))