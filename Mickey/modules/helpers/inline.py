from pyrogram.types import InlineKeyboardButton

from config import SUPPORT_GRP, UPDATE_CHNL
from Mickey import OWNER
from Mickey import MickeyBot

DEV_OP = [
    [
        InlineKeyboardButton(
            text="🥵𝐀𝐝𝐝 𝐌𝐞 𝐘𝐨𝐮𝐫 𝐆𝐫𝐨𝐮𝐩🥵",
            url=f"https://t.me/{MickeyBot.username}?startgroup=true",
        ),
    ],
    [
        InlineKeyboardButton(text="🚀 ʜᴇʟᴘ & ᴄᴍᴅs 🚀", callback_data="HELP"),
    ],
]

PNG_BTN = [
    [
        InlineKeyboardButton(
            text="🥵𝐀𝐝𝐝 𝐌𝐞 𝐘𝐨𝐮𝐫 𝐆𝐫𝐨𝐮𝐩🥵",
            url=f"https://t.me/{MickeyBot.username}?startgroup=true",
        ),
    ],
    [
        InlineKeyboardButton(
            text="✨ ᴄʟᴏsᴇ ✨",
            callback_data="CLOSE",
        ),
    ],
]


BACK = [
    [
        InlineKeyboardButton(text="✨ ʙᴀᴄᴋ ✨", callback_data="BACK"),
    ],
]
