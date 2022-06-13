from application.salary import *
from application.db.people import *
from datetime import date

current_date = date.today()

if __name__ == '__main__':
    print(current_date)
    print(calculate_salary())
    print(get_employees())