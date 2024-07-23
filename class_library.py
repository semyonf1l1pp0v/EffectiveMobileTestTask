from class_book import *


class Library:
    __books: dict = {}

    def __init__(self, book: Book, book_id: int = 0) -> None:
        self.set_books(book_id, book)

    def set_books(self, book_id: int, book: Book) -> None:
        self.__books[book_id] = book

    def get_books(self) -> dict:
        return self.__books

    def add_book(self, new_book_id: int, new_book: Book) -> None:
        self.__books[new_book_id] = new_book

    def delete_book(self, id_to_delete: int) -> None:
        del self.__books[id_to_delete]

    def find_book_by_id(self, book_id: int) -> int:
        for book in self.get_books().items():
            if book[0] == book_id:
                return book[0]
        return -1

    def find_matching_books(self, characteristic) -> list:
        matching_books = []
        for book in self.get_books().items():
            if (book[1].get_title() == characteristic or
                    book[1].get_author() == characteristic or
                    str(book[1].get_year()) == characteristic):
                matching_books.append(book[1])
        return matching_books

    def change_book_status(self, id_to_modify_status: int, new_status: str) -> None:
        self.__books[id_to_modify_status].set_status(status=new_status)
