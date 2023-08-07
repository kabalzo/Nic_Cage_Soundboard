#This is my Nic Cage bot
#<:AlexBird:920135756201213953>
#<:AdolfBergquist:920135114409791578>

import random
from playsound import playsound
import discord
import os
from dotenv import load_dotenv

load_dotenv()

TOKEN = os.getenv("DISCORD_TOKEN")

def cageClips(): 
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
    clip = random.randint(0, len(cage_clips)-1)
    #print(clip)
    myClip = cage_clips[clip]
    print(myClip[0])
    #playsound('sounds/' + cage_clips[clip][1])
    return myClip

client = discord.Client(intents=discord.Intents.default())
@client.event
async def on_ready():
    print('We have logged in as {0.user}'.format(client))

@client.event
async def on_message(message):
    test_comm = "!test"
    speakComm = "!speak"
    helpComm = "!help"
    trevorComm = "!trevor"
    alexComm = "!alex"
    gifComm = "!gif"

    if message.author == client.user:
        print("Debug 2")
        return

    if speakComm in message.content:
        #print(type(message.content))
        print("Debug 3")
        cageClipForDiscord = cageClips()
        await message.channel.send(cageClipForDiscord[0])
        playsound('sounds/' + cageClipForDiscord[1])
        #print(message.channel)

    #All the commands  go in here#
    if helpComm in message.content:
        await message.channel.send("Use @ towards me and I'll respond. Commands: !speak, !help, !alex, !gif")

    if trevorComm in message.content:
        await message.channel.send("Trevor sucks")

    if alexComm in message.content:
        alex = ["<:AdolfBergquist:920135114409791578>", "<:AlexBird:920135756201213953>"]
        r = random.randint(0,1)
        await message.channel.send(alex[r])

    if gifComm in message.content:
        r = random.randint(0,3)
        gifs = ["https://tenor.com/view/nicholas-cage-you-pointing-smoke-gif-14538102",
                "https://tenor.com/view/nicolas-cage-the-rock-smile-windy-handsome-gif-15812740",
                "https://tenor.com/view/woo-nick-cage-nicolas-cage-the-unbearable-weight-of-massive-talent-lets-go-gif-25135470",
                "https://tenor.com/view/national-treasure-benjamin-gates-nicolas-cage-declaration-of-independence-steal-gif-4752081"
                ]
        await message.channel.send(gifs[r])

    if test_comm in message.content:
        await message.channel.send("I'm gonna steal the Declaration of Independence")
        await message.channel.send("https://tenor.com/view/national-treasure-benjamin-gates-nicolas-cage-declaration-of-independence-steal-gif-4752081")








client.run(TOKEN)



