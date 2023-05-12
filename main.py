import logging

from load import *
from utils import get_insertable
from db.misc import update_data, get_info_from_db


@app.on_message(filters.command(commands=['refresh']))
async def refresh(client, message: Message):
    await message.reply('Userbot yangilanadi, kuting, bu bir necha daqiqa vaqt olishi mumkin')
    update_data(await get_insertable())
    await message.reply('Userbot muvaffaqiyatli yangilandi!')


@app.on_message(filters.regex(r"^\%\d+$"))
async def search_groups(client, message: Message):
    lst = []
    for i in get_info_from_db(int(message.text[1:])):
        url = (await app.get_chat(i[-2])).invite_link
        lst.append(f"[{i[-1]}]({url})")
    full_name = i[2]
    await message.edit(f"[{full_name}](https://t.me/{(await app.get_users([i[1]]))[0].username})",
                       parse_mode=parse_mode.ParseMode.MARKDOWN)
    await message.reply("\n".join(lst))


app.run()
