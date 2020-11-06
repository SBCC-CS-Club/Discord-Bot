import discord
from discord.ext import commands
from mailer import send_verification_email
import secrets
intents = discord.Intents(messages=True, members=True, guilds=True, dm_messages=True)
bot = commands.Bot(command_prefix='>', intents=intents)


@bot.command()
async def ping(ctx):
    await ctx.send('pong')

@bot.event
async def on_member_join(member):
    await member.send(
        "Welcome to the **Offical CS Club Discord Server!** In order to make sure our server is safe please enter "
        "your pipeline email. You will recieve an email with a code to verify your account. If you are a former "
        "student and do not have access to your pipeline email anymore people contact an officer through a DM. "
    )
    verified = False
    while not verified:
        m = await bot.wait_for('message', check=lambda
            message: message.author.id == member.id and type(message.channel) == discord.DMChannel)
        if "@pipeline.sbcc.edu" in m.content or "@sbcc.edu":
            token = secrets.token_urlsafe(10)
            send_verification_email(m.content, token)
            await member.send("Please enter the code from the email:")

            m = await bot.wait_for('message', check=lambda
            message: message.author.id == member.id and type(message.channel) == discord.DMChannel)
            if m.content == token:
                # give the user the role
                server = bot.get_guild(756173932599443546)
                print(server.name)
                member = server.get_member(int(member.id))
                print(member.display_name)
                role = discord.utils.get(server.roles, name='Member')
                await member.add_roles(role)
                await member.send('Verified! If you have any issues please contact any of the officers!')
                verified = True
            else:
                await member.send('Sorry that is the wrong verification code please try again. Please re-enter your email for a new code.')
        else:
            await member.send("Sorry that email is not an SBCC email. Please try again")
