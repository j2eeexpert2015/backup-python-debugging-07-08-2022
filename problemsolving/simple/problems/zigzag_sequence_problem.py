"""
Given an array of n distinct integers, transform the array into a zig zag sequence by permuting the array elements.
A sequence will be called a zig zag sequence if the first k elements in the sequence are in increasing order and
the last k elements are in decreasing order, where k=(n+1)/2.
You need to find the lexicographically smallest zig zag sequence of the given array.

Example.
a=[2,3,5,1,4]
Now if we permute the array as [1,4,5,3,2], the result is a zig zag sequence.

Debug the given function findZigZagSequence to return the appropriate zig zag sequence for the given input array.
Input Format

The first line contains t the number of test cases.
The first line of each test case contains an integer n, denoting the number of array elements.
The next line of the test case contains n elements of array a.

Sample Input
1
7
1 2 3 4 5 6 7

Sample Output
1 2 3 7 6 5 4

"""
def findZigZagSequence(a, n):
    a.sort()
    mid = int((n + 1)/2)
    a[mid], a[n-1] = a[n-1], a[mid]

    st = mid + 1
    ed = n - 1
    while(st <= ed):
        a[st], a[ed] = a[ed], a[st]
        st = st + 1
        ed = ed + 1

    for i in range (n):
        if i == n-1:
            print(a[i])
        else:
            print(a[i], end = ' ')
    return

test_cases = int(input())
for cs in range (test_cases):
    n = int(input())
    a = list(map(int, input().split()))
    findZigZagSequence(a, n)