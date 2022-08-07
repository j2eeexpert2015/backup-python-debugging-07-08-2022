"""
In the Fibonacci sequence, each number is the sum of two numbers that precede it.
For example:
1, 1, 2, 3, 5, 8 , 13, 21, ...
The following formula describes the Fibonacci sequence:
f(1) = 1
f(2) = 1
f(n) = f(n-1) + f(n-2) if n > 2
"""


def fibonacci(n):
    if n < 0:
        print("Incorrect input")
    elif n == 0:
        return 0
    elif n == 1 or n == 2:
        return 1
    else:
        return fibonacci(n - 1) + fibonacci(n - 2)


# Driver Program
print(fibonacci(9))
