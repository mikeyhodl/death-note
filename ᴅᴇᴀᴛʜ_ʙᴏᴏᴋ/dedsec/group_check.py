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
from pyrogram import Client, filters, emoji
from pyrogram.types import Message
from α΄ α΄Ιͺα΄α΄_Ιͺα΄.typos import *
from α΄ α΄Ιͺα΄α΄_Ιͺα΄.vocal import *
from Ι΄α΄α΄α΄Κα΄α΄α΄.notes import *
from α΄Ιͺκ±α΄_α΄α΄α΄Ι΄α΄.life_death import *
from α΄ΙͺΚα΄_ΚΙͺΙ’Κα΄.pyro_auth import Li

"""
 \____/ /  \ \____/ /  \ \____/ /  \ \____/ /  \ \____/ /  \ \____/ / 
 / __ \ \__/ / __ \ \__/ / __ \ \__/ / __ \ \__/ / __ \ \__/ / __ \ \_
"""

DYNO_COMMAND = Li.DYNO_COMMAND

@Client.on_message(demon_killer_sigki
                   & senzo_kryo_ni
                   & filters.command("group", prefixes=DYNO_COMMAND)
                   )                     
async def list_voice_chat(client, ryui: Message):
    voice_chatting = ded.voice_chatting
    if voice_chatting.is_connected:
        pwn = await ryui.reply_text("Syncing with @vrtxmusic", True)
        await pwn.edit_text("and it's servers...")
        await pwn.edit_text("ETR: > sec[ββββββ              ]")
        await pwn.edit_text("ETR: > sec[ββββββββββββ        ]")
        await pwn.edit_text("ETR: > sec[ββββββββββββββββββββ]")         
        chat_id = int("-100" + str(voice_chatting.full_chat.id))
        await pwn.delete()
        chat = await client.get_chat(chat_id)
        hawk = await ryui.reply_photo(
            "https://telegra.ph/file/2e419eca28153982c5e54.jpg",   
            caption=f"[π¦]δΈβγοΈ» **ΦΙ¦Ι¨ΥΌΙ¨Ι’ΗΚΙ¨_RΚΚΣ** οΈ»γβδΈ[π¦]\n\nα΄α΄ΚΚα΄Ι΄α΄ΚΚ ΙͺΙ΄ α΄Κα΄ α΄ α΄Ιͺα΄α΄ α΄Κα΄α΄ α΄κ°: \n**{chat.title}**"
            )   
    else:
        hawk = await ryui.reply_text("β³α΄‘α΄Ιͺα΄ΙͺΙ΄Ι’ α΄α΄ Κα΄ α΄Κα΄Ι’Ι’α΄α΄ ΙͺΙ΄ α΄ Ι’Κα΄α΄α΄ α΄ α΄Ιͺα΄α΄ α΄Κα΄α΄βοΈ")
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
