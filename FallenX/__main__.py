import asyncio
import importlib
import sys

from pyrogram import idle
from pytgcalls.exceptions import NoActiveGroupCall

import config
from config import BANNED_USERS
from FallenX import LOGGER, app, userbot
from FallenX.core.call import Anon
from FallenX.plugins import ALL_MODULES
from FallenX.utils.database import get_banned_users, get_gbanned

loop = asyncio.get_event_loop()


async def init():
    if (
        not config.STRING1
        and not config.STRING2
        and not config.STRING3
        and not config.STRING4
        and not config.STRING5
    ):
        LOGGER("FallenX").error(
            "WTF Baby ! Atleast add a pyrogram string, How Cheap..."
        )
        return
    try:
        users = await get_gbanned()
        for user_id in users:
            BANNED_USERS.add(user_id)
        users = await get_banned_users()
        for user_id in users:
            BANNED_USERS.add(user_id)
    except:
        pass
    await app.start()
    for all_module in ALL_MODULES:
        importlib.import_module("FallenX.plugins." + all_module)
    LOGGER("FallenX.plugins").info(
        "Necessary Modules Imported Successfully."
    )
    await userbot.start()
    await Anon.start()
    try:
        await Anon.stream_call(
            "https://te.legra.ph/file/29f784eb49d230ab62e9e.mp4"
        )
    except NoActiveGroupCall:
        LOGGER("FallenX").error(
            "[ERROR] - \n\nHey Baby, firstly open telegram and turn on voice chat in Logger Group else fu*k off. If you ever ended voice chat in log group i will stop working and users will fu*k you up."
        )
        sys.exit()
    except:
        pass
    await Anon.decorators()
    LOGGER("FallenX").info("Music Bot Started Successfully, Now Gib your girlfriend chumt to @anonymous_was_bot")
    await idle()


if __name__ == "__main__":
    loop.run_until_complete(init())
    LOGGER("FallenX").info("Stopping Music Bot, Bhakk Bhosdike (Gaand Maraa Tu)")
