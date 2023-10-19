import os

from dotenv import load_dotenv
from tg_api import (
    InlineKeyboardButton,
    InlineKeyboardMarkup,
    SendBytesPhotoRequest,
    SendMessageRequest,
    SyncTgClient,
)


def send_message(token, tg_chat_id):
    #  Отправить себе текстовое сообщение от имени tg-бота
    with SyncTgClient.setup(token):
        tg_request = SendMessageRequest(
            chat_id=tg_chat_id, text="Message proofs high level usage."
        )
        tg_request.send()


def send_message_with_keyboard(token, tg_chat_id):
    # Отправить себе текстовое сообщение с кнопками от имени tg-бота
    keyboard = InlineKeyboardMarkup(
        inline_keyboard=[
            [
                InlineKeyboardButton(text="button_1", callback_data="test"),
                InlineKeyboardButton(text="button_2", callback_data="test"),
            ],
        ],
    )
    with SyncTgClient.setup(token):
        tg_request = SendMessageRequest(
            chat_id=tg_chat_id,
            text="Message proofs keyboard support.",
            reply_markup=keyboard,
        )
        tg_request.send()


def send_photo(token, tg_chat_id, photo_filename):
    #  Отправить себе сообщение с картинкой от имени tg-бота
    with SyncTgClient.setup(token):
        with open(photo_filename, "rb") as f:
            photo_content = f.read()
        tg_request = SendBytesPhotoRequest(
            chat_id=tg_chat_id, photo=photo_content, filename=photo_filename
        )
        tg_request.send()


def main():
    load_dotenv()
    token = os.environ["TG_BOT_TOKEN"]
    tg_chat_id = os.environ["TG_CHAT_ID"]

    send_message(token, tg_chat_id)

    send_message_with_keyboard(token, tg_chat_id)

    send_photo(token, tg_chat_id, "image.jpeg")


if __name__ == "__main__":
    main()
