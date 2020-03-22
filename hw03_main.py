#3. Использовать модуль catalogs из п.3. Создать модуль main, в нем импортировать catalogs. 
# Просить пользователя ввести код страны (например, us) и выводить информацию об имени страны, код валюты и алиас валюты. 
# Если введено некорректное значение кода, которого нет в словаре, кидать исключение. 

import lesson_21_hw02_catalogs

country_code = input('Please, enter country code: ')
if country_code not in lesson_21_hw02_catalogs.d_country:
    raise Exception ('Invalid country code.')
else:
    print ('Country: ', ((lesson_21_hw02_catalogs.d_country[country_code])[0]),',', 'Currency_Code: ', ((lesson_21_hw02_catalogs.d_country[country_code])[1]),',', 'Alias: ', lesson_21_hw02_catalogs.d_currency[((lesson_21_hw02_catalogs.d_country[country_code])[1])])
