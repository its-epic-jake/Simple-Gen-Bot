import discord
from discord.ext import commands
import os

def get_prefix(client, message):
    prefixes = ['!']
    return commands.when_mentioned_or(*prefixes)(client, message)


bot = commands.Bot(                                         
    command_prefix=get_prefix,                              
    description='A bot',
    case_insensitive=True
)

bot.remove_command('help')

@bot.event
async def  on_ready():
    print("Ready!")
      

#help
@bot.command(pass_context = True)
async def help(ctx):
  helpembed = discord.Embed(title="Commands",description="BOT PREFIX: ! or ping the bot\nInfo (info on bot)\Genaccount (get a hulu account)\nStock see how many accounts are left.", color=0x0011ff)
  helpembed.set_footer(text="This bot was coded by its-epic-jake on github")
  await ctx.send(embed = helpembed)

#info
@bot.command()
async def info(ctx):
  infoembed = discord.Embed(title="Bot information", description="Bot was coded in python by https://github.com/its-epic-jake", color=0x00ff00)
  await ctx.send(embed=infoembed)

#genaccount
@bot.command()
@commands.cooldown(1, 300, commands.BucketType.user)
async def genaccount(ctx):
  filesize = os.path.getsize("accounts.txt")

  if filesize == 0:
    await ctx.send("Out of stock! Ask staff to restock.")
  else:
    await ctx.send("Account should be sent in your dms.")

    f = open("accounts.txt", "r")
    acc = f.readline()
    f.close()
    f = open("accounts.txt", "r")
    lines = f.readlines()
    del lines[0]
    f = open("accounts.txt", "w+")
    for line in lines:
     f.write(line)
    f.close()

    embed = discord.Embed(title="Your account:", description=acc, color=0x00ff00)
    await ctx.author.send(embed=embed)
@genaccount.error
async def mine_error(ctx, error):
    if isinstance(error, commands.CommandOnCooldown):
        msg = 'This command is on cooldown, please try again in {:.2f} / 5m.'.format(error.retry_after)
        await ctx.send(msg)
    else:
        raise error

#stock
@bot.command()
async def stock(ctx):
  def file_lengthy(fname):
          with open(fname) as f:
                  for i, l in enumerate(f):
                          pass
          return i + 1

  accounts = file_lengthy("accounts.txt")
          
  embedVar=discord.Embed(title="Stock", color=0x00ff08)
  embedVar.add_field(name="accounts", value=accounts, inline=True)
  await ctx.send(embed=embedVar)

bot.run(open('token.txt', 'r').read(), bot=True, reconnect=True)
