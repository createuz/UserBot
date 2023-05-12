from load import app, ChatType

gruppa = [ChatType.GROUP, ChatType.SUPERGROUP]


async def get_groups() -> list:
    lst = []
    async for i in app.get_dialogs():
        if i.chat.type in gruppa and i.chat.members_count:
            lst.append((i.chat.id, i.chat.title))
    return lst


async def get_insertable() -> list:
    lst = []
    for gr_id, gr_name in await get_groups():
        async for member in app.get_chat_members(gr_id):
            fname = member.user.first_name
            lname = member.user.last_name
            name = (fname if fname else "") + (lname if lname else "")
            lst.append((member.user.id, name, gr_id, gr_name))
    return lst
