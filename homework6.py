my_dict = {'Dima': 1980, 'Petya': 2001, 'Lena': 1997, 'Sergey': 1994}
print('Список: ', my_dict)
print(type(my_dict))
print("Lena: ", my_dict['Lena'])
a = my_dict['Katya'] = 2003
print("Добавленное значение: ", a)
my_dict.update({'Sonya': 2009, 'Maksim': 1991})
print("Удалённое значение: ", my_dict.pop('Sergey'))
print('Обновлённый список: ', my_dict)
print('В списке? : ', my_dict.get('Boris'))
print('"Work _____________ Set"')
my_set = {'Sonya', 'Lena', 'Roma', 'Lena', 'Roma', 2, 3, 1, 2, 3}
print(my_set)
print(type(my_set))
print(my_set.add('Yana'))
print(my_set.add('Misha'))
print(my_set)
print(my_set.discard(2))
my_set.discard('Lena')
print(my_set)
