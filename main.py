from application.salary import calculate_salary
from application.db.people import get_employees
from datetime import date

current_date = date.today()

if __name__ == '__main__':
    print(current_date)
    print(calculate_salary())
    print(get_employees())