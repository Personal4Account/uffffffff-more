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
from strings import get_command, get_string, botinfo
from YukkiMusic import app
from YukkiMusic.misc import SUDOERS
from YukkiMusic.utils import info_pannel
from YukkiMusic.utils.database import get_lang, is_commanddelete_on
from YukkiMusic.utils.decorators.language import (LanguageStart,
                                                  languageCB)
from YukkiMusic.utils.inline.botinfo2 import (about_back_markup,
                                          private_help_panel)


@app.on_callback_query(
    filters.regex("settings_back_about") & ~BANNED_USERS
)
async def botinfo_private(
    client: app, update: Union[types.Message, types.CallbackQuery]
):
    is_callback = isinstance(update, types.CallbackQuery)
    if is_callback:
        try:
            await update.answer()
        except:
            pass
        chat_id = update.message.chat.id
        language = await get_lang(chat_id)
        _ = get_string(language)
        keyboard = info_pannel(_, True)
        if update.message.photo:
            await update.message.delete()
            await update.message.reply_text(
                _["B_I_3"], reply_markup=keyboard
            )
        else:
            await update.edit_message_text(
                _["B_I_3"], reply_markup=keyboard
            )
    else:
        chat_id = update.chat.id
        if await is_commanddelete_on(update.chat.id):
            try:
                await update.delete()
            except:
                pass
        language = await get_lang(chat_id)
        _ = get_string(language)
        keyboard = info_pannel(_)
        await update.reply_text(_["B_I_3"], reply_markup=keyboard)


@app.on_callback_query(filters.regex("info_callback") & ~BANNED_USERS)
@languageCB
async def botinfo_cb(client, CallbackQuery, _):
    callback_data = CallbackQuery.data.strip()
    cb = callback_data.split(None, 1)[1]
    keyboard = about_back_markup(_)
    try:
        await CallbackQuery.answer()
    except:
        pass
    if cb == "info1":
        await CallbackQuery.edit_message_text(
            botinfo.BOT_ABOUT, reply_markup=keyboard
        )
    elif cb == "info2":
        await CallbackQuery.edit_message_text(
            botinfo.BOT_SETUP, reply_markup=keyboard
        )
