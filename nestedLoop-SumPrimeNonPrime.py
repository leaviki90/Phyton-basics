# 3.	Sum Prime Non-Prime

prime_sum = 0
not_prime_sum = 0

while True:
    n = input()
    if n == "stop":
        break
    n = int(n)
    if n < 0:
        print("Number is negative.")
        continue

    # Assume number is prime unless proven otherwise
    is_prime = True
    if n > 1:
        for i in range(2, int(n**0.5) + 1):
            if n % i == 0:
                is_prime = False
                break
    else:
        is_prime = False  # Numbers less than or equal to 1 are not prime

    if is_prime:
        prime_sum += n
    else:
        not_prime_sum += n

print(f"Sum of all prime numbers is: {prime_sum}")
print(f"Sum of all non-prime numbers is: {not_prime_sum}")
