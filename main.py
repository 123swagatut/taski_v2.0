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
