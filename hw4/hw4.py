import time


def simple_prime_search(n):
    primes = []

    for num in range(2, n + 1):
        is_prime = True
        for divisor in range(2, num):
            if num % divisor == 0:
                is_prime = False
                break
        if is_prime:
            primes.append(num)

    return primes


def sieve_eratosthenes(n):
    sieve = [True] * (n + 1)
    sieve[0] = sieve[1] = False

    for i in range(2, int(n ** 0.5) + 1):
        if sieve[i]:
            for j in range(i * i, n + 1, i):
                sieve[j] = False
    return [i for i in range(2, n + 1) if sieve[i]]


def measure_time(func, *args, **kwargs):
    start_time = time.time()
    result = func(*args, **kwargs)
    end_time = time.time()

    print(f'Час виконання функції {func.__name__}: {end_time - start_time:.8f} сек.')
    return result


ranges = [100, 1000, 10000]

for item in ranges:
    print(f'\nПошук для {item}')

    measure_time(simple_prime_search, item)
    measure_time(sieve_eratosthenes, item)