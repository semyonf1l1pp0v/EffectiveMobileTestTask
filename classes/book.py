class Book:
    """Класс Книга, атрибуты - id, название, автор, год выпуска, статус (в наличии или выдана)"""
    __book_id: int = None
    __title: str = None
    __author: str = None
    __year: int = None
    __status: str = None

    def __init__(self, book_id: int = 0, title: str = "", author: str = "", year: int = 0, status: str = "В наличии") -> None:
        """Конструктор класса Книга"""
        self.set_id(book_id)
        self.set_title(title)
        self.set_author(author)
        self.set_year(year)
        self.set_status(status)

    def set_id(self, book_id: int) -> None:
        """Сеттер для атрибута id класса Книга"""
        self.__book_id = book_id

    def set_title(self, title: str) -> None:
        """Сеттер для атрибута название класса Книга"""
        self.__title = title

    def set_author(self, author: str) -> None:
        """Сеттер для атрибута автор класса Книга"""
        self.__author = author

    def set_year(self, year: int) -> None:
        """Сеттер для атрибута год выпуска класса Книга"""
        self.__year = year

    def set_status(self, status: str) -> None:
        """Сеттер для атрибута статус класса Книга"""
        self.__status = status

    def get_id(self) -> int:
        """Геттер для атрибута id класса Книга"""
        return self.__book_id

    def get_title(self) -> str:
        """Геттер для атрибута название класса Книга"""
        return self.__title

    def get_author(self) -> str:
        """Геттер для атрибута автор класса Книга"""
        return self.__author

    def get_year(self) -> int:
        """Геттер для атрибута год выпуска класса Книга"""
        return self.__year

    def get_status(self) -> str:
        """Геттер для атрибута статус класса Книга"""
        return self.__status
