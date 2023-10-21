#print(5,8,9) 



# print(5,8,9) # Коментария Ctrl + K, Ctrl + C. Раскоментировать Ctrl + K, Ctrl + U.
# # print(5,8,9)
# # print(5,8,9)

# # Интерполяция 
# a = 5
# b = 10
# c = 'Islam'
# print(f"{a}-{b}-{c}") # 1 Вариант
# print("{}-{}-{}".format(a,b,c)) # 2 Вариант

# print("Введите число:") # 1 Вариант
# a = int(input())
# b = int(input("Введите второе число:")) # 2 Вариант
# print(f"{a} + {b} = {a+b}")
# # print(a)

# s = 4.16
# s = int(s) # Изменение типа данных

# print(s)

# Арифметические операции
# + Сложение
# - Вычитание
# * Умножение
# / Деление
# % Остаток от деление
# // Целочисленное деление
# ** Возведение в степен 

# o = 5.2555152
# k = 6.256458  # round - округление Первым пишем число который хотим округлит,
# print(round(o*k, 3)) #2- пишем сколько хотим оставить после запитой

# iter = 2                  #   C# i++
# iter += 3 #iter = iter +3
# iter -= 4 # iter = iter -4
# iter *=5 # iter = iter *5
# iter /= 6 # iter = iter /6
# iter **=7 # iter = iter **7
# iter //= 8 # iter = iter //8
# iter %= 8 # iter = iter %8


# d = 1 > 4
# d = 1<4 and 5>2 # and обединяет условия 
# d = 1 == 2      # == оператор равенство проверяет равныли значение
# d = 1 !=2       # != оператор не равенство проверяет не ровныли значение
# d = 'Islam'     # Сравнение строк
# q = 'Islam'
# print(d==q)
# d = 1<2<5<7>1

#       <------> Отступы 1 Tab = 4 пробела
# if condition:
#     #operator 1
#     #operator 2
#     #operator 3
#     #operator 4
# else:
#     #operator n+1
#     #operator n+2
#     #operator n+3
#     #operator n+4

# if condition:
# #     #operator 1
# elif:
#     #operator 2
# elif:
#     #operator 3

# userName = input('Введите имя: ')
# if userName == 'Ислам':
#     print('Ислам крассавчик!:)')
# elif userName == 'Муха':
#     print('Муха молодец')
# elif userName == 'Самаган':
#     print('Самаган Шоумен №1')

#    <-----------> while 
# i = 0   
# while i < 5:
#     if i == 3:
#         break
#     i = i +1
# else:
#     print('Пожалуй хватит')
#     print(i)

# n = int(input())
# flag = True
# i = 2
# while flag:
#     if n % i == 0: # если остаток при деление число n на i ровен 0
#         flag = False
#         print(i)
#     elif i > n // 2: # делить число не может превышать введенное число, деленное на 2
#         print(n)
#         flag = False
#     i += 1

#           <---------> for range()
# r = range(5) # 0 1 2 3 4 
# r = range(2, 5) # 2 3 4 
# r = range(0,-5) # -----
# r = range(1,10,2) # 1 3 5 7
# r = range(100, 0, =20) # 100 80 60 40 20  
# r = range(100, 0, -20) # 100 0 -20
# fot i in r:
#     print(i)
# #100 80 60 40 20 

# a = 'qwertyui'

# for i in a:
#     print(i)

# line = ""
# for i in range(5):
#     line = ""
#     for j in range(5):
#         line += "+"
#     print(line)

# <----------> Строки и срезы
text = 'Дициплина это крутой абгрейд' # replace изменение слов 1-слово который будет изменен,
print(text.replace('это','Это')) # 2-слово на которого будет изменен,

# Возникают ситуации, когда в некоторых задачах необходимо поработать со строкой,
# которую ввел пользователь. Например: необходимо сделать все буквы маленькими, или
# поменять все буквы “ё” на “е”.
text = 'СъЕШЬ ещё этих МяГкИх французских булок'
print(len(text)) # 39
print('ещё' in text) # True
print(text.lower()) # съешь ещё этих мягких французских булок
print(text.upper()) # СЪЕШЬ ЕЩЁ ЭТИХ МЯГКИХ ФРАНЦУЗСКИХ БУЛОК
print(text.replace('ещё','ЕЩЁ')) # СъЕШЬ ЕЩЁ этих МяГкИх французских булок

# Срезы
# ● Мы представляем строку в виде массива символов. Значит мы можем обращаться к
# элементам по индексам.
# ● Отрицательное число в индексе — счёт с конца строки
text = 'съешь ещё этих мягких французских булок'
print(text[0]) # c
print(text[1]) # ъ
print(text[len(text)-1]) # к
print(text[-5]) # б
print(text[:]) # съешь ещё этих мягких французских булок
print(text[:2]) # съ
print(text[len(text)-2:]) # ок
print(text[2:9]) # ешь ещё
print(text[6:-18]) # ещё этих мягких
print(text[0:len(text):6]) # сеикакл
print(text[::6]) # сеикакл
text = text[2:9] + text[-5] + text[:2] # ...    