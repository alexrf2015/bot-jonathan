import discord
from discord.ext import commands
permisos = discord.Intents.default()
permisos.message_content =  True
jonathan = commands.Bot(command_prefix="/",intents=permisos)
@jonathan.event
async def on_ready():
    print ("iniciado")
@jonathan.command()
async def hola(ctx):
    await ctx.send("viendenido como estas")
@jonathan.command()
async def meme1(ctx):
    imagen = open("prueba\imagenes\m1.jpeg","rb")
    await ctx.send(file=discord.File(imagen,"meme.jpeg"))
    imagen.close()
@jonathan.command()
async def meme2(ctx):
    imagen = open("prueba\imagenes\m2.jpeg","rb")
    await ctx.send(file=discord.File(imagen,"meme.jpeg"))
    imagen.close()
@jonathan.command()
async def meme3(ctx):
    imagen = open("prueba\imagenes\m3.jpeg","rb")
    await ctx.send(file=discord.File(imagen,"meme.jpeg"))
    imagen.close()
    
jonathan.run()
