import discord
from discord.ext import commands
import json
import os
import datetime
import asyncio
import tasks

with open('./setting.json',mode='r',encoding='utf8') as jfile:
    jdata = json.load(jfile)

bot = commands.Bot(command_prefix='na', help_command = None)

async def status_task():
    while True:
        await bot.change_presence(status=discord.Status.online, activity=discord.Game("</> with :heart: by @AdrianL24228638"))
        await asyncio.sleep(10)
        await bot.change_presence(status=discord.Status.online, activity=discord.Game("0help for help!"))
        await asyncio.sleep(10)

@bot.event
async def on_ready():
    bot.loop.create_task(status_task())
    date_time = datetime.datetime.now()
    time = date_time.strftime("%Y-%m-%d %H:%M:%S")
    print(f"[INFO] System Time: {time}")
    print(f"[INFO] Logged in as {bot.user}")
    print(">>Bot is online<<")

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
