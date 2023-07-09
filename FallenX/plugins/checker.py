from pyrogram import filters
from pyrogram.types import Message

from config import BANNED_USERS

from FallenX import app
from FallenX.utils import bot_sys_stats
from FallenX.utils.database.memorydatabase import get_active_chats



@app.on_message(
    filters.command("respondtostatuschecker") & filters.private & ~BANNED_USERS
)
async def respond(_, message: Message):
    get = await bot_sys_stats()
    active_vc = len(await get_active_chats())
    await message.reply_text(f"{get[0]}~{get[1]}~{active_vc}")
