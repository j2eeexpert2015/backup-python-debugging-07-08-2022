"""
The middle() function is supposed to return the "middle" number of three values x, y, and z
The one number that neither is the minimum nor the maximum.
"""
def middle(x, y, z):
    print("x:",x,"y:",y,"z:",z)
    if y < z:
        if x < y:
            return y
        elif x < z:
            return y
    else:
        if x > y:
            return y
        elif x > z:
            return x
    return z
print ("Output :",middle(1,2,3))
print ("Output :",middle(2,1,3))
