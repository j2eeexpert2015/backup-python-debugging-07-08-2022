import math
def search(a, start, last, item):
    mid = None
    if last >= start:
        mid = math.trunc((start + last) / float(2))
        if a[mid] == item:
            return mid + 1
        elif a[mid] < item:
            return search(a, start, mid + 1, item)
        else:
            return search(a, mid - 1, last, item)
    return -1