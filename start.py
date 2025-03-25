import os
import discord
from discord.ext import commands
from dotenv import load_dotenv

load_dotenv()

token = os.getenv('DISCORD_TOKEN')

if not token:
    raise ValueError("Le token n'a pas été trouvé dans les variables d'environnement.")

class LordBot(commands.Bot):
  async def setup_hook(self):
    for extension in ["commandes", "events",]:
        try:
            await self.load_extension(f'cogs.{extension}')
        except Exception as e:
              print(f"Erreur lors du chargement de l'extension {extension}: {e}")


intents = discord.Intents.all()
bot = LordBot(command_prefix='&', intents=intents)

bot.run(token)
