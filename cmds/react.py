import discord
import json
from discord.ext import commands
from core.classes import Cog_Extension
with open('setting.json', mode='r', encoding='utf8') as jfile:
    jdata = json.load(jfile)

class React(Cog_Extension):
    @commands.Cog.listener()
    async def on_message(self, msg):
        if "wau" in msg.content and msg.author != self.bot.user:
            if msg.author.bot:
                pass
            else:
                await msg.channel.send('wau撚夠未')
        if msg.content == "Hi" and msg.author != self.bot.user:
            if msg.author.bot:
                pass
            else:
                await msg.channel.send('Hi')
        if msg.content == "hi" and msg.author != self.bot.user:
            if msg.author.bot:
                pass
            else:
                await msg.channel.send('hi')


def setup(bot):
    bot.add_cog(React(bot))
