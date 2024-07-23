from class_book import *


class Library:
    __books: dict = None

    def __init__(self, book_id: int, book: Book) -> None:
        self.set_books(book_id, book)

    def set_books(self, book_id: int, book: Book) -> None:
        self.__books[book_id] = book

    def get_books(self) -> dict:
        return self.__books

    def add_book(self, new_book_id: int, new_book: Book) -> None:
        self.__books[new_book_id] = new_book

    def delete_book(self, id_to_delete: int) -> bool:
        if self.find_book(id_to_delete) != -1:
            del self.__books[id_to_delete]
            return True
        return False

    def find_book(self, characteristic) -> int:
        for book in self.get_books().items():
            if book[1].get_title() == characteristic or book[1].get_author() == characteristic or book[1].get_year() == characteristic:
                return book[0]
        return -1

    # def show_all_books(self):
    #     for book in self.get_books().items():
    #         pass

    def change_book_status(self, id_to_modify_status: int, new_status: str) -> bool:
        if self.find_book(id_to_modify_status) != -1:
            self.__books[id_to_modify_status].set_status(status=new_status)
            return True
        return False


