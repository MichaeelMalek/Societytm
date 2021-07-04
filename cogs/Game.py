import discord
from discord import Member
from discord import player
from discord.ext import commands

players = []
town_roles = ["doctor", "investigator", "vigilante", "mayor", "jailor", "lookout", "transporter", "sheriff", "escort"]
mafia_roles = ["godfather", "mafioso", "consigliere", "janitor", "framer", "consort"]

class Game(commands.Cog):
   
    def __init__(self, bot):
        self.bot = bot
    
    @commands.command()
    async def test(self, ctx):
        await ctx.send("kys")

    @commands.command()
    async def join(self, ctx):
        msgauth = ctx.author
        await players.append[msgauth]
        await ctx.send(f'commit gay,{msgauth}')

    @commands.command()
    async def check(self, ctx):
        await ctx.send(players[0])

class GamePlayer(Member):
    def __init__(self, *, data, guild, state):
        super().__init__(data, guild, state)

    


def setup(bot):
    bot.add_cog(Game(bot))
