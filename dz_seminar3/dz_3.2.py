# Задача 18: Требуется найти в массиве A[1..N] самый близкий по величине элемент к заданному числу X. 
# Пользователь в первой строке вводит натуральное число N – количество элементов в массиве. 
# В последующих  строках записаны N целых чисел Ai. Последняя строка содержит число X

# *Пример:*

# 5
#     1 2 3 4 5
#     6
#     -> 5

# a = [int(input())for _ in range (int(input('Ввежите размер массива: ')))]
# x=int(input('Введите искомое число: '))
# ind=0
# for i in range(len(a)-1):
#     if x-a[i]>x-a[i+1]:
#         ind=i
#     el
#     print(a[ind])

a = [int(input())for _ in range (int(input('Ввежите размер массива: ')))]
x=int(input('Заданное число:'))
b=[abs(a[i]-x) for i in range(len(a))]
print(a[b.index(min(b))])

# a=[int(input()) for _ in range(int(input()))]
# b=int(input())
# number=0
# for i in range(len(a)):
#     if (b-a[i])<b-number and b-a[i]>0:
#         number=i
# print(a[number])