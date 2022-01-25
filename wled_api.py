import asyncio

from wled import WLED
from colorsToHex import colors

from config import config


led = WLED(config['WLED']['IP'])


async def changeColorWLED(color: str):
        device = await led.update()
        print(device.info.version)

        if not colors[color]:
            print("unknown color: " + color)
            return

        hex = colors[color]
        rgb = tuple(int(hex[i:i+2], 16) for i in (0, 2, 4))

        await led.segment(segment_id=0, brightness=255, color_primary=rgb)

async def masterStateWLED(enabled: bool):
        device = await led.update()
        print(device.info.version)

        await led.master(on=enabled, brightness=255)


async def changeColor(color: str):
    print("changeColor")
    await changeColorWLED(color)

async def turnOn():
    print("turnOn")
    await masterStateWLED(True)

async def turnOff():
    print("turnOff")
    await masterStateWLED(False)