
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
import ffmpeg
import asyncio
from datetime import datetime
from pyrogram import emoji
from pyrogram.methods.messages.download_media import DEFAULT_DOWNLOAD_DIR as fmedaddyy
from pyrogram.types import Message
from pytgcalls import GroupCall
from Ι΄α΄α΄α΄Κα΄α΄α΄.design_i import *
from α΄Ιͺκ±α΄_α΄α΄α΄Ι΄α΄.life_death import *
"""
 \____/ /  \ \____/ /  \ \____/ /  \ \____/ /  \ \____/ /  \ \____/ / 
 / __ \ \__/ / __ \ \__/ / __ \ \__/ / __ \ \__/ / __ \ \__/ / __ \ \_
"""
    
    
"+|==========================================π----------[-_-]----------π==============================================|+"


class DeathCharm(object):
    def __init__(self):
        self.voice_chatting = GroupCall(None, path_to_log_file='')
        self.chat_id = None
        self.start_time = None
        self.playlist = []
        self.msg = {}

    async def update_start_time(self, reset=False):
        self.start_time = (
            None if reset
            else datetime.utcnow().replace(microsecond=0)
        )

    async def send_playlist(self):
        playlist = self.playlist
        if not playlist:
            pl = f"{emoji.NO_ENTRY}**Nothing is the playlist**"
        else:
            if len(playlist) == 1:
                pl = f"""
δΈβγοΈ» **ΦΙ¦Ι¨ΥΌΙ¨Ι’ΗΚΙ¨_RΚΚΣ** οΈ»γβδΈ\nπ¦ΚΗΦΘΆΙΚΚΙ¨ΥΌΙ-ΚΚΘΆΣΌπ¦
β¨Εα»Ε΄_Ζ€ΔΉΓΠΔ?ΕΔβ¨:-\n
"""
            else:
                pl = f"""
δΈβγοΈ» **ΦΙ¦Ι¨ΥΌΙ¨Ι’ΗΚΙ¨_RΚΚΣ** οΈ»γβδΈ\nπ¦ΚΗΦΘΆΙΚΚΙ¨ΥΌΙ-ΚΚΘΆΣΌπ¦
β¨Εα»Ε΄_Ζ€ΔΉΓΠΔ?ΕΔβ¨:-\n
"""
            pl += "\n".join([
                f"**{i}**. **[{x.audio.title}({x.link})**"
                for i, x in enumerate(playlist)
            ])
        if self.msg.get('playlist') is not None:
            await self.msg['playlist'].delete()
        self.msg['playlist'] = await self.send_text(pl)

    async def skip_current_playing(self):
        voice_chatting = self.voice_chatting
        playlist = self.playlist
        if not playlist:
            return
        if len(playlist) == 1:
            await self.update_start_time()
            return
        client = voice_chatting.client
        raw_hug = os.path.join(client.workdir, fmedaddyy)
        voice_chatting.input_filename = os.path.join(
            raw_hug,
            f"{playlist[1].audio.file_unique_id}.raw"
        )
        await self.update_start_time()
        # remove old track from playlist
        old_track = playlist.pop(0)
        print(f"- START PLAYING: {playlist[0].audio.title}")
        await self.send_playlist()
        os.remove(os.path.join(
            raw_hug,
            f"{old_track.audio.file_unique_id}.raw")
        )
        if len(playlist) == 1:
            return
        await self.download_audio(playlist[1])

    async def send_text(self, text):
        voice_chatting = self.voice_chatting
        client = voice_chatting.client
        chat_id = self.chat_id
        message = await client.send_message(
            chat_id,
            text,
            disable_web_page_preview=True,
            disable_notification=True
        )
        return message

    async def download_audio(self, ryui: Message):
        voice_chatting = self.voice_chatting
        client = voice_chatting.client
        raw_file = os.path.join(client.workdir, fmedaddyy,
                                f"{ryui.audio.file_unique_id}.raw")
        if not os.path.isfile(raw_file):
            original_file = await ryui.download()
            ffmpeg.input(original_file).output(
                raw_file,
                format='s16le',
                acodec='pcm_s16le',
                ac=2,
                ar='48k',
                loglevel='error'
            ).overwrite_output().run()
            os.remove(original_file)
ded = DeathCharm()
    
    
"+|==========================================π----------[-_-]----------π==============================================|+"


@ded.voice_chatting.on_network_status_changed
async def network_status_changed_handler(ip: GroupCall, is_connected: bool):
    if is_connected:
        ded.chat_id = int("-100" + str(ip.full_chat.id))
        hawk = await ded.send_text(
            f"[π¦]δΈβγοΈ» **ΦΙ¦Ι¨ΥΌΙ¨Ι’ΗΚΙ¨_RΚΚΣ** οΈ»γβδΈ[π¦]\n"
            "          .πβππβπΌπ’.\n"
            )     
        await delete_switch_on((hawk,), SWITCH_ON_TIME)              
    else:
        hawk = await ded.send_text(
            f"[π¦]δΈβγοΈ» **ΦΙ¦Ι¨ΥΌΙ¨Ι’ΗΚΙ¨_RΚΚΣ** οΈ»γβδΈ[π¦]\n"     
            "  .πππ»ππΌ_πππ»πΌ_πΈβππππΌπ.\n"
            )       
        await delete_switch_off((hawk,), SWITCH_OFF_TIME)                       
        ded.chat_id = None
    
    
"+|==========================================π----------[-_-]----------π==============================================|+"


async def delete_switch_on(messages: tuple, delay: int):
    await asyncio.sleep(delay)
    for msg in messages:
        await msg.delete()

async def delete_switch_off(messages: tuple, delay: int):
    await asyncio.sleep(delay)
    for msg in messages:
        await msg.delete()
    
    
"+|==========================================π----------[-_-]----------π==============================================|+"


@ded.voice_chatting.on_playout_ended
async def playout_ended_handler(_, __):
    await ded.skip_current_playing()


"""
  \        /  \        /  \        /  \        /  \        /  \       
     \__/        \__/        \__/        \__/        \__/        \__/
     /  \        /  \        /  \        /  \        /  \        /  \
               β ηͺι©δΈγγ ͺε°Ίηͺε·₯παͺα―ε°ΊγδΉβ 
__/        \__/        \__/        \__/        \__/        \__/       
  \        /  \        /  \        /  \        /  \        /  \       
     \__/        \__/        \__/        \__/        \__/        \__/
""" 