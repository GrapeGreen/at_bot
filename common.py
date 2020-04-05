import os


AT_PREFIX = 'https://author.today'


def at_link(link):
    return '{}/{}'.format(AT_PREFIX, link.lstrip('/'))


AT_BOOK_URLS = [
    at_link('work/59387'),
    at_link('work/60631')
]

AT_LOGIN_URL = at_link('account/login')

AT_LOGIN = os.environ.get('AT_LOGIN')

AT_PASSWORD = os.environ.get('AT_PASSWORD')

AT_TELEGRAM_CHANNEL = os.environ.get('AT_TELEGRAM_CHANNEL')

AT_TELEGRAM_BOT_TOKEN = os.environ.get('AT_TELEGRAM_BOT_TOKEN')
