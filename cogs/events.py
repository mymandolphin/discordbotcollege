import discord
import asyncio
import typing
from discord.ext import commands
from main import get_prefix



class Events(commands.Cog):

    def __init__(self,bot):
        self.bot = bot

    @commands.Cog.listener()
    async def on_message(self,ctx: typing.Union[discord.User, str]):

        if ctx.author == self.bot.user:

            return

        mentionbot = f'<@!{self.bot.user.id}>'

        if ctx.content.startswith(mentionbot):

            embed = discord.Embed(

                title="The command prefix for this server is:",
                description=f'`{get_prefix(self.bot, ctx)}`',
                colour=0x33e18d

            )

            await ctx.channel.send(embed= embed)


def setup(bot):
    bot.add_cog(Events(bot))