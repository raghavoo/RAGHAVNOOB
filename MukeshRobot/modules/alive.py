import asyncio
from platform import python_version as pyver

from pyrogram import __version__ as pver
from pyrogram import filters
from pyrogram.types import InlineKeyboardButton, InlineKeyboardMarkup, Message
from telegram import __version__ as lver
from telethon import __version__ as tver

from MukeshRobot import SUPPORT_CHAT, pbot,BOT_USERNAME, OWNER_ID,BOT_NAME,START_IMG

PHOTO = [
    "https://te.legra.ph/file/f6dae19f8f70eaebc1fa7.jpg",
    "https://te.legra.ph/file/dc1c14251a23117337709.jpg",
    "https://te.legra.ph/file/6140e420212ecc8a5eb5d.jpg",
    "https://te.legra.ph/file/05fd8d1c72ea4ecab0b94.jpg",
    "https://te.legra.ph/file/c2216b55b5184c6c82bd2.jpg",
    "https://te.legra.ph/file/ce9449ba241a800be90ff.jpg",
    "https://te.legra.ph/file/75be49dd237fbbb536fe5.jpg",
    "https://te.legra.ph/file/88977fae533165fa9a3f6.jpg"
]

Mukesh = [
    [
        InlineKeyboardButton(text="ᴜᴘᴅᴀᴛᴇ", url=f"https://t.me/raghavsupport"),
        InlineKeyboardButton(text="ꜱᴜᴘᴘᴏʀᴛ", url=f"https://t.me/{SUPPORT_CHAT}"),
    ],
    [
        InlineKeyboardButton(
            text="ᴀᴅᴅ ᴍᴇ ʙᴀʙʏ",
            url=f"https://t.me/{BOT_USERNAME}?startgroup=true",
        ),
    ],
]



@pbot.on_message(filters.command("alive"))
async def restart(client, m: Message):
    await m.delete()
    accha = await m.reply("🤍")
    await asyncio.sleep(0.2)
    await accha.edit("🖤")
    await asyncio.sleep(0.1)
    await accha.edit("🧡")
    await asyncio.sleep(0.1)
    await accha.edit("💚")

    await accha.delete()
    await asyncio.sleep(0.3)
    umm = await m.reply_sticker(
        "CAACAgUAAx0Cd3wFvgABAiC2ZaAOXz4KXYQYvvb9CrBPgl03m-8AAt0GAAKi4uBXifHx2xHzXNU0BA"
    )
    await umm.delete()
    await asyncio.sleep(0.2)
    await m.reply_photo(
        START_IMG,
        caption=f"""** ✦ ʜᴇʏ, ɪ ᴀᴍ [{BOT_NAME}](f"t.me/{BOT_USERNAME}") ✦**\n\n❍ **ʟɪʙʀᴀʀʏ ➛** `{lver}`\n❍ **ᴛᴇʟᴇᴛʜᴏɴ ➛** `{tver}`\n❍ **ᴘʏʀᴏɢʀᴀᴍ ➛** `{pver}`\n❍ **ᴘʏᴛʜᴏɴ ➛** `{pyver()}`\n\n❍ **ᴍᴀᴅᴇ ʙʏ ➛** [ʀᴏʏ-ᴇᴅɪᴛx](tg://user?id={OWNER_ID})""",
        reply_markup=InlineKeyboardMarkup(Mukesh),
    )
    
__mod_name__ = "ᴀʟɪᴠᴇ"
__help__ = """
 ❍ /alive ➛ ᴄʜᴇᴄᴋ ʙᴏᴛ ᴀʟɪᴠᴇ sᴛᴀᴛᴜs.
 """
