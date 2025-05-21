#Problem 1: Reverse a String

def reverse_string(s):
    return s[::-1]

# Example
print(reverse_string("hello"))  

#Problem 2: Count Vowels in a String

def count_vowels(s):
    vowels = {'a', 'e', 'i', 'o', 'u'}
    count = 0
    for char in s.lower():
        if char in vowels:
            count += 1
    return count

# Example
print(count_vowels("Apple")) 

#Problem 3: Sum of Digits

def sum_of_digits(num):
    total = 0
    for digit in str(num):
        total += int(digit)
    return total

# Example
print(sum_of_digits(1234))  


