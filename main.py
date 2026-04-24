def show_tasks(tasks):
    if not tasks:
        print("\nСписок задач пуст.")
    else:
        print("\n--- Текущие задачи ---")
        for i, item in enumerate(tasks, 1):
            print(f"{i}. {item['task']} [Приоритет: {item['priority']}]")