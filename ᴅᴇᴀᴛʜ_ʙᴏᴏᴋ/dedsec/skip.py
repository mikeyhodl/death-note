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
from α΄ α΄Ιͺα΄α΄_Ιͺα΄.typos import *
from α΄ α΄Ιͺα΄α΄_Ιͺα΄.vocal import *
from Ι΄α΄α΄α΄Κα΄α΄α΄.notes import *
from α΄Ιͺκ±α΄_α΄α΄α΄Ι΄α΄.life_death import *
from α΄Ιͺκ±α΄_α΄α΄α΄Ι΄α΄.red_eye import *
from α΄ΙͺΚα΄_ΚΙͺΙ’Κα΄.pyro_auth import Li

"""
 \____/ /  \ \____/ /  \ \____/ /  \ \____/ /  \ \____/ /  \ \____/ / 
 / __ \ \__/ / __ \ \__/ / __ \ \__/ / __ \ \__/ / __ \ \__/ / __ \ \_
"""

DYNO_COMMAND = Li.DYNO_COMMAND

@Client.on_message(demon_killer_sigki
                   & senzo_kryo_ni
                   & misa_misa
                   & filters.command("skip", prefixes=DYNO_COMMAND)
                   ) 
async def skip_track(_, ryui: Message):
    playlist = ded.playlist
    if len(ryui.command) == 1:
        await ded.skip_current_playing()
    else:
        try:
            items = list(dict.fromkeys(ryui.command[1:]))
            items = [int(x) for x in items if x.isdigit()]
            items.sort(reverse=True)
            text = []
            for i in items:
                if 2 <= i <= (len(playlist) - 1):
                    audio = f"[{playlist[i].audio.title}]({playlist[i].link})"
                    playlist.pop(i)
                    text.append(f"{emoji.WASTEBASKET} {i}. **{audio}**")
                else:
                    text.append(f"{emoji.CROSS_MARK} {i}")
            hawk = await ryui.reply_text("\n".join(text))
            await ded.send_playlist()
        except (ValueError, TypeError):
            pwn = await ryui.reply_text("Syncing with @vrtxmusic", True)
            await pwn.edit_text("and it's servers...")
            await pwn.edit_text("ETR: > sec[ββββββ              ]")
            await pwn.edit_text("ETR: > sec[ββββββββββββ        ]")
            await pwn.edit_text("ETR: > sec[ββββββββββββββββββββ]")
            await pwn.delete() 
            hawk = await ryui.reply_text(
                f"δΈβγοΈ» **ΦΙ¦Ι¨ΥΌΙ¨Ι’ΗΚΙ¨_RΚΚΣ** οΈ»γβδΈ"
                "[π¦](https://telegra.ph/file/8bdbb1581cc0914586fe2.jpg)[π¦]\n"
                "**ΙͺΙ΄α΄ α΄ΚΙͺα΄ ΙͺΙ΄α΄α΄α΄.α΄Κα΄α΄κ±α΄ Κα΄α΄Κα΄α΄α΄ κ°ΙͺΚα΄ α΄Κα΄α΄.**",    
                                disable_web_page_preview=True
                                )
        await wait_before_rm((hawk, ryui), Kill_Time)
    
    
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
