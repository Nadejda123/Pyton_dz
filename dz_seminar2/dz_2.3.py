# Задача 14: Требуется вывести все целые степени двойки (т.е. числа вида 2k), не превосходящие числа N.


limit = int(input("Введите число N "))
degree = 2
while degree < limit:
    print(degree)
    degree*=2
    
      
