while True:
    print("====== TO DO LIST ======")
    print("1. Добавить задачу")
    print("2. Показать задачи")
    print("3. Удалить задачу")
    print("4. Выход")

    choice = input("Выберите действие: ")

    if choice == "1":
        task = input("Введите задачу: ")

        file = open("todo.txt", "a", encoding="utf-8")
        file.write(task + "\n")
        file.close()

        print("Задача сохранена")

    elif choice == "2":
        try:
            file = open("todo.txt", "r", encoding="utf-8")
            tasks = file.readlines()
            file.close()

            print("\n====== Список задач ======")
            print(f"Всего задач: {len(tasks)}")

            for number, task in enumerate(tasks, start=1):
                print(f"{number}. {task.strip()}")

        except:
            print("Список задач пока пуст.")

    elif choice == "3":
        try:
            file = open("todo.txt", "r", encoding="utf-8")
            tasks = file.readlines()
            file.close()

            number = int(input("Введите номер задачи для удаления: "))
            if 1 <= number <= len(tasks):
                del tasks[number - 1]
            else:
                print("Такой задачи нет")
                continue

            file = open("todo.txt", "w", encoding="utf-8")
            for task in tasks:
                file.write(task)
            file.close()

            print("Задача удалена")

        except ValueError:
            print("Введите номер цифрами")

        except FileNotFoundError:
            print("Список задач пока пуст.")

    elif choice == "4":
        print("Программа завершена")
        break

    else:
        print("Такого пункта нет")