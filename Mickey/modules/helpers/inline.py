from pyrogram.types import InlineKeyboardButton

from config import SUPPORT_GRP, UPDATE_CHNL
from Mickey import OWNER
from Mickey import MickeyBot

DEV_OP = [
    [
        InlineKeyboardButton(text="𝙊𝙒𝙉𝙀𝙍", user_id=OWNER),
        InlineKeyboardButton(text="𝙐𝙋𝘿𝘼𝙏𝙀", url=f"https://t.me/{SUPPORT_GRP}"),
    ],
    [
        InlineKeyboardButton(
            text="❮𝘼𝘿𝘿 𝙔𝙊𝙐𝙍 𝙂𝙍𝙊𝙐𝙋❯",
            url=f"https://t.me/{MickeyBot.username}?startgroup=true",
        ),
    ],
    [
        InlineKeyboardButton(text="❮𝙃𝙀𝙇𝙋❯", callback_data="HELP"),
    ],
]

PNG_BTN = [
    [
        InlineKeyboardButton(
            text="❮𝐀𝐃𝐃 𝐌𝐄 𝐘𝐎𝐔𝐑 𝐆𝐑𝐎𝐔𝐏❯",
            url=f"https://t.me/{MickeyBot.username}?startgroup=true",
        ),
    ],
    [
        InlineKeyboardButton(
            text="❮𝗛𝗘𝗟𝗣❯",
            callback_data="CLOSE",
        ),
    ],
]


BACK = [
    [
        InlineKeyboardButton(text="❮𝗕𝗔𝗖𝗞❯", callback_data="BACK"),
    ],
]


HELP_BTN = [
    [
        InlineKeyboardButton(text="❮𝗖𝗛𝗔𝗧𝗕𝗢𝗧❯", callback_data="CHATBOT_CMD"),
        InlineKeyboardButton(text="𝗧𝗢𝗢𝗟𝗦", callback_data="TOOLS_DATA"),
    ],
    [
        InlineKeyboardButton(text="❮𝗕𝗔𝗖𝗞❯", callback_data="BACK"),
        InlineKeyboardButton(text="❮𝗖𝗟𝗢𝗦𝗘❯", callback_data="CLOSE"),
    ],
]


CLOSE_BTN = [
    [
        InlineKeyboardButton(text="❮𝗖𝗟𝗢𝗦𝗘❯", callback_data="CLOSE"),
    ],
]


CHATBOT_ON = [
    [
        InlineKeyboardButton(text="❮𝗘𝗡𝗔𝗕𝗟𝗘❯", callback_data=f"addchat"),
        InlineKeyboardButton(text="❮𝗗𝗶𝗦𝗔𝗕𝗟𝗘❯", callback_data=f"rmchat"),
    ],
]


MUSIC_BACK_BTN = [
    [
        InlineKeyboardButton(text="❮𝗦𝗢𝗢𝗡❯", callback_data=f"soom"),
    ],
]

S_BACK = [
    [
        InlineKeyboardButton(text="❮𝗕𝗔𝗖𝗞❯", callback_data="SBACK"),
        InlineKeyboardButton(text="❮𝗖𝗟𝗢𝗦𝗘❯", callback_data="CLOSE"),
    ],
]


CHATBOT_BACK = [
    [
        InlineKeyboardButton(text="❮𝗕𝗔𝗖𝗞❯", callback_data="CHATBOT_BACK"),
        InlineKeyboardButton(text="❮𝗖𝗟𝗢𝗦𝗘❯", callback_data="CLOSE"),
    ],
]


HELP_START = [
    [
        InlineKeyboardButton(text="❮𝗛𝗘𝗟𝗣❯", callback_data="HELP"),
        InlineKeyboardButton(text="❮𝗖𝗟𝗢𝗦𝗘❯", callback_data="CLOSE"),
    ],
]


HELP_BUTN = [
    [
        InlineKeyboardButton(
            text="❮𝗔𝗗𝗗 𝗬𝗢𝗨𝗥 𝗖𝗛𝗔𝗧❯", url=f"https://t.me/{MickeyBot.username}?start=help"
        ),
        InlineKeyboardButton(text="❮𝗖𝗟𝗢𝗦𝗘❯", callback_data="CLOSE"),
    ],
]


ABOUT_BTN = [
    [
        InlineKeyboardButton(text="❮𝗝𝗢𝗜𝗡❯", url=f"https://t.me/{SUPPORT_GRP}"),
        InlineKeyboardButton(text="❮𝗛𝗘𝗟𝗣❯", callback_data="HELP"),
    ],
    [
        InlineKeyboardButton(text="❮𝗢𝗪𝗡𝗘𝗥❯", user_id=OWNER),
        InlineKeyboardButton(text="❮𝗝𝗢𝗜𝗡❯", callback_data="https://t.me/{UPDATE_CHNL}"),
    ],
    [
        InlineKeyboardButton(text="❮𝗨𝗣𝗗𝗔𝗧𝗘❯", url=f"https://t.me/{UPDATE_CHNL}"),
        InlineKeyboardButton(text="❮𝗕𝗔𝗖𝗞❯", callback_data="BACK"),
    ],
]
