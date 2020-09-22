import discord
from discord.ext import commands
import asyncio
import datetime

class ModCog(commands.Cog, name='Moderation'):

    def __init__(self, bot):
        self.bot = bot

    @commands.command(aliases=['p','info'])
    async def profil(self, ctx):
        cl = ctx.author.colour
        embed = discord.Embed(colour=cl)
        embed.set_author(name=ctx.author, icon_url=ctx.author.avatar_url)
        embed.set_image(url=ctx.author.avatar_url)
        embed.add_field(name='Erstellt am:', value=ctx.author.created_at.__format__('%d.%m.%Y -- %H:%M:%S'))
        await ctx.send(embed=embed)

    @commands.command(aliases=['c','löschen'])
    async def clear(self, ctx, *, number:int=None):
        if ctx.message.author.guild_permissions.manage_messages:
            try:
                if number is None:
                    await ctx.send('Du musst eine Anzahl angeben')
                else:
                    deleted = await ctx.message.channel.purge(limit=number)
                    await ctx.send(f'Nachrichten gelöscht von: {ctx.message.author.mention}: `{len(deleted)}`')
            except:
                await ctx.send('Nachrichten können nicht gelöscht werden.')
        else:
            await ctx.send('Du bist nicht berechtigt diesen Befehl auszuführen!')

    @commands.command()
    async def kick(self, ctx, user: discord.Member, *, reason=None):
        if user.guild_permissions.manage_messages:
            await ctx.send('Benutzer kann nicht gekickt werden, da er ein Admin/Moderator ist.')
        elif ctx.message.author.guild_permissions.kick_members:
            if reason is None:
                await ctx.guild.kick(user=user, reason='None')
                await ctx.send(f'{user} wurde gekickt.')
            else:
                await ctx.guild.kick(user=user, reason=reason)
                await ctx.send(f'{user} wurde gekickt.')
        else:
            await ctx.send('Du bist nicht berechtigt diesen Befehl auszuführen!')

    @commands.command()
    async def ban(self, ctx, user:discord.Member, *, reason=None):
        if user.guild_permissions.manage_messages:
            await ctx.send('Benutzer kann nicht gekickt werden, da er ein Admin/Moderator ist.')
        elif ctx.message.author.guild_permissions.ban_members:
            if reason is None:
                await ctx.guild.ban(user=user, reason='None')
                await ctx.send(f'{user} wurde gebannt.')
            else:
                await ctx.guild.kick(user=user, reason=reason)
                await ctx.send(f'{user} wurde gebannt.')
        else:
            await ctx.send('Du bist nicht berechtigt diesen Befehl auszuführen!')

def setup(bot):
    bot.add_cog(ModCog(bot))
    print('Moderation wurde geladen.')