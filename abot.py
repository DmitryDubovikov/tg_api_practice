import asyncio
import os

import aiofiles
import httpx
from dotenv import load_dotenv
from tg_api import (
    AsyncTgClient,
    InlineKeyboardButton,
    InlineKeyboardMarkup,
    SendBytesPhotoRequest,
    SendMessageRequest,
)


async def asend_message(token, tg_chat_id):
    #  Отправить себе текстовое сообщение от имени tg-бота
    async with AsyncTgClient.setup(token):
        tg_request = SendMessageRequest(
            chat_id=tg_chat_id, text="Message proofs high level API usage."
        )
        # вызов метода поднимет исключение TgRuntimeError если сервере Telegram ответит HTTP статусом != 2xx
        await tg_request.asend()


async def asend_message_with_keyboard(token, tg_chat_id):
    # Отправить себе текстовое сообщение с кнопками от имени tg-бота
    keyboard = InlineKeyboardMarkup(
        inline_keyboard=[
            [
                InlineKeyboardButton(text="button_1", callback_data="test"),
                InlineKeyboardButton(text="button_2", callback_data="test"),
            ],
        ],
    )
    async with AsyncTgClient.setup(token):
        tg_request = SendMessageRequest(
            chat_id=tg_chat_id,
            text="Message proofs keyboard support.",
            reply_markup=keyboard,
        )
        await tg_request.asend()


async def asend_photo(token, tg_chat_id, photo_filename):
    #  Отправить себе сообщение с картинкой от имени tg-бота
    async with AsyncTgClient.setup(token):
        async with aiofiles.open(photo_filename, "rb") as f:
            photo_content = await f.read()
        tg_request = SendBytesPhotoRequest(
            chat_id=tg_chat_id, photo=photo_content, filename=photo_filename
        )
        await tg_request.asend()


async def asend_message_with_httpx(token, tg_chat_id):
    url = f"https://api.telegram.org/bot{token}/sendMessage"
    async with httpx.AsyncClient() as client:
        response = await client.post(
            url, params={"chat_id": tg_chat_id, "text": "hello from httpx"}
        )
        return response


async def main():
    load_dotenv()
    token = os.environ["TG_BOT_TOKEN"]
    tg_chat_id = os.environ["TG_CHAT_ID"]

    # await asend_message(token, tg_chat_id)
    #
    # await asend_message_with_keyboard(token, tg_chat_id)
    #
    # await asend_photo(token, tg_chat_id, "image.jpeg")

    await asend_message_with_httpx(token, tg_chat_id)


if __name__ == "__main__":
    asyncio.run(main())
