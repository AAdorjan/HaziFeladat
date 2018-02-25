
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

def feladat_7():
    while True:
        a = float(input("A kert hossza: "))
        b = float(input("A kert szelessege: "))
        c = float(input("A drot hossza: "))
        if a<0 or b<0 or c<=0:
            print("Nem megfelelo adatok !")
        else:
            break
    K=2*(a+b)
    print("Szükséges drot: ",K)
    print("Kimaradt drot: ",c-K)


def feladat_8(x):
    if x<5:
        print("f(x)= ",3*x-5)
    elif x>=5 and x<=10:
        print("f(x)= ",10)
    elif x>10:
        print("f(x)= ", 9*x+1)

def feladat_8a(a,b,c,d):
    if a+c >2*d and b >0:
        print("E(a,b,c,d): ",d-3*b)
    elif a+c <2*d and b <0:
        print("E(a,b,c,d): ",d+3*b)
    else:
        print("E(a,b,c,d): ",4)


def feladat9(a,b,c):
    import math
    d = b ** 2 - 4 * a * c
    if d < 0:
        print("Az egyenletnek nincs valos eredmenye")
    elif d == 0:
        x = (-b + math.sqrt(b ** 2 - 4 * a * c)) / 2 * a
        print("Az egyenletnek egy megoldasa van: ", x)
    else:
        x1 = (-b + math.sqrt(b ** 2 - 4 * a * c)) / 2 * a
        x2 = (-b - math.sqrt(b ** 2 - 4 * a * c)) / 2 * a
        print("Az egyenletnek ketto megoldasa van a : ", x1, " es a ", x2)

def feladat_10(evszam1,evszam2):
    szokoev=0
    for i in range(evszam1,evszam2+1):
        if i %4 ==0 and i%100!=0 or i %400==0:
            szokoev=szokoev+1
    print("A szokoevek szama: ",szokoev)

def feladat_11():
    from datetime import datetime
    a = datetime(1999, 2, 15)
    now = datetime.now()
    days=(now - a).days
    print(days)

def main():
    feladat_1(10,5)
    feladat_2(4,8,3)
    feladat_2a(4,8,3)
    feladat_3(-1)
    feladat_4(3,6,8)
    feladat_5(5,6,3,10)
    feladat_6()
    feladat_7()
    feladat_8(12)
    feladat_8a(4,5,12,5)
    feladat9(1,10,20)
    feladat_10(1980,2400)
    feladat_11()

if __name__=="__main__":
    main()