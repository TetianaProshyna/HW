#1
name=input("Введіть ваше ім'я: ")
salary=int(input('Введіть місячну зарплату в доларах: '))
salary_year=salary*12//1000
print(f'Річна зарплата {name} складає {salary_year} тис. доларів' )

#2
count=int(input('Введіть ціле число: '))
print(100 <= count < 1000 and count % 2 == 0)
count=input('Введіть ціле число: ')
if count.isdigit():
    num = int(count)
    print(100 <= num <= 999 and num % 2 == 0)
else:
    print("Невірний формат вводу")

#3a
user_input = input('Введіть трицифрове число (101-999, остання цифра має бути не 0): ')

if user_input.isdigit():
    num = int(user_input)
    if 101 <= num <= 999 and num % 10 != 0:
        reversed_num = int(user_input[::-1])
        print('Перевернуте число:', reversed_num)
    else:
        print('Число не відповідає умовам')
else:
    print('Введене значення не є числом')

#3b
import random

while True:
    num = random.randint(101, 999)
    if num % 10 != 0:
        break

reversed_num = int(str(num)[::-1])
print(f"Згенероване число: {num} - Перевернуте: {reversed_num}")

#4
num1_input = input("Введіть перше ціле число: ")
num2_input = input("Введіть друге ціле число: ")

if num1_input.isdigit() and num2_input.isdigit():
    num1 = int(num1_input)
    num2 = int(num2_input)

    print("Сума:", num1 + num2)
    print("Різниця:", num1 - num2)
    print("Множення:", num1 * num2)

    if num2 != 0:
        print("Ділення:", num1 / num2)
        print("Залишок від ділення:", num1 % num2)
    else:
        print("Помилка: ділення на нуль неможливе")

    print("Перше число ≥ другому:", num1 >= num2)

else:
    print("Помилка: потрібно ввести цілі числа")