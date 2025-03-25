
import random
from discord.ext import commands
import asyncio

class CommandsCog(commands.Cog):
  def __init__(self, bot):
    self.bot = bot  
  #---------------------------MATH-----------------------------------
  @commands.hybrid_command()
  async def soustraire(self, ctx, a: int, b: int):
    await ctx.send(f"La différence entre {a} et {b} est {a - b}")

  @commands.hybrid_command()
  async def multiplication(self, ctx, a: int, b: int):
    await ctx.send(f"Le produit entre {a} et {b} est {a * b}")

  @commands.hybrid_command()
  async def somme(self, ctx, a: int, b: int):
    await ctx.send(f"La somme entre {a} et {b} est {a + b}")
  #---------------------------------------------------------------
  @commands.hybrid_command()
  async def note(self, ctx, *, note: str):
    await ctx.send(f"Note : {note} enregistrée !")

  @commands.hybrid_command()
  async def ping(self, ctx):
    await ctx.send("Pong !")

  @commands.hybrid_command()
  async def jet(self, ctx, lancer: int, des: int, mod: int):
      total = 0
      for i in range(lancer):
        roll = random.randint(1, des)
        total += roll
      result= total + mod
      await ctx.send(f'Résulat obtenu : {result}')

  @commands.hybrid_command()
  async def stop(self, ctx):
    await ctx.send("Je retourne me coucher Zzzz!")
    await self.bot.close()


  @commands.Cog.listener()
  async def on_ready(self):
    await self.bot.tree.sync()

async def setup(bot):
    await bot.add_cog(CommandsCog(bot))
