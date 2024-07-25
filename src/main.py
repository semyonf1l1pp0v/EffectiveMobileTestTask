from src.dialog_functions import *

choice = None   # Переменная для хранения числа, обозначающего опцию, введенного пользователем
book_id = 1
our_library = Library(Book())
our_library.delete_book(0)

"""
Ниже приведен код меню для взаимодействия пользователя с программой.
Введены цифры от 0 до 6 - выполняется соответствующая опция.
Введено не целое и/или отрицательное число - пользователя просят повторить ввод. 
Программа завершается при выборе опции 0. 
"""

while choice != 0:
    print("\n1. Добавить книгу")
    print("2. Удалить книгу")
    print("3. Найти книгу")
    print("4. Показать все книги")
    print("5. Изменить статус книги")
    print("6. Записать данные о книгах в текстовый файл")
    print("0. Выйти")
    try:
        choice = int(input("\nВыберите действие: "))
    except ValueError:
        print("\nОпция выбрана неверно - введите целое число от 0 до 6")
        continue
    match choice:
        case 0:
            break
        case 1:
            dialog_add_book(library=our_library, new_book_id=book_id)
            book_id += 1
        case 2:
            dialog_delete_book(library=our_library)
        case 3:
            dialog_find_book(library=our_library)
        case 4:
            dialog_show_all_books(library=our_library)
        case 5:
            dialog_change_book_status(library=our_library)
        case 6:
            dialog_write_info_to_file(library=our_library)

print("\nПрограмма завершена.")
