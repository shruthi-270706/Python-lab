num_primes = int(input("Enter how many primes: "))
count_primes = 0  
prime_count = 0  
i = 2 
while prime_count < num_primes:
    count = 0 
    for j in range(1, i+1):  
        if i % j == 0:
            count += 1
    if count == 2:  
        print(i, end=" ")  
        prime_count += 1
        count_primes += 1
        if count_primes == 5:
            print()  
            count_primes = 0  
    i += 1
