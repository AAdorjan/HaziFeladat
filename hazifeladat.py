def feladat_1(a,b):
    a = a + b
    b = a - b
    a = a - b
    print(a,b)


def feladat_2(a,b,c):
    if a<b and a<c:
        if b<c:
            print(a,b,c)
        else:
            print(a,c,b)
    elif b<a and b<c:
        if a<c:
            print(b,a,c)
        else:
            print(b,c,a)
    elif c<a and c<b:
        if a<b:
            print(c,a,b)
        else:
            print(c,b,a)

def feladat_2a(a,b,c):
    print(sorted([a,b,c]))


def feladat_3(x):
    if x>-2 and x<0:
        print("f(x)=",2*x)
    elif x<=0 and x<2:
        print("f(x)=",x*x)
    elif x>2:
        print("f(x)=",10)
    else:
        print("Hibás input ! ")

def feladat_4(a,b,c):
    print(min(a,b,c))
    print(max(a,b,c))

def feladat_5(a,b,c,d):
    if d>=0:
        print(a,c,b,d)
    else:
        print(a,b,d,c)

import math as mt
def feladat_6():
    while True:
        a = float(input("A haromszog oldala: "))
        b = float(input("A haromszog oldala: "))
        c = float(input("A haromszog oldala: "))
        if a<=0 or b<=0 or c<=0:
            print("Nem megfelelo adatok !")
        else:
            break
    if a+b>c and a+c>b and b+c>a:
        p = (a+b+c)/2
        T= mt.sqrt(p*(p-a)*(p-b)*(p-c))
        r= T/p
        R= a*b*c/(4*T)
        print("R=%.2f és r=%.2f" % (R,r))
    else:
        print("Nem kepezheto a haromszog !")


def main():
    feladat_1(10,5)
    feladat_2(4,8,3)
    feladat_2a(4,8,3)
    feladat_3(-1)
    feladat_4(3,6,8)
    feladat_5(5,6,3,10)
    feladat_6()
if __name__=="__main__":
    main()