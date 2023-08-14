#This is my Nic Cage bot

import random
#from playsound import playsound
import discord
from discord.ext import commands
import os
from dotenv import load_dotenv
load_dotenv()
TOKEN = os.getenv("DISCORD_TOKEN")

intents = discord.Intents.all()
bot = commands.Bot(command_prefix='!', intents=intents)
intents.message_content = True

cage_clips = [
                ("Not the bees! :bee:", "bees.mp3"),
                ("I'M A VAMPIRE!:man_vampire:I'M A VAMPIRE!:man_vampire:I'M A VAMPIRE!:man_vampire:I'M A VAMPIRE!:man_vampire:I'M A VAMPIRE!:man_vampire:", "vampire.mp3"), 
                ("YOU BITCHES!!! YOU BITCHES!!!", "you_bs.mp3"), 
                ("I'm just relieved that I'm not as crazy as everyone says...", "crazy.wav"),
                ("I said put the bunny back in the box :rabbit:", "bunny.mp3"),
                ("I'm gonna steal the Declaration of Independence", "steal.wav"),
                ("I never disrobe before gunplay", "other.mp3"),
                ("I'll be taking these Huggies and whatever cash you've got", "huggies.mp3"),
                ("You know, I could eat a peach for hours :peach:", "peach.mp3"),
                ("FUUUUUUUUUUUUUUUCCCCCCKKKKK", "fudge.mp3"),
                ("Sorry Boss But There’s Only Two Men I Trust. One of Them’s Me. And The Other’s Not You :airplane:", "con-trust.wav")
            ]

gifs = [
        "https://tenor.com/view/nicholas-cage-you-pointing-smoke-gif-14538102",
        "https://tenor.com/view/nicolas-cage-the-rock-smile-windy-handsome-gif-15812740",
        "https://tenor.com/view/woo-nick-cage-nicolas-cage-the-unbearable-weight-of-massive-talent-lets-go-gif-25135470",
        "https://tenor.com/view/national-treasure-benjamin-gates-nicolas-cage-declaration-of-independence-steal-gif-4752081"
        ]

@bot.event
async def on_ready():
    print("User name: " + bot.user.name)
    print("User id: " + str(bot.user.id))
    print('We have logged in as {0.user}'.format(bot))

@bot.command()
async def test(ctx, arg):
    await ctx.send("Test command - CORRECT WAY " + arg)

@bot.command()
async def speak(ctx):
    print("Channel ID: " + str(ctx.channel.id))
    clip = random.randint(0, len(cage_clips)-1)
    myClip = cage_clips[clip]
    print(myClip[0])
    await ctx.channel.send(myClip[0])

    #playsound('sounds/' + cage_clips[clip][1])
    #playsound('sounds/' + cageClipForDiscord[1])
    #print(message.channel)'''

@bot.command()
async def helpme(ctx):
       await ctx.channel.send("Use @ towards me and I'll respond. Commands: !speak, !help, !alex, !gif")

@bot.command()
async def gif(ctx):
    r = random.randint(0,3)
    await ctx.channel.send(gifs[r])

@bot.command()
async def join(ctx):
    connected = ctx.author.voice
    if connected:
        await connected.channel.connect()

bot.run(TOKEN)



