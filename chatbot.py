import os
from twitchio.ext import commands
from config import config

from wled_api import changeColor, turnOff, turnOn

class Bot(commands.Bot):
    def __init__(self):
            mytoken = config['STREAM']['Access_Token']
            client = config['STREAM']['Client_ID']
            pre = config['STREAM']['Prefix']
            channel = config['STREAM']['Channel']

            # Initialise our Bot with our access token, prefix and a list of channels to join on boot...
            super().__init__(token=mytoken, client_id=client, prefix=pre,
                         initial_channels=[channel])

    async def event_ready(self):
        'Called once when the bot goes online.'
        print("Bot is ready!")

    async def event_message(self, message):
        'Runs every time a message is sent in chat.'

        # make sure the bot ignores itself and the streamer
        if not message.author:
            return
        if message.author.name.lower() == config['STREAM']['Channel'].lower():
            return

        # checks if any defined command matches @bot.command()
        await bot.handle_commands(message)
            
        # get author name
        chatterName = str(message.author.name)

        # if someone use hello in their message, greet back
        if 'hello' in message.content.lower():
            
            await message.channel.send(f"Hi, @{chatterName}!")


    # new command with name 'color'
    @commands.command(name='color')
    async def color(self, bot: commands.Context, arg):
        await changeColor(bot, arg)

    # new command with name 'on'
    @commands.command(name='on')
    async def on(self, bot: commands.Context):
        await turnOn(bot)

    # new command with name 'off'
    @commands.command(name='off')
    async def off(self, bot: commands.Context):
        await turnOff(bot)

bot = Bot()
bot.run()