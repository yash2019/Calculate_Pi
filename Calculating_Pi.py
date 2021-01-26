import math

# The Higher Extent is given the
# more accurate yet slower it will be

def Calc(Extent):
    Sum = 0
    for digit in range(1,Extent):
        Sum += 1/digit**2
    return math.sqrt(Sum)


print(Calc(999999))

