import os

from dotenv import load_dotenv
from tg_api import SendMessageRequest, SyncTgClient


def main():
    load_dotenv()
    token = os.environ["TG_BOT_TOKEN"]
    tg_chat_id = os.environ["TG_CHAT_ID"]

    with SyncTgClient.setup(token):
        tg_request = SendMessageRequest(
            chat_id=tg_chat_id, text="Message proofs high level usage."
        )
        tg_request.send()


if __name__ == "__main__":
    main()
