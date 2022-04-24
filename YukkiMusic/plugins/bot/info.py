#
# Copyright (C) 2021-2022 by TeamYukki@Github, < https://github.com/TeamYukki >.
#
# This file is part of < https://github.com/TeamYukki/YukkiMusicBot > project,
# and is released under the "GNU v3.0 License Agreement".
# Please see < https://github.com/TeamYukki/YukkiMusicBot/blob/master/LICENSE >
#
# All rights reserved.


from typing import Union

from pyrogram import filters, types
from pyrogram.types import InlineKeyboardMarkup, Message

from config import BANNED_USERS
from strings import get_command, get_string, helpers
from YukkiMusic import app
from YukkiMusic.misc import SUDOERS
from YukkiMusic.utils import help_pannel
from YukkiMusic.utils.database import get_lang, is_commanddelete_on
from YukkiMusic.utils.decorators.language import (LanguageStart,
                                                  languageCB)
from YukkiMusic.utils.inline.help import (help_back_markup,
                                          private_help_panel)


@app.on_callback_query(filters.regex("info_callback") & ~BANNED_USERS)
@languageCB
async def helper_cb(client, CallbackQuery, _):
    callback_data = CallbackQuery.data.strip()
    cb = callback_data.split(None, 1)[1]
    keyboard = help_back_markup(_)
    try:
        await CallbackQuery.answer()
    except:
        pass
    if cb == "info1":
        await CallbackQuery.edit_message_text(
            helpers.BOT_ABOUT, reply_markup=keyboard
        )
    elif cb == "info2":
        await CallbackQuery.edit_message_text(
            helpers.BOT_SETUP, reply_markup=keyboard
        )
