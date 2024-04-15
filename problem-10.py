import math

def is_prime_number_slow(number_range):
    sum_of_p_numbers = 0
    for p_number in range(2, number_range):
        divide_count = 0
        for divide in range(2, int(math.sqrt(p_number)) + 1):
            result = p_number%divide
            if result == 0:
                divide_count = divide_count + 1
                #print(p_number, divide)
                break
        if divide_count < 1:
            sum_of_p_numbers += p_number
    return(sum_of_p_numbers)
        


def is_prime(num):
    if num <= 1:
        return False
    elif num <= 3:
        return True
    elif num % 2 == 0 or num % 3 == 0:
        return False
    else:
        sqrt_num = int(math.sqrt(num))
        for i in range(5, sqrt_num + 1, 6):
            if num % i == 0 or num % (i + 2) == 0:
                return False
        return True
    

def is_prime_number(number_range):
    sum_of_p_numbers = 0
    for p_number in range(2, number_range):
        if is_prime(p_number):
            sum_of_p_numbers += p_number
    return sum_of_p_numbers
    
'''Factor pairs: Any number can be factored into pairs of factors. For example, 
if num = a * b, then one of a or b must be less than or equal to the square root of num, 
and the other must be greater than or equal to the square root of num.'''

'''Divisibility: If a > sqrt(num) and b > sqrt(num), then a * b > num, which contradicts the 
fact that a * b = num. Therefore, if we have already checked all numbers up to sqrt(num) and 
havent found any divisors, we can conclude that num is prime.'''

print(is_prime_number_slow(2000000))