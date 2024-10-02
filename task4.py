from datetime import datetime, timedelta

def get_upcoming_birthdays(users):
    today = datetime.today().date()
    next_week = today + timedelta(days=7)
    
    # Порожній список для зберігання даних привітань
    upcoming_birthdays = []

    for user in users:
        # Конвертуємо дату народження з рядка у формат datetime.date
        birthday = datetime.strptime(user['birthday'], "%Y.%m.%d").date()
        
        # Робимо перевірку на цей рік
        birthday_this_year = birthday.replace(year=today.year)
        
        # Якщо день народження вже був цього року, беремо наступний рік
        if birthday_this_year < today:
            birthday_this_year = birthday.replace(year=today.year + 1)
        
        # Перевіряємо, чи день народження відбувається в найближчі 7 днів
        if today <= birthday_this_year <= next_week:
            # Якщо день народження припадає на вихідні (субота = 5, неділя = 6)
            if birthday_this_year.weekday() >= 5:
                # Переносимо на найближчий понеділок
                days_until_monday = 7 - birthday_this_year.weekday()
                congratulation_date = birthday_this_year + timedelta(days=days_until_monday)
            else:
                congratulation_date = birthday_this_year

            # Додаємо користувача з датою привітання у список
            upcoming_birthdays.append({
                'name': user['name'],
                'congratulation_date': congratulation_date.strftime('%Y.%m.%d')
            })

    return upcoming_birthdays

# Приклад використання
users = [
    {"name": "John Doe", "birthday": "1985.01.23"},
    {"name": "Jane Smith", "birthday": "1990.01.27"}
]

upcoming_birthdays = get_upcoming_birthdays(users)
print("Список привітань на цьому тижні:", upcoming_birthdays)
