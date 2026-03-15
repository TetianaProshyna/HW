import random
import statistics

#1
while True:
    num=input('Введіть ціле число: ')
    if num.isdigit():
        res=int(num)
        break
    else:
        print('Введено невірні дані')
if res%3==0 and res%5==0:
    print('ham')
elif res%3==0:
    print('foo')
elif res%5==0:
    print('bar')
else:
    print('число не ділиться ні на 3 ні на 5')

#2
while True:
    x = input('Введіть перше число: ')
    y = input('Введіть друге число: ')

    if x.isdigit() and y.isdigit():
        a = int(x)
        b = int(y)
        break
    else:
        print('Введено невірні дані. Введіть два цілих числа.')

if a > b:
    print(f'{a} більше за {b}')
elif a < b:
    print(f'{a} менше за {b}')
else:
    print('Числа рівні')

#2a
numbers=[random.randint(100,1000), random.randint(100,1000)]
print(numbers)
if numbers[0]>numbers[1]:
    print(f'Число {numbers[0]} більше ніж число {numbers[1]}')
elif numbers[0]<numbers[1]:
    print(f'Число {numbers[0]} менше ніж число {numbers[1]}')
else:
    print('Числа рівні')

#3
numbers = list(map(int, input('Введіть три числа : ').split()))
numbers.sort()
print(numbers[0], numbers[1], numbers[2])

#3a
nums=[random.randint(1, 10) for i in range(3)]
print(nums)
print(min(nums), statistics.median(nums), max(nums))

#4
for i in range(1, 101):
    res=''
    if i%3==0 and i%5==0:
        res+='fizz buzz'
    elif i%3==0:
        res+='fizz'
    elif i%5==0:
        res+='buzz'
    else:
        res=i
    print(res)

#5
for i in range(1, 101): print('BOOM' if i%7==0 or '7' in str(i) else i )
