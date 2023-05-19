import discord
from discord.ext import commands


intents = discord.Intents(messages=True, guilds=True,reactions=True,members=True,presences=True)
Bot = commands.Bot("!uw ",intents=intents)

@Bot.event
async def on_ready():
    print("Spawn başarılı!")

@Bot.event
async def on_member_join(member):
    channel = discord.utils.get(member.guild.text_channels, name="rrrrrrrrrr")
    await channel.send(str(member) + "aramızdan ayrıldı :( .")

@Bot.event
async def on_member_remove(member):
    channel = discord.utils.get(member.guild.text_channels, name="rrrrrrrrrr")
    await channel.send(str(member) + "aramızdan ayrıldı :( .")




@Bot.command()
async def mesajYaz(mesaj):
    await mesaj.send("Emredersiniz! Mesaj yazıldı.")


Bot.run("ODgzNjk3NDY0NjE0NDY5NjUy.YTNtZQ.WP92O_ZyXs32Ck19lhNitPbeFEQ")
