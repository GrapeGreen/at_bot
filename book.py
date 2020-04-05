# -*- coding: utf-8 -*-

import common
from bs4 import BeautifulSoup


class BookChapter:
    def __init__(self, chapter_li):
        chapter_info = chapter_li.find('a')
        self.name = chapter_info.string
        self.link = chapter_info.get('href')
        assert self.link is not None
        self.date = chapter_li.find('span', 'hint-top-right').get('data-time')

    def __str__(self):
        return common.at_link(self.link)


class Book:
    def __init__(self, link, book_html):
        self.link = link
        soup = BeautifulSoup(book_html, features = 'lxml')
        self.title, self.author = self.parse_title_and_author(soup.title.string)
        self.chapters = self.create_chapters(soup.find('ul', 'list-unstyled table-of-content').find_all('li'))
        assert self.chapters

    @staticmethod
    def parse_title_and_author(title):
        chunks = title.split(' - ')
        assert 2 <= len(chunks) <= 3
        return chunks[0].strip('"'), chunks[1]

    @staticmethod
    def create_chapters(chapters_list):
        chapters = []
        for chapter in chapters_list:
            chapters.append(BookChapter(chapter))
        return chapters

    def get_last_update_timestamp(self):
        return self.chapters[-1].date

    def __str__(self):
        return '{}\n{}\n{}'.format(self.author, self.title, str(self.chapters[-1]))
