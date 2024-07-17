import discord
from Packages import Botloader
import asyncio
from discord.ext import commands
from discord.ext.commands import Context

class Owner(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
        Owner.app_command.deleter

    @commands.command(name="off")
    async def off(self, ctx: Context):
        if not Botloader.owner_permission.check(ctx.author.id):
            return
        await ctx.send("Bot was offline.")
        await asyncio.sleep(3)
        print("")
        Botloader.Bot.console("INFO", f'Bot Closed')
        print("")
        await self.bot.close()
        
    @commands.command(name="invits")
    async def invits(self, ctx: Context):
        if not Botloader.owner_permission.check(ctx.author.id):
            return
        for guild in self.bot.guilds:
            try:
                invite = await guild.text_channels[0].create_invite(max_uses=1, unique=True)
                await ctx.send(f'Invitation pour le serveur {guild.name}: {invite.url}')
            except discord.Forbidden:
                 print(f"Le bot n'a pas les permissions nécessaires pour créer une invitation dans le serveur {guild.name}")