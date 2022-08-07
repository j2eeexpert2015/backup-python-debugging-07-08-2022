"""
The function sum_of_value adds up all the numbers of the entered array,
which are completely divisible by the entered value
For example – If the entered array is arr{1,2,3,4,5} and the entered value is 2,
then the output will be 2+4 = 6.
"""
import math


def sum_of_value(arr, value):
    total_sum = 0
    length_of_array = len(arr)
    for i in range(0, length_of_array):
        if math.fmod(arr[i], value) == 0:
            total_sum = + arr[i]
    print("sum is :", total_sum)
    return total_sum


number_array = [10, 20, 30]
sum_of_value(number_array, 5)
