import discord
from discord.ext import commands



class EventsCog(commands.Cog):
  def __init__(self, bot):
    self.bot = bot

  TRIGGER = ["Quoi", "quoi", "Quoi ?", "quoi ?", "pourquoi ?" , "Pourquoi ?" , "pourquoi" , "Pourquoi"]

  @commands.Cog.listener()
  async def on_message(self, message: discord.Message):
    if message.author.bot:
      return
    for trigger in self.TRIGGER:
      if message.content.lower().endswith(trigger):
        await message.channel.send("Feur")

  @commands.Cog.listener()
  async def on_ready(self):
    print("Le bot est prêt")
    channel = self.bot.get_channel(1186417157173686322)
    if channel:
      await channel.send(f"Yop je suis prêt")

async def setup(bot): 
  await bot.add_cog(EventsCog(bot))
