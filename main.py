import book
import common
import db
import requests
import sender


def main():
    with requests.Session() as session:
        login_query = session.post(common.AT_LOGIN_URL, data={'Login': common.AT_LOGIN, 'Password': common.AT_PASSWORD})
        assert login_query.status_code == 200

        books = []
        for book_url in common.AT_BOOK_URLS:
            book_query = session.get(book_url)
            assert book_query.status_code == 200
            books.append(book.Book(book_url, book_query.text))

        for b in books:
            last_update_timestamp = b.get_last_update_timestamp()
            if db.get_last_update_timestamp(b.link) != last_update_timestamp:
                print(db.get_last_update_timestamp(b.link), last_update_timestamp)
                db.set_last_update_timestamp(b.link, last_update_timestamp)
                sender.send_message(str(b))


if __name__ == "__main__":
    main()
