#№22 Даны два неупорядоченных набора целых чисел (может быть, с повторениями). 
#Выдать без повторений в порядке возрастания все те числа, которые встречаются в обоих наборах.
#Пользователь вводит 2 числа. n - кол-во элементов первого множества. 
#m - кол-во элементов второго множества. Затем пользователь вводит сами элементы множеств.

n = int(input('Введите количество элементов первого множества '))
m = int(input('Введите количество элементов второго множества '))
print('Заполнение первого мнрожества:')
first_set=list(int(input()) for _ in range(n))
print('Заполнение второго мнрожества:')
second_set =list(int(input()) for _ in range(m))
print(f'Первое множество {first_set}')
print(f'Второе множество {second_set}')

first_set=set(first_set)
second_set=set(second_set)
if first_set.isdisjoint(second_set):
        print('Нет пересечений')
else:
     first_set.intersection_update(second_set)
     first_set=list(frozenset(first_set))
     print(f'Элементы встречающиеся в обоих набороах {sorted(first_set)}')

