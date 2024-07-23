from dialog_functions import *

choice = None
book_id = 1
our_library = Library(Book())
our_library.delete_book(0)
while choice != 0:
    print("\n1. Добавить книгу")
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
            dialog_add_book(library=our_library, new_book_id=book_id)
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
