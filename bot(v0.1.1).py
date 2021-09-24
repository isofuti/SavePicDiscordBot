import discord
from discord import client
from discord import message
from discord import channel
from discord.ext import commands

pathsave = "path\\to\\save\\"
myear = "m-year"# month and year - the period for which you need to download the pictures


bot = discord.Client()
@bot.event
async def check():
    print('Logged in as')
    print(bot.user.name)
    print(bot.user.id)
    print('------')

    channel = bot.get_channel(id)#id of the channel from which you want to download pictures

    messages = await channel.history(limit=10).flatten()# limit - the number of messages that are viewed

    # reversing because discord sends only data first
    messages.reverse()

    for ch in messages:
        tods = ch.created_at
        my = str(tods.month) + "-" + str(tods.year)
        if my == myear:
            print('check')
            att = ch.attachments
            todss = ch.created_at
            print(att)
            my = str(todss.month) + "-" + str(todss.year)
            print(todss.year, todss.month)
            for attach in ch.attachments:
                await attach.save(pathsave + myear + "-" + str(ch.id) + ".png")#file formatting

bot.run('token')