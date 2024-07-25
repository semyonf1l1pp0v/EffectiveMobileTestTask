from class_book import *


class Library:
    """Класс Библиотека, состоящий из словаря __books, где ключ - id (число), значение - экземпляр класса Книга"""
    __books: dict = {}

    def __init__(self, book: Book, book_id: int = 0) -> None:
        """Конструктор класса Библиотека"""
        self.set_books(book_id, book)

    def set_books(self, book_id: int, book: Book) -> None:
        """"Сеттер для атрибута books класса Библиотека"""
        self.__books[book_id] = book

    def get_books(self) -> dict:
        """"Геттер для атрибута books класса Библиотека"""
        return self.__books

    def add_book(self, new_book_id: int, new_book: Book) -> None:
        """"Метод для добавления Книги в Библиотеку по id"""
        self.__books[new_book_id] = new_book

    def delete_book(self, id_to_delete: int) -> None:
        """Метод для удаления Книги из Библиотеки по id"""
        del self.__books[id_to_delete]

    def find_book_by_id(self, book_id: int) -> int:
        """Метод для поиска Книги в Библиотеке по id"""
        for book in self.get_books().items():
            if book[0] == book_id:
                return book[0]
        return -1

    def find_matching_books(self, characteristic: str) -> list[Book]:
        """Метод для поиска в Библиотеке подходящих Книг (по названию, автору или году выпуска)"""
        matching_books = []
        for book in self.get_books().items():
            if (book[1].get_title() == characteristic or
                    book[1].get_author() == characteristic or
                    str(book[1].get_year()) == characteristic):
                matching_books.append(book[1])
        return matching_books

    def change_book_status(self, id_to_modify_status: int, new_status: str) -> None:
        """Метод для изменения статуса Книги"""
        self.__books[id_to_modify_status].set_status(status=new_status)
