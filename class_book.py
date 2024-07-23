class Book:
    __book_id: int = None
    __title: str = None
    __author: str = None
    __year: int = None
    __status: str = None

    def __init__(self, book_id: int, title: str, author: str, year: int, status: str = "В наличии") -> None:
        self.set_id(book_id)
        self.set_title(title)
        self.set_author(author)
        self.set_year(year)
        self.set_status(status)

    def set_id(self, book_id: int) -> None:
        self.__book_id = book_id

    def set_title(self, title: str) -> None:
        self.__title = title

    def set_author(self, author: str) -> None:
        self.__author = author

    def set_year(self, year: int) -> None:
        self.__year = year

    def set_status(self, status: str) -> None:
        self.__status = status

    def get_id(self) -> int:
        return self.__book_id

    def get_title(self) -> str:
        return self.__title

    def get_author(self) -> str:
        return self.__author

    def get_year(self) -> int:
        return self.__year

    def get_status(self) -> str:
        return self.__status
