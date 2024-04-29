#This is my Nic Cage bot
import random
import time
import discord
from discord.ext import commands
import os
from dotenv import load_dotenv
import os

#Bot Testing
#getID = 1199174850955194428
        
#bot-testing
#sendID = 1198772106305998919
    
#bestvid-of-the-week
getID = 1074298607454400563
        
#oracle-room
sendID = 381974064891428868

#For use with start/stop.sh files instead of starting via shell
pid = os.getpid()
f = open("pid", "w")
f.write(str(pid))
f.close()

load_dotenv()
TOKEN = os.getenv("DISCORD_TOKEN")

intents = discord.Intents.all()
bot = commands.Bot(command_prefix='!', intents=intents)
intents.message_content = True
lastInt = -1

#This is where the quotes and references to the sound clips live
f = open("quotes.txt", "r")
NicCageQuotes = f.readlines()
f.seek(0)
f.close()

#TOOD: change this
gifs = [
        "https://tenor.com/view/nicholas-cage-you-pointing-smoke-gif-14538102",
        "https://tenor.com/view/nicolas-cage-the-rock-smile-windy-handsome-gif-15812740",
        "https://tenor.com/view/woo-nick-cage-nicolas-cage-the-unbearable-weight-of-massive-talent-lets-go-gif-25135470",
        "https://tenor.com/view/national-treasure-benjamin-gates-nicolas-cage-declaration-of-independence-steal-gif-4752081"
        ]
################################################################################################################################################
#Play a random clip each time !speak is called
def getRandomInt():
     i = random.randint(0, len(NicCageQuotes)-1)
     return i
################################################################################################################################################
@bot.event
async def on_ready(channel=None):
    print("User name: " + bot.user.name)
    print("User id: " + str(bot.user.id))
    print('We have logged in as {0.user}\n'.format(bot))
    
    f = open("links.txt", "w")
    f.write("")
    f.seek(0)
    f.close()
    # Check if channel argument is empty
    if channel is None:
        # if yes, use channel from the command
        #channel = ctx.channel
        channel = bot.get_channel(getID)
    
    async for message in channel.history(limit=None):
        # Check if message has content
        if (message.content is not None and message.content.startswith("https")):
            if (message.content == "Link history has been logged"):
                pass
            else:
                f = open("links.txt", "a")
                # Add message content to list
                #print(f'{message.content} - {message.created_at}')
                f.write(message.content+"\n")
                f.seek(0)
                f.close()
            
    print("Link history has been logged")
################################################################################################################################################
@bot.event
async def on_message(ctx):
    if (ctx.content.startswith("!")):
        pass
    else:
        sendTo = bot.get_channel(sendID)
        newLink = ctx.content
        try:
            if (ctx.channel.id == getID): 
                #print(f'Message from {ctx.author} with  channel ID {ctx.channel.id}: {newLink}')
                f = open("links.txt", "r")
                myLinks = f.readlines()
                f.seek(0)
                f.close()
                for link in myLinks:
                    link = link.strip("\n")
                    #print(link)
                    if (link == newLink):
                        #print(f'{newLink} has previously been posted by {ctx.author.id}')
                        await sendTo.send(f'<@{ctx.author.id}> {newLink} has been posted previously')
                        break
                    elif (newLink.startswith("https")):
                        f = open("links.txt", "a")
                        f.write(newLink+"\n")
                        f.seek(0)
                        f.close()
                    else:
                        pass
        except:
            print("Link history not created. Run !log command")
    await bot.process_commands(ctx)
################################################################################################################################################
'''@bot.command()
async def log(ctx, channel=None):
    f = open("links.txt", "w")
    f.write("")
    f.seek(0)
    f.close()
    # Check if channel argument is empty
    if channel is None:
        # if yes, use channel from the command
        #channel = ctx.channel
        channel = bot.get_channel(getID)
    
    async for message in channel.history(limit=None):
        # Check if message has content
        if (message.content is not None and message.content.startswith("https")):
            if (message.content == "Link history has been logged"):
                pass
            else:
                f = open("links.txt", "a")
                # Add message content to list
                print(f'{message.content} - {message.created_at}')
                f.write(message.content+"\n")
                f.seek(0)
                f.close()
            
    print("Link history has been logged")'''
################################################################################################################################################
@bot.command()
async def test(ctx, arg):
    await ctx.send("Test command - CORRECT WAY " + arg)
################################################################################################################################################
@bot.command()
async def speak(ctx):
    global lastInt
    #Prevent the same quote/clip from being played twice in a row
    myRandomInt = getRandomInt()
    while (True):
        if (myRandomInt == lastInt):
            myRandomInt = getRandomInt()
        else:
            lastInt = myRandomInt
            _myQuote = NicCageQuotes[myRandomInt]
            myQuote = _myQuote.split("; ")
            print("Channel Name: " + str(ctx.channel.name) + ", Channel ID: " + str(ctx.channel.id))
            await ctx.channel.send(myQuote[0])
            print('Quote: ' + '\33[32m' + myQuote[0] + '\33[0m')
            try:
                voice = ctx.voice_client.play(discord.FFmpegPCMAudio(str('./sounds/' + myQuote[1].strip())))
            except:
                print('\33[31m' + "No active voice channel" + '\33[0m')
            break
################################################################################################################################################
@bot.command()
async def helpme(ctx):
       await ctx.channel.send("Commands: !join !leave !speak !helpme !gif")
################################################################################################################################################
@bot.command()
async def gif(ctx):
    randomGif = random.randint(0,3)
    await ctx.channel.send(gifs[randomGif])
################################################################################################################################################
@bot.command()
async def join(ctx):
    try:
        voice = await ctx.author.voice.channel.connect()
        await ctx.channel.send("Nic is here to party, woo! (!helpme)")
        voice.play(discord.FFmpegPCMAudio('./sounds/woo.mp3'))
    except:
        print('\33[31m' + "No members active in voice channel" + '\33[0m')
################################################################################################################################################
@bot.command()
async def leave(ctx):
    voice = ctx.voice_client.play(discord.FFmpegPCMAudio('./sounds/silence.mp3'))
    await ctx.channel.send("Hurray for the sounds of fucking silence")
    time.sleep(5)
    voice = await ctx.voice_client.disconnect()
################################################################################################################################################
bot.run(TOKEN)
    


