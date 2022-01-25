from wled import WLED
from colorsToHex import colors
from twitchio.ext import commands

from config import config


led = WLED(config['WLED']['IP'])


async def changeColorWLED(color: str) -> bool:
        if color not in colors:
            print("unknown color: " + color)
            return False

        hex = colors[color]
        rgb = tuple(int(hex[i:i+2], 16) for i in (0, 2, 4))

        await led.segment(segment_id=0, brightness=255, color_primary=rgb)
        return True

async def masterStateWLED(enabled: bool):
        # device = await led.update()

        await led.master(on=enabled, brightness=255)


async def changeColor(bot: commands.Context, color: str):
    ret = await changeColorWLED(color)
    if ret:
        await bot.send('Color changed!')

async def turnOn(bot: commands.Context):
    await masterStateWLED(True)
    await bot.send('LED Strip turned on!')

async def turnOff(bot: commands.Context):
    await masterStateWLED(False)
    await bot.send('LED Strip turned off!')