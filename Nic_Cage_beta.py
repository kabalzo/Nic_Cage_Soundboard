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

NicCageQuotes = [
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
    #print("Channel ID: " + str(ctx.channel.id))
    randomQuote = random.randint(0, len(NicCageQuotes)-1)
    myQuote = NicCageQuotes[randomQuote]
    print(myQuote[0])
    #This block is for selecting a random voice clip to play
    myClip = NicCageQuotes[randomQuote]
    voice = ctx.voice_client.play(discord.FFmpegPCMAudio('./sounds/' + str(myClip[1])))
    await ctx.channel.send(myQuote[0])

@bot.command()
async def helpme(ctx):
       await ctx.channel.send("Commands: !join !leave !speak !helpme !gif")

@bot.command()
async def gif(ctx):
    randomGif = random.randint(0,3)
    await ctx.channel.send(gifs[randomGif])

@bot.command()
async def join(ctx):
    voice = await ctx.author.voice.channel.connect()
    await ctx.channel.send("Nic is here to party, woo! (!helpme)")
    voice.play(discord.FFmpegPCMAudio('./sounds/woo.mp3'))

@bot.command()
async def leave(ctx):
    voice = await ctx.voice_client.disconnect()
    #print(type(voice))     
    await ctx.channel.send("Chao!")

bot.run(TOKEN)
    


