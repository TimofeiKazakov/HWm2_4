numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15]
primes = [2, 3, 5, 7, 11, 13]
not_primes = [4, 6, 8, 9, 10, 12, 14, 15]
print(primes)
print(not_primes)
primes = []
not_primes = []
for number in numbers:
    if number != 1:
        is_prime = True
        for i in range(2, number):
                if number % i == 0:
                 is_prime = False
                 break
        if is_prime:
            primes.append(number)
        else:
           not_primes.append(number)

print(primes)
print(not_primes)




