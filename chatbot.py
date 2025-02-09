import discord
from discord.ext import commands
import random

TOKEN = 'token'

intents = discord.Intents.default()
intents.message_content = True
bot = commands.Bot(command_prefix='!',intents=intents)


@bot.event
async def on_ready():
    print(f'{bot.user} ha iniciado sesión')

@bot.command(name='cambio_climatico')
async def cambio_climatico(ctx):
    embed = discord.Embed(title='Cambio Climático', description='El cambio climático es el aumento de la temperatura promedio de la Tierra debido a la acumulación de gases de efecto invernadero en la atmósfera.', color=0x00ff00)
    embed.add_field(name='Causas', value='* Quema de combustibles fósiles * Deforestación * Agricultura intensiva', inline=False)
    embed.add_field(name='Efectos', value='* Aumento del nivel del mar * Cambios en los patrones climáticos * Pérdida de biodiversidad', inline=False)
    await ctx.send(embed=embed)

@bot.command(name='consejos')
async def consejos(ctx):
    embed = discord.Embed(title='Consejos para reducir el impacto ambiental', description='Aquí te dejo algunos consejos para reducir tu impacto ambiental:', color=0x00ff00)
    embed.add_field(name='1. Reduce el uso de plásticos', value='Evita el uso de bolsas de plástico y botellas de plástico.', inline=False)
    embed.add_field(name='2. Ahorra energía', value='Apaga las luces y los electrodomésticos cuando no estén en uso.', inline=False)
    embed.add_field(name='3. Utiliza transporte sostenible', value='Utiliza bicicletas o transporte público en lugar de coches.', inline=False)
    await ctx.send(embed=embed)

@bot.command(name='datos_curiosos')
async def datos_curiosos(ctx):
    datos = [
        'El cambio climático es responsable de la pérdida de 200.000 especies de plantas y animales cada año.',
        'La quema de combustibles fósiles es responsable del 65% de las emisiones de gases de efecto invernadero.',
        'El nivel del mar ha aumentado 15-20 cm desde 1900.',
    ]
    embed = discord.Embed(title='Datos curiosos sobre el cambio climático', description='Aquí te dejo algunos datos curiosos sobre el cambio climático:', color=0x00ff00)
    for dato in datos:
        embed.add_field(name=' ', value=dato, inline=False)
    await ctx.send(embed=embed)

@bot.command(name='ayuda')
async def ayuda(ctx):
    embed = discord.Embed(title='¿Cómo puedo ayudar a combatir el cambio climático?', description='Aquí te dejo algunas formas en que puedes ayudar a combatir el cambio climático:', color=0x00ff00)
    embed.add_field(name='1. Reduce tu huella de carbono', value='Reduce tu consumo de energía y agua, y utiliza transporte sostenible.', inline=False)
    embed.add_field(name='2. Apoya a organizaciones ambientales', value='Apoya a organizaciones que trabajan para proteger el medio ambiente y combatir el cambio climático.', inline=False)
    embed.add_field(name='3. Educa a otros', value='Educa a otros sobre el cambio climático y cómo pueden ayudar a combatirlo.', inline=False)
    await ctx.send(embed=embed)

bot.run(token)
