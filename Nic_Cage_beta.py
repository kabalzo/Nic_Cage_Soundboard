#This is my Nic Cage bot

import random
from playsound import playsound
import discord
import os
from dotenv import load_dotenv

load_dotenv()

TOKEN = os.getenv("DISCORD_TOKEN")

def cageQuote(): 
    cage_quotes = [
                   ("Not the bees! :bee:", "bees.mp3"),
                   ("I'M A VAMPIRE!:man_vampire:I'M A VAMPIRE!:man_vampire:I'M A VAMPIRE!:man_vampire:I'M A VAMPIRE!:man_vampire:I'M A VAMPIRE!:man_vampire:", "vampire.mp3"), 
                   ("YOU BITCHES!!! YOU BITCHES!!!", "you_bs.mp3"), 
                   ("I'm just relieved that I'm not as crazy as everyone says...", "crazy.wav"),
                   ("I said put the bunny back in the box :rabbit:", "placeholder"),
                   ("I'm gonna steal the Declaration of Independence", "placeholder"),
                   ("I never disrobe before gunplay", "placeholder"),
                   ("I'll be taking these Huggies and whatever cash you've got", "placeholder"),
                   ("You know, I could eat a peach for hours :peach:", "placeholder"),
                   ("Lets ride :skull_crossbones: :motorcycle:", "placeholder"),
                   ("Sorry Boss But There’s Only Two Men I Trust. One of Them’s Me. And The Other’s Not You :airplane:", "placeholder"),
                   (":FaceoffCage:", "")
                  ]
    quote = random.randint(0, len(cage_quotes)-1)
    #print(quote)
    myQuote = cage_quotes[quote][0]
    print(myQuote)
    #playsound('sounds/' + cage_quotes[quote][1])
    return myQuote

client = discord.Client(intents=discord.Intents.default())
@client.event
async def on_ready():
    print('We have logged in as {0.user}'.format(client))

@client.event
async def on_message(message):
    speakComm = "!speak"
    helpComm = "!help"
    trevorComm = "!trevor"
    alexComm = "!alex"
    if message.author == client.user:
        print("Debug 2")
        return

    if speakComm in message.content:
        #print(type(message.content))
        print("Debug 3")
        cageQuoteForDiscord = cageQuote()
        await message.channel.send(cageQuoteForDiscord)
        #print(message.channel)

    if helpComm in message.content:
        await message.channel.send("Use @ towards me and I'll respond. Commands: !speak, !help, !trevor, !alex")

    if trevorComm in message.content:
        await message.channel.send("Trevor sucks")

    if alexComm in message.content:
        await message.channel.send(":AdolfBergquist:")


client.run(TOKEN)



