from class_library import *


def dialog_add_book(library: Library) -> None:
    title = input("\nВведите название книги: ")
    author = input("Введите автора книги: ")
    year = int(input("Введите год выхода книги: "))
    new_book = Book(book_id=book_id, title=title, author=author, year=year)
    library.add_book(new_book_id=book_id, new_book=new_book)


def dialog_delete_book(library: Library) -> None:
    id_book_to_delete = int(input("\nВведите id книги, которую хотите удалить: "))
    if library.delete_book(id_book_to_delete):
        print("\nКнига успешно удалена")
    else:
        print("\nКниги с таким id нет в библиотеке")


def dialog_show_all_books(library: Library) -> None:
    print("{:<10} {:<15} {:<15} {:<15} {:<10}".format('ID', 'Название', 'Автор', 'Год издания', 'Статус'))
    for book in library.get_books().items():
        print("{:<10} {:<15} {:<15} {:<15} {:<10}\n".format(book[1].get_id(), book[1].get_title(), book[1].get_author(),
                                                            book[1].get_year(), book[1].get_status()))


choice = None
book_id = 1
our_library = Library(Book())
our_library.delete_book(0)
while choice != 0:
    print("1. Добавить книгу")
    print("2. Удалить книгу")
    print("3. Найти книгу")
    print("4. Показать все книги")
    print("5. Изменить статус книги")
    print("0. Выйти")
    choice = int(input("\nВыберите действие: "))
    match choice:
        case 0:
            break
        case 1:
            dialog_add_book(library=our_library)
            book_id += 1
        case 2:
            dialog_delete_book(library=our_library)
        case 3:
            pass
        case 4:
            dialog_show_all_books(library=our_library)
        case 5:
            pass

print("\nПрограмма завершена.")
