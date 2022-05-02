#
# Copyright (C) 2021-2022 by TeamYukki@Github, < https://github.com/TeamYukki >.
#
# This file is part of < https://github.com/TeamYukki/YukkiMusicBot > project,
# and is released under the "GNU v3.0 License Agreement".
# Please see < https://github.com/TeamYukki/YukkiMusicBot/blob/master/LICENSE >
#
# All rights reserved.

from typing import Union

from pyrogram.types import InlineKeyboardButton

from config import GITHUB_REPO, SUPPORT_CHANNEL, SUPPORT_GROUP
from YukkiMusic import app


def start_pannel(_):
    buttons = [
        [
            InlineKeyboardButton(
                text=_["S_B_1"],
                url=f"https://t.me/{app.username}?start=help",
            ),
            InlineKeyboardButton(
                text=_["S_B_2"], callback_data="settings_helper"
            ),
        ],
    ]
    if SUPPORT_CHANNEL and SUPPORT_GROUP:
        buttons.append(
            [
                InlineKeyboardButton(
                    text=_["S_B_3"], url=f"{SUPPORT_GROUP}"
                ),
                InlineKeyboardButton(
                    text=_["S_B_4"], url=f"{SUPPORT_CHANNEL}"
                ),
            ]
        )
    else:
        if SUPPORT_CHANNEL:
            buttons.append(
                [
                    InlineKeyboardButton(
                        text=_["S_B_3"], url=f"{SUPPORT_GROUP}"
                    )
                ]
            )
        if SUPPORT_GROUP:
            buttons.append(
                [
                    InlineKeyboardButton(
                        text=_["S_B_4"], url=f"{SUPPORT_CHANNEL}"
                    )
                ]
            )
    return buttons


def private_panel(_, BOT_USERNAME, OWNER: Union[bool, int] = None):
    buttons = [
            [
                InlineKeyboardButton(
                    text=_["S_B_11"], callback_data="bot_code"
                ),
                InlineKeyboardButton(
                    text=_["S_B_9"], callback_data="settings_back_about"
                ),
            ]
        ]
    if SUPPORT_CHANNEL and SUPPORT_GROUP:
        buttons.append(
            [
                InlineKeyboardButton(
                    text=_["S_B_11"], callback_data="bot_code"
                ),
                InlineKeyboardButton(
                    text=_["S_B_9"], callback_data="settings_back_about"
                ),
            ]
        )
    else:
        if SUPPORT_CHANNEL:
            buttons.append(
                [
                    InlineKeyboardButton(
                        text=_["S_B_11"], callback_data="bot_code"
                    )
                ]
            )
        if SUPPORT_GROUP:
            buttons.append(
                [
                    InlineKeyboardButton(
                        text=_["S_B_9"], callback_data="settings_back_about"
                    )
                ]
            )
    if GITHUB_REPO and OWNER:
        buttons.append(
            [
                InlineKeyboardButton(text=_["S_B_11"], callback_data="bot_code"),
                InlineKeyboardButton(
                    text=_["S_B_10"], callback_data="LG"
                ),
            ]
        )
    else:
        if GITHUB_REPO:
            buttons.append(
                [
                    InlineKeyboardButton(
                        text=_["S_B_10"], callback_data="LG"
                    ),
                ]
            )
        if OWNER:
            buttons.append(
                [
                    InlineKeyboardButton(
                        text=_["S_B_11"], callback_data="bot_code"
                    ),
                ]
            )
    buttons.append(
        [InlineKeyboardButton(text=_["S_B_13"], callback_data="LG")]
    )
    return buttons
