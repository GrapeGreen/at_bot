# -*- coding: utf-8 -*-

import requests
from bs4 import BeautifulSoup
import dateutil.parser
import datetime, time

token = '655927459:AAHbkV9bwjN8ipCat6NNLTo314TC7Vro_D8'

def book_info(url):
    r = requests.get(url)
    if r.status_code != 200:
        return None
    soup = BeautifulSoup(r.text, features = 'lxml')
    title = soup.title.string.replace(' - читать книгу в онлайн-библиотеке', '')
    values = {'title' : title}
    chapters = []
    for chapter in soup.find('div', 'tab-content book-tab-content').find_all('li'):
        chapter_dict = {}
        subtitle = chapter.find('a')
        if subtitle is not None:
            name = subtitle.string
            link = subtitle.get('href')
            chapter_dict['link'] = link
        else:
            name = chapter.find('span').string
        chapter_dict['name'] = name
        chapter_dict['date'] = chapter.find('span', 'hint-top-right').get('data-time')#.split('T')[0]
        chapters.append(chapter_dict)
    values['chapters'] = chapters
    return values


def send_update(last_upd):
    last_upd = dateutil.parser.parse(last_upd)
    now = datetime.datetime.now(tz = datetime.timezone.utc)
    return (now - last_upd) <= datetime.timedelta(hours = 0.2)


def send_message(chat_id, message):
    requests.get(
        'https://api.telegram.org/bot{}/sendMessage?text={}&chat_id={}'.format(
            token,
            message,
            chat_id
        )
    )


chat_ids = ['202386422', '332427326']
book_urls = ['https://author.today/work/33438', 'https://author.today/work/32389']

while True:
    try:
        for book_url in book_urls:
            book = book_info(book_url)
            if book is None or len(book['chapters']) == 0:
                continue
            chapter = book['chapters'][-1]
            title = book['title']
            last_upd, name = chapter['date'], chapter['name']
            if send_update(last_upd):
                for chat_id in chat_ids:
                    send_message(chat_id, '{}\n{}\n{}'.format(title, name, book_url))
        time.sleep(650)
    except:
        pass