from class_library import *


def dialog_add_book(library: Library, new_book_id: int) -> None:
    """Диалоговая функция для добавления Книги в Библиотеку"""
    title = input("\nВведите название книги: ")
    author = input("Введите автора книги: ")
    while True:
        try:
            year = int(input("Введите год выхода книги: "))
            if year > 0:
                break
            else:
                print("\nГод не может быть отрицательным, введите положительное целое число")
        except ValueError:
            print("\nГод указан неверно - введите целое число")
    new_book = Book(book_id=new_book_id, title=title, author=author, year=year)
    library.add_book(new_book_id=new_book_id, new_book=new_book)
    print("\nКнига успешно добавлена")


def dialog_delete_book(library: Library) -> None:
    """Диалоговая функция для удаления книги из Библиотеки по id"""
    while True:
        try:
            id_book_to_delete = int(input("\nВведите id книги, которую хотите удалить: "))
            if id_book_to_delete > 0:
                break
            else:
                print("\nID указан неверно - введите целое положительное число")
        except ValueError:
            print("\nID указан неверно - введите целое число")
    if library.find_book_by_id(book_id=id_book_to_delete) != -1:
        library.delete_book(id_to_delete=id_book_to_delete)
        print("\nКнига успешно удалена")
    else:
        print("\nКниги с таким id нет в библиотеке")


def dialog_find_book(library: Library):
    """Диалоговая функция для поиска Книг в Библиотеке по названию/автору/году, печатает все Книги с заданным
    значением атрибута (например, все Книги, выпущенные в 1999 году)"""
    parameter = input("Введите название книги, или ее автора, или год издания: ")
    matching_books = library.find_matching_books(characteristic=parameter)
    if matching_books:
        print("\nКниги по вашему запросу:")
        print("{:<10} {:<15} {:<15} {:<15} {:<10}".format('ID', 'Название', 'Автор', 'Год издания', 'Статус'))
        for book in matching_books:
            print(
                "{:<10} {:<15} {:<15} {:<15} {:<10}".format(book.get_id(), book.get_title(), book.get_author(),
                                                            book.get_year(), book.get_status()))
    else:
        print("Книг по вашему запросу не найдено")


def dialog_show_all_books(library: Library) -> None:
    """Диалоговая функция для вывода в консоль информации обо всех Книгах в Библиотеке"""
    print("{:<10} {:<15} {:<15} {:<15} {:<10}".format('ID', 'Название', 'Автор', 'Год издания', 'Статус'))
    for book in library.get_books().items():
        print("{:<10} {:<15} {:<15} {:<15} {:<10}".format(book[1].get_id(), book[1].get_title(), book[1].get_author(),
                                                          book[1].get_year(), book[1].get_status()))


def dialog_change_book_status(library: Library) -> None:
    """Диалоговая функция для изменения статуса Книги по id"""
    while True:
        try:
            id_book_to_change_status = int(input("Введите id книги, статус которой хотите изменить: "))
            if id_book_to_change_status > 0:
                break
            else:
                print("\nID указан неверно - введите целое положительное число")
        except ValueError:
            print("\nID указан неверно - введите целое число")
    if library.find_book_by_id(book_id=id_book_to_change_status) != -1:
        if library.get_books()[id_book_to_change_status].get_status() == "В наличии":
            library.change_book_status(id_to_modify_status=id_book_to_change_status, new_status="Выдана")
        else:
            library.change_book_status(id_to_modify_status=id_book_to_change_status, new_status="В наличии")
        print("\nСтатус книги успешно изменен")
    else:
        print("\nКниги с таким id нет в библиотеке")


def dialog_write_info_to_file(library: Library) -> None:
    """Диалоговая функция для записи информации обо всех Книгах в txt файл"""
    with open("output.txt", "w") as file:
        file.write("{:<10} {:<15} {:<15} {:<15} {:<10}".format('ID', 'Название', 'Автор', 'Год издания', 'Статус'))
        books = library.get_books().values()
        for book in books:
            file.write("\n{:<10} {:<15} {:<15} {:<15} {:<10}".format(book.get_id(), book.get_title(), book.get_author(),
                                                                     book.get_year(), book.get_status()))
    print("Данные о книгах успешно записаны в файл")
