import discord
from discord.ext import commands
import json
import os
import datetime
import asyncio
import tasks

with open('./setting.json',mode='r',encoding='utf8') as jfile:
    jdata = json.load(jfile)
    
with open('./guild.json',mode='r+',encoding='utf8') as gfile:
    gdata = json.load(gfile)
    


bot = commands.Bot(command_prefix='2', help_command = None)

async def status_task():
    while True:
        await bot.change_presence(status=discord.Status.online, activity=discord.Game("</> with ❤ by @AdrianL24228638"))
        await asyncio.sleep(10)
        await bot.change_presence(status=discord.Status.online, activity=discord.Game("2help for help!"))
        await asyncio.sleep(10)

@bot.event
async def on_ready():
    bot.loop.create_task(status_task())
    date_time = datetime.datetime.now()
    time = date_time.strftime("%Y-%m-%d %H:%M:%S")
    print(f"[INFO] System Time: {time}")
    print(f"[INFO] Logged in as {bot.user}")
    print(">>Bot is online<<")

@bot.event
async def on_guild_join(guild):
    for channel in guild.text_channels:
        if "general" in channel.name and channel.permissions_for(guild.me).send_messages:
            await channel.send('Hey there! Thank you for using Tairitsu 2.0.\nMy source code is on Github Adrian400811/Discord-Bot-2.0.')
            entry = {f"{guild.id}": {"name": f"{guild.name}", "mainChannel": f"{channel}"}}
        else:
            entry = {f"{guild.id}": {"name": f"{guild.name}", "mainChannel": None}}
    gdata.append(entry)
    gfile.seek(0)
    json.dump(gdata, gfile)

@bot.command(hidden=True)
@commands.is_owner()
async def load (ctx, extension):
    bot.load_extension(f'cmds.{extension}')
    await ctx.send(f'Loaded {extension}')

@bot.command(hidden=True)
@commands.is_owner()
async def unload (ctx, extension):
    bot.unload_extension(f'cmds.{extension}')
    await ctx.send(f'unloaded {extension}')

@bot.command(hidden=True)
@commands.is_owner()
async def reload (ctx, extension):
    bot.reload_extension(f'cmds.{extension}')
    await ctx.send(f'reloaded {extension}')

for filename in os.listdir('./cmds'):
    if filename.endswith('.py'):
        bot.load_extension(f'cmds.{filename[:-3]}')

bot.run(jdata['TOKEN'])
