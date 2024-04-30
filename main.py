import nextcord
from nextcord.ext import commands


TESTING_GUILD_ID = 997109991272087662  # Replace with your guild ID
bot = commands.Bot()

@bot.event
async def on_ready():
    print(f'We have logged in as {bot.user}')

@bot.slash_command(description="use this command to meet the requreiments for the active dev badge", guild_ids=[TESTING_GUILD_ID])
async def active_dev_badge(interaction: nextcord.Interaction):
    await interaction.send("Requriments met, wait 24 hour then go to https://discord.com/developers/active-developer to claim")



bot.run('MTAzNjI5NDE2MTMxNTM5NzY3Mg.GUfAii.bdeXlmRG0mj7PbqnWK_wGixRi15L8no_iIR1Xc')
