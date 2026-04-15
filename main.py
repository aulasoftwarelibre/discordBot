import discord
from discord.ext import commands
import logging
from dotenv import load_dotenv
import os

load_dotenv()
token = os.getenv('DISCORD_TOKEN')


handler = logging.FileHandler(filename='discord.log', encoding='utf-8', mode='w')

intents = discord.Intents.default()
intents.message_content = True
intents.members = True

bot = commands.Bot(command_prefix='!', intents=intents)

@bot.event
async def on_ready():
    print(f"Tamos ready")

@bot.event
async def on_member_join(member):
    #Por privado lo envia
    await member.send(f"Bienvenido {member.name}")

@bot.event
async def on_message(message):
    if message.author == bot.user:
        return
    
    if message.content.lower() == "como estamos?":
        await message.channel.send(f"{message.author.mention} estoy bakano gracias")

    await bot.process_commands(message)

@bot.command()
async def hello(ctx):
    await ctx.send(f"Hello {ctx.author.name}!!")

@bot.hybrid_command(name="hate", description=f"Muestra amor por Microsoft")
async def hate(ctx):
    await ctx.send("Microsoft!!\n" + "Mu malo\n"*4)

@bot.command()
async def assign(ctx):
    role = discord.utils.get(ctx.guild.roles, name="prueba")
    if role:
        await ctx.author.add_roles(role)
        await ctx.message.add_reaction("✅")

@bot.command()
async def unassign(ctx):
    role = discord.utils.get(ctx.guild.roles, name="prueba")
    if role:
        await ctx.author.remove_roles(role)
        await ctx.message.add_reaction("✅")

@bot.command()
async def poll(ctx, *,question):
    embed = discord.Embed(title="New Poll",description=question, color=discord.Colour.green())
    poll_message = await ctx.send(embed=embed)
    await poll_message.add_reaction("👎")
    await poll_message.add_reaction("👍")
    


bot.run(token, log_handler=handler, log_level=logging.DEBUG)