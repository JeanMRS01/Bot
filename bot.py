import discord
from discord.ext import commands
import requests
import pyttsx3

intents = discord.Intents.default()
intents.message_content = True

def talk(text):
    engine = pyttsx3.init()  # object creation
    rate = engine.getProperty("rate")  # getting details of current speaking rate
    engine.setProperty("rate", 200)  # setting up new voice rat
    volume = engine.getProperty("volume")  # getting to know current volume level (min=0 and max=1)
    engine.setProperty("volume", 1.0)  # setting up volume level  between 0 and 
    voices = engine.getProperty("voices")  # getting details of current voice
    engine.setProperty("voice", voices[1].id)  # changing index, changes voices. 1 for female
    pitch = engine.getProperty("pitch")  # Get current pitch value
    engine.setProperty("pitch", 75)  # Set the pitch (default 50) to 75 out of 100
    engine.say(text)
    engine.runAndWait()

bot = commands.Bot(command_prefix = "/", intents = intents)

@bot.command()
async def hello(ctx):
    await ctx.send("Hello")
    talk("hello")

def obtener_clima(ciudad: str) -> str:
    url = f"https://wttr.in/{ciudad}?format=%C+%t&lang=es"
    respuesta = requests.get(url)

    if respuesta.status_code == 200:
        return respuesta.text.strip()
    else:
        return "No nos conectamos con la API"
    
def obtener_dato():
    url = f"https://uselessfacts.jsph.pl/api/v2/facts/random"
    ar = requests.get(url)

    if ar.status_code == 200:
        return ar.json().get("text", "No se pudo obtener el texto")
    else:
        return "No nos conectamos con la API"
    
@bot.command()
async def clima(ctx, *, ciudad:str):
    prediccion = obtener_clima(ciudad)
    await ctx.send(f"The climate in {ciudad} is {prediccion}")
    talk(f"The climate in {ciudad} is {prediccion}")

@bot.command()
async def dato(ctx):
    dr = obtener_dato()
    await ctx.send(f"{dr}")
    talk(f"{dr}")


@bot.command()
async def bye (ctx):
    await ctx.send("Bye")
    talk("bye")

bot.run("TOKEN")