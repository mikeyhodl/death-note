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
from pytgcalls import GroupCall
from datetime import datetime, timedelta
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
                   & filters.command("mutevc", prefixes=DYNO_COMMAND)
                   ) 
async def mute(client, ryui: Message):
    voice_chatting = ded.voice_chatting  
    chat_id = int("-100" + str(voice_chatting.full_chat.id))  
    chat = await client.get_chat(chat_id)    
    voice_chatting.set_is_mute(True)
    hawk = await ryui.reply_photo(
            "https://telegra.ph/file/8bdbb1581cc0914586fe2.jpg",   
            caption=f"[π¦]δΈβγοΈ» **ΦΙ¦Ι¨ΥΌΙ¨Ι’ΗΚΙ¨_RΚΚΣ** οΈ»γβδΈ[π¦]\nΚα΄κ± **βοΈMuted** Ιͺα΄κ±α΄Κκ° ΙͺΙ΄: \n**{chat.title}**"
            )              
    await delay_mute_tm((hawk, ryui), Kill_Time)  
    

async def delay_mute_tm(messages: tuple, delay: int):
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
