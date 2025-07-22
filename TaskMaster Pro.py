users = {}  
tasks = []  
categories = ["Работа", "Дом", "Учёба", "Хобби"]  # Список категорий
statuses = ["Новая", "В процессе", "Завершена", "Отложена"]  # Список статусов


def register_user():
    """Регистрация нового пользователя"""
    username = input("Создайте логин: ")
    
    
    if username in users:
        print("Ошибка: Пользователь уже существует!")
        return
    
    password = input("Создайте пароль: ")
    users[username] = password
    print(f"Пользователь {username} успешно зарегистрирован!")

def login():
    """Аутентификация пользователя"""
    username = input("Логин: ")
    password = input("Пароль: ")
    
    
    if username in users and users[username] == password:
        print(f"Добро пожаловать, {username}!")
        return True
    print("Ошибка: Неверный логин или пароль!")
    return False

def add_task():
    """Добавление новой задачи"""
    task = {
        "id": len(tasks) + 1, 
        "title": input("Название задачи: "),  
        "category": select_category(),  
        "priority": int(input("Приоритет (1-5): ")), 
        "status": "Новая",  
        "completed": False 
    }
    tasks.append(task)
    print("Задача успешно добавлена!")

def select_category():
    """Выбор категории из списка"""
    
    print("\nДоступные категории:")
    for i, category in enumerate(categories, 1):
        print(f"{i}. {category}")
    
    
    while True:
        try:
            choice = int(input("Выберите категорию (1-4): "))
            if 1 <= choice <= len(categories):
                return categories[choice - 1]
            print("Ошибка: Неверный номер категории!")
        except ValueError:
            print("Ошибка: Введите число!")

def show_tasks():
    """Отображение задач с фильтрацией"""
    
    if not tasks:
        print("Список задач пуст!")
        return
    
    print("\n===== ВАШИ ЗАДАЧИ =====")
    
    for task in tasks:
        status_icon = "✓" if task["completed"] else "◻"
        print(f"{status_icon} #{task['id']} [{task['category']}] {task['title']} "
              f"(Приоритет: {task['priority']}, Статус: {task['status']})")

def complete_task():
    """Отметка задачи как выполненной"""
    show_tasks()
    try:
        task_id = int(input("Введите ID задачи для завершения: "))
        
        
        for task in tasks:
            if task["id"] == task_id:
                task["completed"] = True
                task["status"] = "Завершена"
                print("Задача отмечена как выполненная!")
                return
        print("Ошибка: Задача не найдена!")
    except ValueError:
        print("Ошибка: Введите числовой ID!")

def show_stats():
    """Аналитика продуктивности"""
    if not tasks:
        print("Нет данных для анализа!")
        return
    
    
    completed = sum(1 for t in tasks if t["completed"])
    total = len(tasks)
    completion_rate = (completed / total) * 100 if total > 0 else 0
    
  
    category_stats = {}
    for category in categories:
        count = sum(1 for t in tasks if t["category"] == category)
        category_stats[category] = count
     
    print("\n===== АНАЛИТИКА =====")
    print(f"Всего задач: {total}, Выполнено: {completed} ({completion_rate:.2f}%)")
    print("Статистика по категориям:")
    for category, count in category_stats.items():
        print(f"{category}: {count} задач")         
def main():
    global users, tasks
    
    # Инициализация тестовых данных
    users = {"admin": "password123"}
    tasks = [
        {"id": 1, "title": "Изучить Python", "category": "Учёба", 
         "priority": 5, "status": "В процессе", "completed": False},
        {"id": 2, "title": "Купить продукты", "category": "Дом", 
         "priority": 3, "status": "Новая", "completed": False}
    ]
    
    # Главный цикл системы
    while True:
        print("\n===== TASKMASTER PRO =====")
        print("1. Регистрация")
        print("2. Вход")
        print("3. Выход")
        
        choice = input("Выберите действие: ")
        
        # Условия для обработки выбора
        if choice == "1":
            register_user()
        elif choice == "2":
            if login():
                user_menu()
        elif choice == "3":
            print("До свидания!")
            break
        else:
            print("Неверный ввод! Попробуйте снова.")

def user_menu():
    """Меню залогиненного пользователя"""
    while True:
        print("\n===== ГЛАВНОЕ МЕНЮ =====")
        print("1. Добавить задачу")
        print("2. Показать задачи")
        print("3. Завершить задачу")
        print("4. Аналитика продуктивности")
        print("5. Выход")
        
        choice = input("Выберите действие: ")
        
        
        if choice == "1":
            add_task()
        elif choice == "2":
            show_tasks()
        elif choice == "3":
            complete_task()
        elif choice == "4":
            show_stats()
        elif choice == "5":
            break
        else:
            print("Неверный ввод! Попробуйте снова.")


if __name__ == "__main__":
    main()