# Напишите программу, которая принимает на вход цифру, 
# обозначающую день недели, и проверяет, является ли этот день выходным.
# Пример:
# - 6 -> да
# - 7 -> да
# - 1 -> нет

number = int(input('Введите число: '))
def f(x):
    if x == 6 or x == 7:
        return 'Число является выходным'
    elif x >= 1 and x <= 5:
        return 'Число не является выходным'
    else:
        return 'Число не обозначает день недели'

print (f(number))