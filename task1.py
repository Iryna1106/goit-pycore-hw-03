from datetime import datetime

def get_days_from_today(date_str):
    try:
        input_date=datetime.strptime(date_str, '%Y-%m-%d').date()
        today=datetime.today().date()
        delta=today-input_date
        return delta.days
    except ValueError:
        return"Неправильний формат дати. Використовуйте формат 'РРРР-ММ-ДД'."
print(get_days_from_today("2025-10-01"))
