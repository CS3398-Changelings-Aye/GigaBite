import discord
from discord.ext import commands

class Information(commands.Cog):

    def __init__(self, bot):
        self.bot = bot


    @commands.command(pass_context=True)
    async def drinks(self, ctx):
        em = discord.Embed(title="Drink Pairing", description="Here are a few recommendations for drinks to pair with your meals.")
        em.set_author(name=str(self.bot.user.name))
        em.colour = 0x000000
        em.add_field(name="Red Meat", value="Beers, such as porters and stouts are good with beef, as well as white or red wine and whiskey.")
        em.add_field(name= "White Meat", value="Pale Ales, Sake, full bodied red or white wines, as well as a gin or tonic pair well with poultry.")
        em.add_field(name= "Seafood",  value="Citrus margaritas, a Bloody Mary, or Bourbon pair best with seafood.")
        em.add_field(name= "Pasta",  value="For red sauces, I suggest a classic red wine. For white sauces, IPA beer or Chardonay.")
        em.add_field(name= "Vegetables",  value="If your vegetables are roasted, try a rich red, like Merlot. For more buttery veggies, try a Chardonay.")
        await ctx.send(embed=em)



def setup(bot):
    bot.add_cog(Information(bot))