numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15]

primes = []
not_praimes = []

for i in numbers:
    if i == 1:
        continue
    is_prime = True
    for j in range(2, i):
        if i % j == 0:
            not_primes.append(i)
            break
    else:
        primes.append(i)

print('Primes: ', primes)
print('Not Primes: ', not_praimes)
