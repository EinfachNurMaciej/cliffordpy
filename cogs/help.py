import discord
from discord.ext import commands
import asyncio
import datetime

class ErrorCog(commands.Cog, name='Help'):

    """Help Formater"""

    def __init__(self, bot):
        self.bot = bot

    @commands.Cog.listener()
    async def on_command_error(self, ctx, error):
        try:
            if hasattr(ctx.command, 'on_error'):
                return
            else:
                embed = discord.Embed(title=f'Error in {ctx.command}', description=f'`{ctx.command.qualified_name} {ctx.command.signature}` \n{error}', color=0x43780)
                await ctx.send(embed=embed)
        except:
            embed = discord.Embed(title=f'Error in {ctx.command}', description=f'{error}', color=0x43780)
            await ctx.send(embed=embed)

    @commands.command()
    async def help(self, ctx, *cog):
        if not cog:
            embed = discord.Embed(description='Custom Help')
            cog_desc = ''
            for x in self.bot.cogs:
                cog_desc = f'**{x}** - {self.bot.cogs[x].__doc__}\n'
                embed.add_field(name='Cogs', value=cog_desc)
            await ctx.send(embed=embed)
        else:
            if len(cog) > 1:
                embed = discord.Embed(title='Error', description='Zu viele Cogs!')
            else:
                found = False
                for x in self.bot.cogs:
                    for y in cog:
                        if x == y:
                            embed = discord.Embed()
                            scog_info = ''
                            for c in self.bot.cog(y).get_commands:
                                if not c.hidden:
                                    scog_info += {f'**{c.name}** - {c.help}\n'
                            embed.add_field(name=f'{cog[0]} Module', value=scog_info)
                            found = True
            if not found:
                for x in self.bot.cogs:
                    for c in self.bot.get_cog(x).commands():
                        if c.name == cog[0]:
                            embed =discord.Embed()
                            embed.add_field(name=f'{c.name} = {c.help}', value=f'Propper Syntax:\n`{c.qualified_name} {c. signature}`')
                    found = True
                if not found:
                    embed = discord.Embed(description='Das ist kein Cog!')
            await ctx.send(embed=embed)

def setup(bot):
    bot.add_cog(ErrorCog(bot))
    print('Help wurde geladen.')