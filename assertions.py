def average(weight):
    assert len(weight) != 0,"List can't be empty"
    return sum(weight)/len(weight)
weight = [10,20,30]
print("Average weight is:",average(weight))
print("last line of the programe")




#____________________________________________with error message

def average(weight):
    assert len(weight) != 0,"List can't be empty"
    return sum(weight)/len(weight)

weight = [20,30,40,50,60]
print("Average weight is:",average(weight))

weight = []# problem is here: assert? yes
print("Average weight is:",average(weight))

#___________________________________________________square root

import math
def squareroot(a,b,c):
   assert b*b >= 4*a*c, " %s < %s square root of negative number is not possible " % (b*b, 4*a*c)
   return math.sqrt(b*b - 4*a*c)

print("call1",squareroot(4, 10, 5))

print("call2",squareroot(10, 8, 4))

#sqrt(b*b-4ac)
