#1. Write a python program to create a simple function which prints “TasiNCoder”.
def show():
    print("TasiNCoder")

show()


#2. Write a python program to create a function which expects two arguments and print them in the function body.
def display(a, b):
    print(a, b)

display(10, 20)


#3. Write a python program to create a function which expects an unknown number of arguments.
def total(*args):
    print(args)

total(1, 2, 3, 4)


#4. Write a python program to create a function which expects kwargs arguments.
def info(**kwargs):
    print(kwargs)

info(name="Rohan", course="Python")


#5. Write a python program to create a function which expects a list as an argument.
def show_list(lst):
    print(lst)

show_list([1, 2, 3])


#6. Write a python program to create a function that finds a maximum of four numbers
def maximum(a, b, c, d):
    return max(a, b, c, d)

print(maximum(4, 7, 2, 9))


#7. Write a python program to sum all the numbers in a list.
def sum_list(lst):
    return sum(lst)

print(sum_list([1, 2, 3, 4]))


#8. Write a python program to multiply all the numbers in a list.
def multiply_list(lst):
    r = 1
    for i in lst:
        r *= i
    return r

print(multiply_list([1, 2, 3, 4]))


#9. Write a python program to create a function to check whether a number falls in a given range.
def in_range(n, a, b):
    return a <= n <= b

print(in_range(5, 1, 10))


#10. Write a python program to create a function to check whether a given number is even or odd.
def check(n):
    return "Even" if n % 2 == 0 else "Odd"

print(check(7))
