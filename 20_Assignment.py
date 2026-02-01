#1. Write a python program to create a function that takes a list and returns a new list with the original list's unique elements.

def unique(lst):
    return list(set(lst))

print(unique([1,2,2,3,4,4,5]))


#2. Write a python program to create a function that takes a number as a parameter and checks if the number is prime or not.
def is_prime(n):
    if n < 2:
        return False
    for i in range(2, int(n**0.5)+1):
        if n % i == 0:
            return False
    return True

print(is_prime(7))



#3. Write a python program to create a function that prints the even numbers from a given list. Sample List : [1, 2, 3, 4, 5, 6, 7, 8, 9]
def even_nums(lst):
    print([i for i in lst if i % 2 == 0])

even_nums([1,2,3,4,5,6,7,8,9])


#4. Write a python program to create a function that checks whether a passed string is palindrome or not.
def palindrome(s):
    return s == s[::-1]

print(palindrome("madam"))


#5. Write a python program to create a function to find the Min of three numbers.
def minimum(a, b, c):
    return min(a, b, c)

print(minimum(3, 1, 2))


#6. Write a python program to create a function and print a list where the values are square of numbers between 1 and 30.
def squares():
    return [i*i for i in range(1, 31)]

print(squares())


#7. Write a python program to access a function inside a function.
def outer():
    def inner():
        return "Hello"
    return inner()

print(outer())


#8. Write a python program to create a function that accepts a string and calculate the number of upper case letters and lower case letters.
def count_case(s):
    u = l = 0
    for i in s:
        if i.isupper():
            u += 1
        elif i.islower():
            l += 1
    return u, l

print(count_case("PyThOn"))


#9. Write a python program to create a function to check whether a string is a pangram or not.
def pangram(s):
    return set("abcdefghijklmnopqrstuvwxyz") <= set(s.lower())

print(pangram("The quick brown fox jumps over the lazy dog"))


#10. Write a python program to create a function to check whether a string is an anagram or not.
def anagram(a, b):
    return sorted(a) == sorted(b)

print(anagram("listen", "silent"))
