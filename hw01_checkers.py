#1. Написать два модуля. Первый checkers.py, содержит функции проверки - имени(check_name), даты рождения(check_bdate), 
# а также функцию test без параметров. (Функция test вызывается в случае запуска модуля в интерпретаторе, 
# в ней происходит вызов каждой описанной в модуле функции с корректными значениями). 
# Функции check_name, check_bdate проверяют корректность переданных аргументов и кидают исключения с текстом, 
# если что-то не соответствует норме.
#Второй модуль - main.py, импортирует модуль проверок checkers и просит пользователя ввести имя, год, месяц, день рождения 
# и проверяет введенные данные с помощью функций модуля checkers.py. Запускать модуль main и checkers.

def check_name (name):
    if name != 'Nata':
        raise Exception ('Invalid name')
    print ('Name checked')


def check_bday (year,month,day):
    year = input ('Please, enter the year of your b-day: ')
    if int(year)>2020:
        raise Exception ('Invalid year')
    month = input ('Please, enter the month of your b-day: ')
    if int(month)>13:
        raise Exception ('Invalid month')
    day = input ('Please, enter the day of your b-day: ')
    if int(day)>31:
        raise Exception ('Invalid day')

    print ('Date checked')


def test ():
    a = check_name ('Nata')
    b = check_bday (2019,11,20)

if __name__=='__main__':
    print (test ())
else:
    print ('Module is imported')
