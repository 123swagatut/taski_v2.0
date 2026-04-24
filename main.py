def show_tasks(tasks):
    if not tasks:
        print("\nСписок задач пуст.")
    else:
        print("\n--- Текущие задачи ---")
        for i, item in enumerate(tasks, 1):
            print(f"{i}. {item['task']} [Приоритет: {item['priority']}]")

def add_task(tasks):
    name = input("Введите описание задачи: ")
    priority = input("Введите приоритет (высокий/средний/низкий): ")
    tasks.append({"task": name, "priority": priority})
    print("Задача добавлена!")

def remove_task(tasks):
    show_tasks(tasks)
    try:
        index = int(input("Введите номер задачи для удаления: ")) - 1
        if 0 <= index < len(tasks):
            removed = tasks.pop(index)
            print(f"Задача '{removed['task']}' удалена.")
        else:
            print("Некорректный номер.")
    except ValueError:
        print("Ошибка: введите число.")

def find_task(tasks):
    query = input("Что ищем? ").lower()
    found = [t for t in tasks if query in t['task'].lower()]
    if found:
        print("\nРезультаты поиска:")
        for t in found:
            print(f"- {t['task']} (Приоритет: {t['priority']})")
    else:
        print("Ничего не найдено.")

def main():
    todo_list = []
    while True:
        print("\n1. Показать задачи\n2. Добавить\n3. Удалить\n4. Поиск\n5. Выход")
        choice = input("Выберите действие: ")
        if choice == '1':
            show_tasks(todo_list)
        elif choice == '2':
            add_task(todo_list)
        elif choice == '3':
            remove_task(todo_list)
        elif choice == '4':
            find_task(todo_list)
        elif choice == '5':
            break
        else:
            print("Неверный ввод.")

if __name__ == "__main__":
    main()