import os
from twitchio.ext import commands
import configparser

config = configparser.ConfigParser()

class Bot(commands.Bot):
    def __init__(self):
            global config
            config.read('config.ini')
            mytoken = config['STREAM']['Access_Token']
            client = config['STREAM']['Client_ID']
            nickname = config['STREAM']['Nickname']
            pre = config['STREAM']['Prefix']
            channel = config['STREAM']['Channel']

            # Initialise our Bot with our access token, prefix and a list of channels to join on boot...
            super().__init__(token=mytoken, client_id=client, nick=nickname, prefix=pre,
                         initial_channels=[channel])

    async def event_ready(self):
        'Called once when the bot goes online.'
        print(f"{config['STREAM']['Nickname']} is online!")

    async def event_message(self, message):
        'Runs every time a message is sent in chat.'

        # make sure the bot ignores itself and the streamer
        if not message.author:
            return
        if message.author.name.lower() == config['STREAM']['Channel'].lower():
            return
        # get author name
        chatterName = str(message.author.name)

        # checks if any defined command matches @bot.command()
        await bot.handle_commands(message)

        # if someone use hello in their message, greet back
        if 'hello' in message.content.lower():
            
            await message.channel.send(f"Hi, @{chatterName}!")


    # new command with name 'test'
    # prefix in env
    @commands.command(name='test')
    async def test(ctx):
        await ctx.send('test passed!')

bot = Bot()
bot.run()