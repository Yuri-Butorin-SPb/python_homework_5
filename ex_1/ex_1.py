# Задача 26:  Напишите программу, которая на вход принимает два числа A и B, 
# и возводит число А в целую степень B с помощью рекурсии.

# *Пример:*

# A = 3; B = 5 -> 243 (3⁵)
#     A = 2; B = 3 -> 8 


def get_power (a, b):
    
    if b == 0:
        return 1
    elif b == 1:
        return a
    elif b != 1: 
        return a * (get_power(a, b-1))

a = int(input("Введите число: "))
b = int(input("Введите степень: "))

print(f"{a} в степени {b} равно {get_power(a,b)}")

