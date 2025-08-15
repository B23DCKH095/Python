from decimal import Decimal
from math import sqrt
class Point:
    def __init__(self,a,b)-> None:
        self.x = a
        self.y = b 
    def distance(self,b):
        dis = sqrt(pow(self.x - b.x,2) + pow(self.y - b.y , 2))
        return dis
if __name__ == '__main__':
    t = int(input())
    while t > 0:
        arr = input().split()
        A = Point(Decimal(arr[0]), Decimal(arr[1]))
        B = Point(Decimal(arr[2]), Decimal(arr[3]))
        C = Point(Decimal(arr[4]), Decimal(arr[5]))
        AB = A.distance(B)
        AC = A.distance(C)
        BC = B.distance(C)
        ok = True
        if(AB + AC <= BC or AB +BC <= AC or BC + AC <= AB): ok = False
        if(ok): print(f"{round(AB + BC +AC,3):.3f}")
        else: print("INVALID")
        t -= 1
