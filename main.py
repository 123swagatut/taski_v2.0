def add_task(tasks):
    name = input("Введите описание задачи: ")
    priority = input("Введите приоритет (высокий/средний/низкий): ")
    tasks.append({"task": name, "priority": priority})
    print("Задача добавлена!")