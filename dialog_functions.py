from class_library import *


def dialog_add_book(library: Library, new_book_id: int) -> None:
    title = input("\nВведите название книги: ")
    author = input("Введите автора книги: ")
    year = int(input("Введите год выхода книги: "))
    new_book = Book(book_id=new_book_id, title=title, author=author, year=year)
    library.add_book(new_book_id=new_book_id, new_book=new_book)
    print("\nКнига успешно добавлена")


def dialog_delete_book(library: Library) -> None:
    id_book_to_delete = int(input("\nВведите id книги, которую хотите удалить: "))
    if library.find_book_by_id(book_id=id_book_to_delete) != -1:
        library.delete_book(id_to_delete=id_book_to_delete)
        print("\nКнига успешно удалена")
    else:
        print("\nКниги с таким id нет в библиотеке")


def dialog_find_book(library: Library):
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
    print("{:<10} {:<15} {:<15} {:<15} {:<10}".format('ID', 'Название', 'Автор', 'Год издания', 'Статус'))
    for book in library.get_books().items():
        print("{:<10} {:<15} {:<15} {:<15} {:<10}".format(book[1].get_id(), book[1].get_title(), book[1].get_author(),
                                                          book[1].get_year(), book[1].get_status()))


def dialog_change_book_status(library: Library) -> None:
    id_book_to_change_status = int(input("Введите id книги, статус которой хотите изменить: "))
    if library.find_book_by_id(book_id=id_book_to_change_status) != -1:
        if library.get_books()[id_book_to_change_status].get_status() == "В наличии":
            library.change_book_status(id_to_modify_status=id_book_to_change_status, new_status="Выдана")
        else:
            library.change_book_status(id_to_modify_status=id_book_to_change_status, new_status="В наличии")
        print("\nСтатус книги успешно изменен")
    else:
        print("\nКниги с таким id нет в библиотеке")
