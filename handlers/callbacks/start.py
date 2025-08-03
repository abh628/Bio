from bot.bot import app
from pyrogram import filters
from pyrogram.types import Message
from utils.language import get_message
from database.user_language import get_user_language
from config import START_IMG
from utils.inline_buttons import start_buttons
from database.users import store_user_data

@app.on_message(filters.command("start"))
async def start_command(client, message: Message):
    user = message.from_user
    full_name = f"{user.first_name or ''} {user.last_name or ''}".strip()
    await store_user_data(user.id, user.username, full_name)
    lang = await get_user_language(user.id)
    welcome_text = get_message(lang, "welcome_message").format(user=user.mention)
    await message.reply_photo(
        photo=START_IMG,
        caption=welcome_text,
        reply_markup=await start_buttons(user.id)
    )
