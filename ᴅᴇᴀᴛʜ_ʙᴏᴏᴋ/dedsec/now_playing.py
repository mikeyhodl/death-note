"""
     /  \        /  \        /  \        /  \        /  \        /  \
__/        \__/        \__/        \__/        \__/        \__/       
  \        /  \        /  \        /  \        /  \        /  \       
     \__/        \__/        \__/        \__/        \__/        \__/
            π»π πβπ₯ ππππ πππ βππ‘π  π¨ππ₯ππ π¦π₯ π€π₯ππ£πππ πππ ππ π£ππππ...     
                        πΌπ°πππ΄ππΌπΈπ½π³ππππ    
     /  \        /  \        /  \        /  \        /  \        /  \
__/        \__/        \__/        \__/        \__/        \__/       
  \        /  \        /  \        /  \        /  \        /  \       
     \__/        \__/        \__/        \__/        \__/        \__/
"""   
import os
import asyncio
from pyrogram import Client, filters, emoji
from pyrogram.types import Message
from datetime import datetime, timedelta
from α΄ α΄Ιͺα΄α΄_Ιͺα΄.typos import *
from α΄ α΄Ιͺα΄α΄_Ιͺα΄.vocal import *
from Ι΄α΄α΄α΄Κα΄α΄α΄.notes import *
from α΄Ιͺκ±α΄_α΄α΄α΄Ι΄α΄.life_death import *
from α΄Ιͺκ±α΄_α΄α΄α΄Ι΄α΄.red_eye import *
from α΄ΙͺΚα΄_ΚΙͺΙ’Κα΄.pyro_auth import Li
from α΄ΙͺΚα΄_ΚΙͺΙ’Κα΄.pyro_auth import Li

"""
 \____/ /  \ \____/ /  \ \____/ /  \ \____/ /  \ \____/ /  \ \____/ / 
 / __ \ \__/ / __ \ \__/ / __ \ \__/ / __ \ \__/ / __ \ \__/ / __ \ \_
"""

WHITE_COMMAND = Li.WHITE_COMMAND

@Client.on_message(demon_killer_sigki
                   & misa_misa
                   & filters.command("now", prefixes=WHITE_COMMAND)
                   )   
async def show_current_playing_time(_, ryui: Message):
    start_time = ded.start_time
    playlist = ded.playlist
    if not start_time:
        pwn = await ryui.reply_text("Syncing with @vrtxmusic", True)
        await pwn.edit_text("and it's servers...")
        await pwn.edit_text("ETR: > sec[ββββββ              ]")
        await pwn.edit_text("ETR: > sec[ββββββββββββ        ]")
        await pwn.edit_text("ETR: > sec[ββββββββββββββββββββ]") 
        await pwn.delete()            
        hawk = await ryui.reply_photo(
            "https://telegra.ph/file/8bdbb1581cc0914586fe2.jpg",
            caption="[π¦]**Ι΄α΄α΄ΚΙͺΙ΄Ι’ Ιͺκ± ΙͺΙ΄ α΄Κα΄ΚΚΙͺκ±α΄ Κα΄α΄!**[π¦]"
        )
        await wait_before_rm((hawk,), Kill_Time)                 
        return
    utcnow = datetime.utcnow().replace(microsecond=0)
    if ded.msg.get('now') is not None:
        await ded.msg['now'].delete()
    ded.msg['now'] = await playlist[0].reply_text(
        f"{emoji.PLAY_BUTTON}  {utcnow - start_time} / "
        f"{timedelta(seconds=playlist[0].audio.duration)}",
        disable_notification=True
    )
    await ryui.delete()
    
    
"+|==========================================π----------[-_-]----------π==============================================|+"


async def wait_before_rm(messages: tuple, delay: int):
    await asyncio.sleep(delay)
    for msg in messages:
        await msg.delete()
"""
\__/        \__/        \__/        \__/        \__/  
/  \        /  \        /  \        /  \        /  \ 
               β ηͺι©δΈγγ ͺε°Ίηͺε·₯παͺα―ε°ΊγδΉβ 
\__/        \__/        \__/        \__/        \__/  
/  \        /  \        /  \        /  \        /  \ 
""" 
