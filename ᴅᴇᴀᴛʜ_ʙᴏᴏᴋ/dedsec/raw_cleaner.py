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
from pyrogram import Client, filters
from pyrogram.methods.messages.download_media import DEFAULT_DOWNLOAD_DIR as fmedaddyy
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
                   & filters.command("raw", prefixes=DYNO_COMMAND)
                   ) 
async def clean_raw_pcm(client, ryui: Message):
    raw_hug = os.path.join(client.workdir, fmedaddyy)
    all_fn: list[str] = os.listdir(raw_hug)
    for track in ded.playlist[:2]:
        track_fn = f"{track.audio.file_unique_id}.raw"
        if track_fn in all_fn:
            all_fn.remove(track_fn)
    files = 0
    if all_fn:
        for fn in all_fn:
            if fn.endswith(".raw"):
                files += 1
                os.remove(os.path.join(raw_hug, fn))             
    hawk = await ryui.reply_text(
        f"δΈβγοΈ» **ΦΙ¦Ι¨ΥΌΙ¨Ι’ΗΚΙ¨_RΚΚΣ** οΈ»γβδΈ\n Ι΄α΄α΄Κα΄Κ α΄κ° α΄Κα΄α΄Ι΄α΄α΄ α΄α΄α΄α΄ κ°ΙͺΚα΄: **{files}**"
                    )
    await ryui.delete()
    await wait_before_rm((hawk, ryui), Kill_Time)
    return
    
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
