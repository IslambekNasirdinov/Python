# Требуется вывести все целые степени двойки (т.е. числа вида 2k), не превосходящие числаN.

# Пример

# n=16

# #Вывод
# 1
# 2
# 4
# 8
# 16

n = 16
p = 1
    #       <-------- 1-Вариант------>
while p <= n:
    print(p)
    p*=2

# #   <-------- 2-Вариант------>
# i = 0
# while 2 ** i <= n:
#     print(2 ** i)
#     i += 1

