from utils.listUtils import RandomListIndex
import discord
from discord.ext import commands

players = []
factions = ["Citizen", "Unaligned", "Mob"]
town_roles = ["goodman1", "goodman2", "goodman3", "goodman4"]
unaligned_roles = ["this", "is", "a", "placeholder"]
mafia_roles = ["badman1", "badman2", "badman3", "badman4", "badman5"]

class GamePlayer():
    def __init__(self, id, fac, role, iid):
        self.id = id
        self.fac = fac
        self.role = role
        self.iid = iid

    def __repr__(self):
        return f'GamePlayer(id = {self.id}, fac = {self.fac}, role = {self.role}, IID = {self.iid})'

    def get_id(self):   
        return self.id

    def get_fac_str(self):
        return str(self.fac)

    def get_role(self):
        return self.role
    
    def set_fac(self, fac):
        self.fac = fac

    def set_role(self, role):
        self.role = role

def SetPlayerFR(playerid):
    petroleum = len(players)
    oil = GamePlayer(playerid, "you shouldnt", "be seeing this", petroleum)
    oil.set_fac(factions[RandomListIndex(factions)])
    if oil.get_fac_str() == str(factions[0]):
        oil.set_role(town_roles[RandomListIndex(town_roles)])
    elif oil.get_fac_str() == str(factions[1]):
        oil.set_role(unaligned_roles[RandomListIndex(unaligned_roles)])
    elif oil.get_fac_str() == str(factions[2]):
        oil.set_role(mafia_roles[RandomListIndex(mafia_roles)])
    players.append(oil)
    print(oil)

async def sesh(host):
    pass

class GameCommands(commands.Cog):
   
    def __init__(self, bot):
        self.bot = bot

    @commands.command()
    async def test(self, ctx):
        await ctx.send("placeholder")
        
    @commands.command()
    async def join(self, ctx):
        msgauth = ctx.author
        if(msgauth.id not in players):
            SetPlayerFR(msgauth.id)
            
            if len(players) == 1:
                await ctx.send(f'Session hosted by {msgauth} has been created')
                await sesh()
            else:
                await ctx.send(f'{msgauth} has joined the session')
        else:
            await ctx.send(f'{msgauth}, youre already in the session!')

    @commands.command()
    async def check(self, ctx):
        try:
            print(str(players))
            await ctx.send(f"List of people in the game: {str(players)}")
        
        except Exception as e:
            exception = f"{type(e).__name__}: {e}"
            print(exception)


def setup(bot):
    bot.add_cog(GameCommands(bot))
