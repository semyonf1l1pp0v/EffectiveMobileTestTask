from class_library import *


def dialog_add_book():
    title = input("Введите название книги: ")
    author = input("Введите автора книги: ")
    year = int(input("Введите год выхода книги: "))
    new_book = Book(book_id=book_id, title=title, author=author, year=year)
    library.add_book(book_id, new_book)


def dialog_show_all_books():
    print(f"ID\t\t"
          f"Название\t\t"
          f"Автор\t\t"
          f"Год издания\t\t"
          f"Статус\n")
    for book in library.get_books().items():
        print(f"{book[1].get_id()}\t\t"
              f"{book[1].get_title()}\t\t"
              f"{book[1].get_author()}\t\t"
              f"{book[1].get_year()}\t\t"
              f"{book[1].get_status()}\n")


choice = None
book_id = 1
library = Library(Book())
library.delete_book(0)
while choice != 0:
    print("1. Добавить книгу")
    print("2. Удалить книгу")
    print("3. Найти книгу")
    print("4. Показать все книги")
    print("5. Изменить статус книги")
    print("0. Выйти")
    choice = int(input("Выберите действие: "))
    match choice:
        case 0:
            break
        case 1:
            dialog_add_book()
            book_id += 1
        case 2:
            pass
        case 3:
            pass
        case 4:
            dialog_show_all_books()
        case 5:
            pass

print("\nПрограмма завершена.")
