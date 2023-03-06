#Напишите рекурсивную функцию sum(a, b), возвращающую сумму двух целых неотрицательных чисел. 
#Из всех арифметических операций допускаются только +1 и -1. Также нельзя использовать циклы.


def rec_sum(a, b):
   if b==0:
      return a
   else:
          if b>0:
            return  rec_sum(a+1, b-1)
          else:
           return   rec_sum(a-1, b+1)

a=int(input())
b=int(input())
print(rec_sum(a,b))
