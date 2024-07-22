

choice = None
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
print("\nПрограмма завершена.")

