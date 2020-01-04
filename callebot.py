import discord, random, string
from asyncio import sleep
from discord.ext import commands
import botlib.info as info
from discord import Game
from discord.utils import get
from colorama import init, Fore, Back, Style

init(autoreset=True)

client = discord.Client()

botToken = info.getBotId()
botToken = botToken[0]

firstname   = info.setUser("firstname")
lastname    = info.setUser("lastname")
discordTag  = info.setUser("discord")

with open("count", "a"):
    pass
with open("count", "r") as init:
    global ingenjörCount
    ingenjörCount = init.read()
    if ingenjörCount == "":
        ingenjörCount = 0

async def getUserFName(userId):
    pos = discordTag.index(str(userId))
    return firstname[pos]
    
async def find_channel(guild):
    for c in guild.text_channels:
        if not c.permissions_for(guild.me).send_messages:
            continue
        return c
       
@client.event
async def on_ready():
    print(f"Logged in as:\t{Fore.MAGENTA}{Style.BRIGHT}{client.user}{Fore.RESET}.")
    await client.change_presence(activity=Game(name=f"with {ingenjörCount} ingenjörer."))

@client.event
async def on_message(message):
    if message.author == client.user:
        return
        
    async def sendMessage(messagelist, istyping=True, channel=message.channel):
        print(f"{Style.BRIGHT}{Fore.GREEN}{message.author}{Style.RESET_ALL}:\t{message.content}")
        for messages in messagelist:
            if istyping == True:
                async with message.channel.typing():
                    await sleep(random.randint(2,5))
            await channel.send(messages)
            print(f"{Fore.MAGENTA}{Style.BRIGHT}{client.user}{Style.RESET_ALL}:\t{messages}")   


    if message.content == ('Calle, hjälp!'):
        messagelist = [
        '+ingenjörer',
        'Calle, ingenjör count',
        'Calle, vem bestämmer?',
        'Trim!',
        'Calle, vad gör en mus bra?',
        'Calle, vad är vi?']
        await sendMessage(messagelist, istyping=False)

    if message.content == ('Calle, vad är vi?'):
        messagelist = ['Vi är ingenjörer.', 'OCH INGENJÖRER LÖSER PROBLEM!']    
        await sendMessage(messagelist)
    
    if message.content == ('Calle, vad gör en mus bra?'):
        messagelist = ['Den där, runda..', 'knappen?.', 'Den ska ha en såndär rund knapp i mitten.',':)']    
        await sendMessage(messagelist)
        
    if message.content == ('Trim!') and str(message.author) != discordTag[1]:
        messagelist = ['Ja, trim!']    
        await sendMessage(messagelist)
    
    if message.content == ("+ingenjörer"):
        global ingenjörCount
        ingenjörCount = int(ingenjörCount)
        ingenjörCount+=1
        messagelist = [f"Ingenjörer: {str(ingenjörCount)}"]
        await sendMessage(messagelist)
        with open("count", "w") as file:
            file.write(str(ingenjörCount))
        await client.change_presence(activity=Game(name=f"with {ingenjörCount} ingenjörer."))
    
    if message.content == ('Calle, ingenjör count'):
        messagelist = [f'Jag har sagt ingenjörer {ingenjörCount} gånger.', 'OCH INGENJÖRER LÖSER PROBLEM!']    
        await sendMessage(messagelist)
    
    if message.content == ('Calle, vem bestämmer?'):

        name = await getUserFName(message.author)

        messagelist = [f'Alla utom {name}.']    
        await sendMessage(messagelist)

@client.event
async def on_member_join(member):
    channel = await find_channel(member.guild)
    await channel.send(f"@everyone Welcom da cannibal: **{member}**.")
    print(f"{Fore.MAGENTA}{Style.BRIGHT}{member}{Style.RESET_ALL}\t{Fore.GREEN}joined{Style.RESET_ALL} the guild.")
    
@client.event
async def on_member_remove(member):
    channel = await find_channel(member.guild)
    await channel.send(f"@everyone Goodbye to the cannibal: **{member}**.")
    print(f"{Fore.MAGENTA}{Style.BRIGHT}{member}{Style.RESET_ALL}\t{Fore.RED}left{Style.RESET_ALL} the guild.")


client.run(botToken)
