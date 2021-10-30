# Import modules
import requests
import json
import discord
from discord.ext import commands
from core.classes import Cog_Extension

with open('setting.json',mode='r',encoding='utf8') as jfile:
    jdata = json.load(jfile)
    
# API key 
api = jdata["weatherApiKey"]


class Weather(Cog_Extension):
    
    @commands.command()
    async def weather(self, ctx, location="Hong Kong"):
        # url
        url = "http://api.openweathermap.org/data/2.5/"
        
        #  Finish url
        f_url = f"{url}weather?appid={api}&q={location}" 
  
        # Get and return response
        response = requests.get(f_url) 
        
        # Transfer json to python object
        x = response.json() 
        
        # If not city not found
        if x["cod"] != "404": 
            
            # Get city name
            city = x["name"]
            # Get temperture in kelvin
            temp_k = x["main"]["temp"] 
            #convert kelvin to celsius
            temp_c = temp_k - 273.15
            #get rid of the decimals
            temp = round(temp_c)
            
            # Get air pressure
            pressure = x["main"]["pressure"] 
            
            # Get huminity
            humidity = x["main"]["humidity"] 
            
            # Get description
            description = x["weather"][0]["description"]
            
            #generate discord embed
            embed=discord.Embed(title="Weather", description=f"Location:{city}", color=0x00ff00)
            embed.add_field(name="Description", value=f"{description}", inline=False)
            embed.add_field(name="Temperature", value=f"{temp}°C", inline=False)
            embed.add_field(name="Atmospheric pressure", value=f"{pressure} hPa", inline=False)
            embed.add_field(name="Humidity", value=f"{humidity}%", inline=False)
            embed.set_footer(text="Data source: OpenWeather")
        else:
            #generate error discord embed
            embed=discord.Embed(title="Location not found", description=f"{location} not found", color=0xff0000)
        
        #send embed
        await ctx.send(embed=embed)
        
    @commands.command()
    async def forecast(self, ctx, location="hong kong"):
        # url
        url = "http://api.openweathermap.org/data/2.5/weather?"
        #  Finish url
        f_url = f"{url}appid={api}&q={location}" 
          
        # Get and return response
        response = requests.get(f_url) 
          
        # Transfer json to python object
        x = response.json()
        
        # If not city not found
        if x["cod"] != "404": 
             
            # Get city name
            city = x["name"]
            
            # Get weather description
            description = x["weather"][0]["description"]
            
            # Get highest temp
            maxtemp_k = x["main"]["temp_max"]
            maxtemp_c = maxtemp_k - 273.15
            maxtemp = round(maxtemp_c)
            
            # Get lowest temp
            mintemp_k = x["main"]["temp_min"]
            mintemp_c = mintemp_k - 273.15
            mintemp = round(mintemp_c)

            #generate discord embed
            embed=discord.Embed(title="Weather", description=f"Location:{city}", color=0x00ff00)
            embed.add_field(name="Description", value=f"{description}", inline=False)
            embed.add_field(name="Higherst Temperature", value=f"{maxtemp}°C", inline=False)
            embed.add_field(name="Lowest Temperature", value=f"{mintemp}°C", inline=False)
            embed.set_footer(text="Data source: OpenWeather")
        else:
            #generate error discord embed
            embed=discord.Embed(title="Location not found", description=f"{location} not found", color=0xff0000)
        
        #send embed
        await ctx.send(embed=embed)
        
def setup(bot):
    bot.add_cog(Weather(bot))
