import discord
import random
from GenPass import gen_pass
import time
meme_img = discord.File(r"C:\Users\talit\OneDrive\Escritorio\ya no tengo nombres para las carpetas XD\meme.png","meme de amogus.png")
puntos = discord.File(r"C:\Users\talit\OneDrive\Escritorio\ya no tengo nombres para las carpetas XD\puntos.png","´puntos.png")
oceano_contaminado = discord.File(r"C:\Users\talit\OneDrive\Escritorio\ya no tengo nombres para las carpetas XD\isla-basura-pacifico.png","oceano_contaminado.png")
botellas = discord.File(r"C:\Users\talit\OneDrive\Escritorio\ya no tengo nombres para las carpetas XD\botellas.png","botellas.png")



# La variable intents almacena los privilegios del bot
intents = discord.Intents.default()
# Activar el privilegio de lectura de mensajes
intents.message_content = True
# Crear un bot en la variable cliente y transferirle los privilegios
client = discord.Client(intents=intents)

@client.event
async def on_ready():
    print(f'Hemos iniciado sesión como {client.user}')

@client.event
async def on_message(message):
    if message.author == client.user:
        return
    if message.content.startswith('/hola bot'):
        await message.channel.send("Hola!, Listo para combatir la contaminacion?")
    elif message.content.startswith('/bot problemas del oceano contaminado'):
        await message.channel.send(file = oceano_contaminado)
        await message.channel.send("El oceano esta en graves problemas!,Necesitamos ayudarlo reciclando la basura :)")
    elif message.content.startswith('/bot como reciclar la basura?'):
        await message.channel.send(file = botellas)
        await message.channel.send("puedes empezar reciclando con un par de botellas:D")
    elif message.content.startswith('/bot que beneficios me da reciclar?'):
        await message.channel.send(file = puntos)
        await message.channel.send("por ayudar al oceano obtienes puntos llamados oceapuntos que pueden ser cambiados por tarjetas de regalos de diferentes marcas:O")
        

    # elif message.content.startswith('generame una contraseña aleatoria'):
    #     await message.channel.send(gen_pass(int(message.content[12:])))



client.run("tu codigo de bot")
