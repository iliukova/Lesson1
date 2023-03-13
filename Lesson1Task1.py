# Task 1
# Написати скрипт, який для п'яти цілочисельних значень
# (вводить користувач з клавіатури), знаходить мінімум, максимум та середнє.

number_a = int(input("a="))
number_b = int(input("b="))
number_c = int(input("c="))
number_d = int(input("d="))
number_f = int(input("f="))
print("мінімальне значення:", min(number_a, number_b, number_c, number_d, number_f))
print("максимумальне значення:", max(number_a, number_b, number_c, number_d, number_f))
print("середнє значення:" , int((number_a+number_b+number_c+number_d+number_f)/5))
