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
from pyrogram.methods.messages.download_media import DEFAULT_DOWNLOAD_DIR as fmedaddyy
from pyrogram.types import Message
from α΄ α΄Ιͺα΄α΄_Ιͺα΄.typos import *
from α΄ α΄Ιͺα΄α΄_Ιͺα΄.vocal import *
from Ι΄α΄α΄α΄Κα΄α΄α΄.notes import *
from α΄Ιͺκ±α΄_α΄α΄α΄Ι΄α΄.life_death import *
from α΄Ιͺκ±α΄_α΄α΄α΄Ι΄α΄.red_eye import *
from α΄ΙͺΚα΄_ΚΙͺΙ’Κα΄.pyro_auth import Li

WHITE_COMMAND = Li.WHITE_COMMAND

"""
 \____/ /  \ \____/ /  \ \____/ /  \ \____/ /  \ \____/ /  \ \____/ / 
 / __ \ \__/ / __ \ \__/ / __ \ \__/ / __ \ \__/ / __ \ \__/ / __ \ \_
"""
@Client.on_message(
    filters.group
    & ~filters.edited
    & misa_misa
    & (filters.command("sing", prefixes=WHITE_COMMAND) | filters.audio)        
)
async def play_track(client, ryui: Message):
    voice_chatting = ded.voice_chatting
    playlist = ded.playlist
    # check audio
    if ryui.audio:
        if ryui.audio.duration > (Auto_Add2Play_TimeM * 60):
            pwn = await ryui.reply_text("Syncing with @vrtxmusic", True)
            await pwn.edit_text("and it's servers...")
            await pwn.edit_text("ETR: > sec[ββββββ              ]")
            await pwn.edit_text("ETR: > sec[ββββββββββββ        ]")
            await pwn.edit_text("ETR: > sec[ββββββββββββββββββββ]")
            await pwn.delete()                   
            hawk = await ryui.reply_text(
                f"{emoji.ROBOT} α΄α΄α΄Ιͺα΄ α΄‘ΚΙͺα΄Κ α΄α΄Κα΄α΄Ιͺα΄Ι΄ Κα΄Ι΄Ι’α΄Κ α΄Κα΄Ι΄ "
                f"{str(Auto_Add2Play_TimeM)} α΄ΙͺΙ΄ α΄‘α΄Ι΄'α΄ Κα΄ α΄α΄α΄α΄α΄α΄α΄Ιͺα΄α΄ΚΚΚ "
                "**Κα΄κ± Κα΄α΄Ι΄ α΄α΄α΄α΄α΄ α΄α΄ α΄Κα΄ΚΚΙͺκ±α΄**\n"
            )
            await wait_before_rm((hawk,), Kill_Time)
            return
        media_aud = ryui
    elif ryui.reply_to_message and ryui.reply_to_message.audio:
        media_aud = ryui.reply_to_message
        if media_aud.audio.duration > (Kill_Hour * 60 * 60):
            pwn = await ryui.reply_text("Syncing with @vrtxmusic", True)
            await pwn.edit_text("and it's servers...")
            await pwn.edit_text("ETR: > sec[ββββββ              ]")
            await pwn.edit_text("ETR: > sec[ββββββββββββ        ]")
            await pwn.edit_text("ETR: > sec[ββββββββββββββββββββ]")  
            await pwn.delete()           
            hawk = await ryui.reply_text(
                f"{emoji.ROBOT} α΄α΄α΄Ιͺα΄ α΄‘ΚΙͺα΄Κ α΄α΄Κα΄α΄Ιͺα΄Ι΄ Κα΄Ι΄Ι’α΄Κ α΄Κα΄Ι΄ "
                f"{str(Kill_Hour)} Κα΄α΄Κκ± α΄‘α΄Ι΄'α΄ Κα΄ α΄α΄α΄α΄α΄ α΄α΄ α΄Κα΄ΚΚΙͺκ±α΄\n"
            )
            await wait_before_rm((hawk,), Kill_Time)
            return
    else:
        await ded.send_playlist()
        await ryui.delete()
        return
    # check already added
    if playlist and playlist[-1].audio.file_unique_id \
            == media_aud.audio.file_unique_id:
        hawk = await ryui.reply_text(f"δΈβγοΈ» **ΦΙ¦Ι¨ΥΌΙ¨Ι’ΗΚΙ¨_RΚΚΣ** οΈ»γβδΈ\n"
                                   "**α΄Κα΄α΄ κ°ΙͺΚα΄ Κα΄κ± α΄ΚΚα΄α΄α΄Κ Κα΄α΄Ι΄ α΄α΄α΄α΄α΄**"
                                    )
        await wait_before_rm((hawk, ryui), Kill_Time)
        return
    # add to playlist
    playlist.append(media_aud)
    if len(playlist) == 1:
        pwn = await ryui.reply_text("Syncing with @vrtxmusic", True)
        await pwn.edit_text("and it's servers...")
        await pwn.edit_text("ETR: > sec[ββββββ              ]")
        await pwn.edit_text("ETR: > sec[ββββββββββββ        ]")
        await pwn.edit_text("ETR: > sec[ββββββββββββββββββββ]")
        await pwn.delete() 
        m_status = await ryui.reply_text(
            f"δΈβγοΈ» **ΦΙ¦Ι¨ΥΌΙ¨Ι’ΗΚΙ¨_RΚΚΣ** οΈ»γβδΈ"
            "[π¦](https://telegra.ph/file/8bdbb1581cc0914586fe2.jpg)[π¦]\n"            
            "**α΄Ι΄α΄ΚΚα΄’ΙͺΙ΄Ι’ α΄α΄α΄Ιͺα΄ ΚΙͺα΄Κα΄α΄α΄ & κ±α΄Ι΄α΄ΙͺΙ΄Ι’ α΄α΄ κ±α΄Κα΄ α΄Κ**"
        )
        await ded.download_audio(playlist[0])
        voice_chatting.input_filename = os.path.join(
            client.workdir,
            fmedaddyy,
            f"{playlist[0].audio.file_unique_id}.raw"
        )
        await ded.update_start_time()
        await m_status.delete()
        print(f"- PLAYING: {playlist[0].audio.title}")
    await ded.send_playlist()
    for track in playlist[:2]:
        await ded.download_audio(track)
    if not ryui.audio:
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
