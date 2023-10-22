# Ближайший элемент в массиве

# Требуется найти в массиве list_1 самый близкий по величине элемент к заданному числу k и вывести его.

# Пример:

# list_1 = [1, 2, 3, 4, 5]
# k = 6
# # 5

list_1 = [1, 12, 6, 7, 8, 15]
k = 11
# list_2 = []


# for i in list_1:
#     if k <= k:
#         list_2.append(i)
# print(max(list_2))

#   <--------Решение------->
m = abs(k - list_1[0])  # модуль числа
number = list_1[0]
for i in range(1, len(list_1)):
    if m > abs(list_1[i] - k):
        m = abs(list_1[i] - k)
        number = list_1[i]
print(number)

#       <----- Скопироваль с интернета :( ----->
# import bisect
# list_1 = [1, 12, 6, 7, 8, 15]
# k = 11
# list_1.sort()
# index = bisect.bisect_left(list_1, k)
# if index == 0:
#     closest = list_1[0]
# elif index == len(list_1):
#     closest = list_1[-1]
# else:
#     before = list_1[index-1]
#     after = list_1[index]
#     closest = before if after-k > k-before else after
# print(closest)
