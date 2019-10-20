from xtrabot import loader
import asyncio
TANNER = 79316791
TCOIN = -1001394158904

@loader.command(incoming=True)
async def handler(event):
    me = await event.client.get_me()
    if event.message.from_id != TANNER:
        return
    if "> exhausted miners:" not in event.message.message:
        return
    if "me.first_name" in event.message.message:
        return
    await asyncio.sleep(2)
    await event.client.send_message(TCOIN, "!mine")
