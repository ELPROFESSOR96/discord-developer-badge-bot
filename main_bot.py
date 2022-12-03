import nextcord
from nextcord.ext import commands


TESTING_GUILD_ID = 1027416032748511262  # Replace with your guild ID
bot = commands.Bot()

@bot.event
async def on_ready():
    print(f'We have logged in as {bot.user}')

@bot.slash_command(description="use this command to meet the requreiments for the active dev badge", guild_ids=[TESTING_GUILD_ID])
async def active_dev_badge(interaction: nextcord.Interaction):
    await interaction.send("Requriments met, wait 24 hour then go to https://discord.com/developers/active-developer to claim")



bot.run('MTA0ODE0MDIyMTc5NzEwOTg1MA.GI02xG.ozNEZr_-ig8ITgOx1al6_skOijXfjG5C5CZEBk')
