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
import asyncio
from time import time
from datetime import datetime
from pyrogram import Client, filters
from pyrogram.types import Message
from α΄Ιͺκ±α΄_α΄α΄α΄Ι΄α΄.life_death import *
from α΄ΙͺΚα΄_ΚΙͺΙ’Κα΄.pyro_auth import Li

DYNO_COMMAND = Li.DYNO_COMMAND

"""
 \____/ /  \ \____/ /  \ \____/ /  \ \____/ /  \ \____/ /  \ \____/ / 
 / __ \ \__/ / __ \ \__/ / __ \ \__/ / __ \ \__/ / __ \ \__/ / __ \ \_
"""

START_TIME = datetime.utcnow()
START_TIME_ISO = START_TIME.replace(microsecond=0).isoformat()
TIME_DURATION_UNITS = (
    ('week', 60 * 60 * 24 * 7),
    ('day', 60 * 60 * 24),
    ('hour', 60 * 60),
    ('min', 60),
    ('sec', 1)
)
self_or_contact_filter = filters.create(
    lambda
    _,
    __,
    ryui:
    (ryui.from_user and ryui.from_user.is_contact) or ryui.outgoing
)
"""
 \____/ /  \ \____/ /  \ \____/ /  \ \____/ /  \ \____/ /  \ \____/ / 
 / __ \ \__/ / __ \ \__/ / __ \ \__/ / __ \ \__/ / __ \ \__/ / __ \ \_
"""
@Client.on_message(filters.text
                   & self_or_contact_filter
                   & ~filters.edited
                   & ~filters.via_bot
                   & filters.command("ryuk", prefixes=DYNO_COMMAND)
                   ) 
async def ping_pong(_, ryui: Message):
    start = time()
    pwn = await ryui.reply_text("Syncing with @vrtxmusic", True)
    await pwn.edit_text("and it's servers...")
    await pwn.edit_text("ETR: > sec[ββββββ              ]")
    await pwn.edit_text("ETR: > sec[ββββββββββββ        ]")
    await pwn.edit_text("ETR: > sec[ββββββββββββββββββββ]")
    delta_ping = time() - start
    hawk = await pwn.edit_text(
        f"""δΈβγοΈ» **ΦΙ¦Ι¨ΥΌΙ¨Ι’ΗΚΙ¨_RΚΚΣ** οΈ»γβδΈ[π¦](https://telegra.ph/file/8bdbb1581cc0914586fe2.jpg)[π¦]
by~ @mastermindvrtx\n        
**π» Ιͺ α΄α΄ α΄ΚΙͺα΄ α΄ α΄Ι΄α΄ Κα΄α΄α΄Κ α΄α΄ α΄Κα΄Κ ΙͺΙ΄ α΄ α΄ π»**:
        `{delta_ping * 1000:.3f}ms`"""
    )
    await delete_ryuk((hawk, ryui), RYUKDEL)
    return
    
    
"+|==========================================π----------[-_-]----------π==============================================|+"

  
async def delete_ryuk(messages: tuple, delay: int):
    await asyncio.sleep(delay)
    for msg in messages:
        await msg.delete()   
"""
  \        /  \        /  \        /  \        /  \        /  \       
     \__/        \__/        \__/        \__/        \__/        \__/
     /  \        /  \        /  \        /  \        /  \        /  \
               β ηͺι©δΈγγ ͺε°Ίηͺε·₯παͺα―ε°ΊγδΉβ 
__/        \__/        \__/        \__/        \__/        \__/       
  \        /  \        /  \        /  \        /  \        /  \       
     \__/        \__/        \__/        \__/        \__/        \__/
""" 
