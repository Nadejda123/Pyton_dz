# Строка представляет собой арифметическое выражение из однозначных чисел и знаков + и -. Вычислите результат.
# Пример
# Ввод

# 8-5+2-1
# Вывод 4


txt = input()
result = int(txt[0])
for i in range(1, len(txt), 2):
    if txt[i] == '+':
        result += int(txt[i + 1])
    elif txt[i] == '-':
        result -= int(txt[i + 1])
print(result)

1 