# Семинар 2 Задание 2 Задайте список из n чисел последовательности (1 + 1/n)**n, выведеите его на экран, а так же сумму элементов списка.-/*
n = int (input('Задание 2 Введите число n '))
calc = lambda a:round ((1+1/a)**a,2) 
row = [calc(i) for  i in range(1,n+1)]
print(f'Список чисел заданной последовательности {row}')
print(f'Сумма элементов последовательности равна {sum(row)} \n')
input("Для продолжения нажмите любую кнопку")

#Семинар 3 Задание 3 Нахождение разницы между наибольшей и наименьшей дробной частью элементов списка
f_list = [-4.27,5.01,9.04,6.07,12345.01,9.25]
print ("Задание 3")
print(f"Исходный список {f_list}")
import math
get_float = lambda a: abs (float (format(math.fmod(a ,1.00),'.2f'))) 
float_list = [get_float(i) for i in f_list]
print(float_list)
print (f'разница между наибольшей ={max (float_list)} и наименьшей ={min(float_list)} дробными частями чисел списка составляет:') 
print(format (max (float_list)-min(float_list),'.2f'))