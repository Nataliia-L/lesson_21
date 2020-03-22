#4. Написать скрипт парсинга файла с информацией о балансах пользователей 
# https://drive.google.com/open?id=1iItMYUF0Uwb-qB0epNTLRnJpKRU6joGV (https://drive.google.com/open?id=1iItMYUF0Uwb-qB0epNTLRnJpKRU6joGV) . 
# Затем просить пользователей ввести номер аккаунта, а в ответ выводить ему баланс этого пользователя. 
# С помощью механизма исключений и обработки исключений, предусмотреть варианты - что пользователь введет вместо номера аккаунта не числа. 
# А также, что будет введен несуществующий номер аккаунта.

import string

info_file = {}
with open ('balances.txt') as f:
    lines = f.readlines ()
    for line in lines:
        splitted = line.strip ().split (';')
        account, balance = splitted
        if account in info_file:
            info_file[account].append (balance)
        else:
            info_file[account] = float(balance) 

ask = str(input ('Please, enter your account number: '))
if ask in info_file:
    print (f'Your balance is: {info_file[ask]}')
elif ask.isdigit()==False:
    raise Exception ('Account number contains letters or special symbols. Check, please.')
else:
    raise Exception ('Account is not defined.')
