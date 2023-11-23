# Don't remove This Line From Here. Tg: @Dev_Arora_0981 | @DevArora0981
# Github :- Devarora-0981 | Devarora2604

import asyncio
import random

from pyrogram import filters
from pyrogram.enums import ChatType
from pyrogram.types import InlineKeyboardMarkup, Message

from config import EMOJIOS, IMG, STICKER
from Mickey import MickeyBot
from Mickey.database.chats import add_served_chat
from Mickey.database.users import add_served_user
from Mickey.modules.helpers import (
    CLOSE_BTN,
    DEV_OP,
    HELP_BTN,
    HELP_BUTN,
    HELP_READ,
    HELP_START,
    SOURCE_READ,
    START,
)


@MickeyBot.on_cmd(["start", "start"])
async def start(_, m: Message):
    if m.chat.type == ChatType.PRIVATE:
        accha = await m.reply_text(
            text=random.choice(EMOJIOS),
        )
        await asyncio.sleep(1.3)
        await accha.edit("__𝐖𝐞𝐥𝐜𝐨𝐦𝐞 𝐁𝐚𝐛𝐲 ꨄ︎ 𝐖𝐚𝐢𝐭..🥵__")
        await asyncio.sleep(0.2)
        await accha.edit("__𝐇𝐞𝐲 𝐁𝐚𝐛𝐲 ꨄ 𝐇𝐨𝐰 𝐀𝐫𝐞 𝐘𝐨𝐮⚡.....__")
        await asyncio.sleep(0.2)
        await accha.edit("__𝐁𝐨𝐭 𝐒𝐭𝐚𝐫𝐭𝐢𝐧𝐠 ꨄ︎ 𝐁𝐚𝐛𝐲📍..__")
        await asyncio.sleep(0.2)
        await accha.delete()
        umm = await m.reply_sticker(sticker=random.choice(STICKER))
        await asyncio.sleep(2)
        await umm.delete()
        await m.reply_photo(
            photo=random.choice(IMG),
            caption=f"""**🥀 𝐇𝐞𝐥𝐥𝐨, 𝐈 𝐀𝐦 𝐀𝐧 📀 𝐀𝐝𝐯𝐚𝐧𝐜𝐞𝐝 𝐀𝐧𝐝
𝐒𝐮𝐩𝐞𝐫𝐟𝐚𝐬𝐭 𝐕𝐂 𝐏𝐥𝐚𝐲𝐞𝐫 💐 𝐅𝐞𝐞𝐥 𝐅𝐫𝐞𝐞 𝐓𝐨 🕊️ 𝐀𝐧𝐝 𝐄𝐧𝐣𝐨𝐲 ❥︎ 𝐒𝐮𝐩𝐞𝐫 𝐇𝐢𝐠𝐡
𝐐𝐮𝐚𝐥𝐢𝐭𝐲 𝐀𝐮𝐝𝐢𝐨 𝐀𝐧𝐝 𝐕𝐢𝐝𝐞𝐨 🥂

┏━━━━━━━━━━━━━━━━━┓
┣★𝐂𝐑𝐄𝐀𝐓𝐎𝐑🌱 [𝐒𝐀𝐑𝐊𝐀𝐑](https://t.me/ll_SARKAR_BABE_ll)
┣★𝐀𝐁𝐎𝐔𝐓 𝐌𝐄🌱 [𝗝𝗢𝗜𝗡](https://t.me/TKS_JOIN)
┣★𝐆𝐑𝐎𝐔𝐏🌱 [𝗖𝗛𝗔𝗧 𝗚𝗥𝗢𝗨𝗣](https://t.me/TKS_CHAT_OFFICIAL)
┗━━━━━━━━━━━━━━━━━┛
🍹𝐏𝐎𝐖𝐄𝐑𝐃 𝐁𝐘🥀[𝐒𝐀𝐑𝐊𝐀𝐑](https://t.me/ll_SARKAR_BABE_ll)
"""""",
            reply_markup=InlineKeyboardMarkup(DEV_OP),
        )
        await add_served_user(m.from_user.id)
    else:
        await m.reply_photo(
            photo=random.choice(IMG),
            caption=START,
            reply_markup=InlineKeyboardMarkup(HELP_START),
        )
        await add_served_chat(m.chat.id)


@MickeyBot.on_cmd("help")
async def help(client: MickeyBot, m: Message):
    if m.chat.type == ChatType.PRIVATE:
        hmm = await m.reply_photo(
            photo=random.choice(IMG),
            caption=HELP_READ,
            reply_markup=InlineKeyboardMarkup(HELP_BTN),
        )
        await add_served_user(m.from_user.id)
    else:
        await m.reply_photo(
            photo=random.choice(IMG),
            caption="**ʜᴇʏ, ᴘᴍ ᴍᴇ ғᴏʀ ʜᴇʟᴘ ᴄᴏᴍᴍᴀɴᴅs!**",
            reply_markup=InlineKeyboardMarkup(HELP_BUTN),
        )
        await add_served_chat(m.chat.id)


@MickeyBot.on_cmd("on")
async def repo(_, m: Message):
    await m.reply_text(
        text=SOURCE_READ,
        reply_markup=InlineKeyboardMarkup(CLOSE_BTN),
        disable_web_page_preview=True,
    )


@MickeyBot.on_message(filters.new_chat_members)
async def welcome(_, m: Message):
    for member in m.new_chat_members:
        await m.reply_photo(photo=random.choice(IMG), caption=START)
