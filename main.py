def find_task(tasks):
    query = input("Что ищем? ").lower()
    found = [t for t in tasks if query in t['task'].lower()]
    if found:
        print("\nРезультаты поиска:")
        for t in found:
            print(f"- {t['task']} (Приоритет: {t['priority']})")
    else:
        print("Ничего не найдено.")