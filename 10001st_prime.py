'''
By listing the first six prime numbers: 2, 3, 5, 7, 11, and 13, we can see that
the 6th prime is 13. What is the 10 001st prime number?
'''


def check_prime(n):
    '''
    Divide n by all integers less than n.
    Return true if prime.
    Return false if divisible by an integer less than n.
    '''
    for i in range(2,n):
        if n % i == 0:
            return False
        else:
            return True

def build_list():
    '''
    Starting from 3, check 'primeness' of each integer.
    Append prime numbers to prime_list.
    Return list of primes.
    '''
    i = 3
    while len(prime_list) < 10001:
        if check_prime(i):
            prime_list.append(i)
        i += 1
    return prime_list
 
prime_list = [2]
build_list()
print 'This list has ' +str(len(prime_list)) +' elements.'
print 'The 10,001st prime is: ' + str(prime_list[-1])
