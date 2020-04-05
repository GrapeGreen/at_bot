import common
import requests


def send_message(message):
    telegram_query = requests.post(
        'https://api.telegram.org/bot{}/sendMessage?text={}&chat_id={}'.format(
            common.AT_TELEGRAM_BOT_TOKEN,
            message,
            common.AT_TELEGRAM_CHANNEL
        )
    )

    assert telegram_query.status_code == 200
