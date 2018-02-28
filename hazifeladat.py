
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
    print("Megélt napok száma: ",days)

def feladat_12(maxpont,elertpont):
    if elertpont>= maxpont*0.6:
        print("Sikeres")
    else:
        print("Sikertelen")

def feladat_13(jegy):
    if jegy==1:
        print("Elegtelen")
    elif jegy==2:
        print("Elegseges")
    elif jegy==3:
        print("Kozepes")
    elif jegy == 4:
        print("Jo")
    elif jegy==5:
        print("Kivalo")

def feladat_14(honapszama):
    if honapszama==1:
        print("Januar")
    elif honapszama==2:
        print("Februar")
    elif honapszama==3:
        print("Marcius")
    elif honapszama==4:
        print("Aprilis")
    elif honapszama==5:
        print("Majus")
    elif honapszama==6:
        print("Junius")
    elif honapszama==7:
        print("Julius")
    elif honapszama==8:
        print("Augusztus")
    elif honapszama==9:
        print("Szeptember")
    elif honapszama==10:
        print("Oktober")
    elif honapszama==11:
        print("November")
    elif honapszama==12:
        print("December")

def feladat_15(a,b):
    hanyados=0
    while a>=b:
        hanyados= hanyados+1
        a=a-b
    print(hanyados)

def feladat_16(a,b):
    while True:
        r=a%b
        a=b
        b=r
        if r==0:
            break
    print(a)

def feladat_17(n):
    masolat=n
    uj_szam=0
    while n!=0:
        szj = n%10
        uj_szam=uj_szam*10+szj
        n=n//10
    print(uj_szam==masolat)

def feldat_18(x,y):
    eredmeny = 0
    while y != 0:
        if (y % 2 != 0):
            eredmeny = eredmeny + x
            x = x * 2
            y = y // 2
        if (y % 2 == 0):
            x = x * 2
            y = y // 2
    print("Az eredmeny: ", (eredmeny))

def feladat_19(n):
    prim=True
    if n==1:
        prim=False
    for i in range(2,int(mt.sqrt(n))+1):
        if n%i==0:
            prim= False
            break
    print(prim)

def feladat_20(n):
    a=1
    b=1
    if n==1:
        print(a)
    elif n==2:
        print(a,b)
    else:
        c=a+b
        print(a,b,c)
        k=3
        while k<n:
            a=b
            b=c
            c=a+b
            print(c)
            k+=1

def feladat_21(n):
  ujszam = 0
  while n > 0:
    ujszam = (10*ujszam) + n%10
    n //= 10
  print(ujszam)


def feladat_22(x, n):
    if x > 0 and n > 6:
        eredmeny = 1
        while n > 0:
            if n % 2 == 0:
                n = n / 2
                x = x * x
            else:
                n = n - 1
                eredmeny = eredmeny * x
                n = n / 2
                x = x * x
        print (eredmeny)

def feladat_22a(x,n):
    import math
    if x >0 and n>6:
        print(math.pow(x, n))

def feladat_23(n):
    sum = 0
    for x in range(1, n):
        if n % x == 0:
            sum += x
    return sum == n

def feladat_24():
    hettel = 0
    tizenh = 0
    a = float(input("Szám: "))
    while a>0:
        a = float(input("Szám: "))
        if a%7==5:
            hettel=hettel+1
        elif a%13==7:
            tizenh=tizenh+1
    print(hettel,tizenh)

def feladat_25(lakossag ,terulet):
    nepsuruseg= lakossag/terulet
    if nepsuruseg<50:
        print("Ritkan lakott nepsuruseg a",nepsuruseg, "fo/km^2")
    elif nepsuruseg>50 and nepsuruseg<300:
        print("Atlagos nepsuruseg a ", nepsuruseg, "fo/km^2")
    elif nepsuruseg>300:
        print("Surun lakott nepsuruseg a ", nepsuruseg, "fo/km^2")

def feladat_26():
    i = int( input ("Szam: "))
    count_pos = 0
    count_neg = 0
    osszead=0
    if (i != 0):
        while (i != 0):
            osszead=osszead+i
            if osszead==0:
                break
            print("Eddigi osszeg:",osszead)
            if (i > 0):
                count_pos += 1
            elif (i < 0):
                count_neg += 1
            i = int( input ("Szam: "))
        print ("Pozitiv szamok db: ", count_pos)
        print ("Negativ szamik db: ", count_neg)

def feladat_27():
    count_pos = 0
    count_neg = 0
    a1 = int(input("Szam: "))
    a2 = int(input("Szam: "))
    while a1 >0 and a2 <0 :
        if a1>0:
            count_pos += 1
        elif a2<0:
            count_neg += 1
        a1 = int(input("Szam: "))
        a2 = int(input("Szam: "))

    print("Pozitiv szamok db: ", count_pos)
    print("Negativ szamik db: ", count_neg)

def feladat_28(n):
    if n>1:
        x = n
        y = (x + 1) // 2
        while y < x:
            x = y
            y = (x + n // x) // 2
        print (x)

def feladat_29(n):
    if n == 0:
        return 1
    elif n >= 1 and n<12:
        return n * feladat_29(n-1)

def feladat_30(year,month,day):
    import datetime as dt
    days_in_the_year = (dt.date(year, month, day) - dt.date(year, 1, 1)).days + 1
    print(days_in_the_year)


import math
def feladat_31(n):
    i = 1
    while i <= math.sqrt(n) + 1:
        if (n % i == 0):
            if (n/i == i):
                print(i)
            else:
                print(i,n/i,)
        i = i + 1

def feladat_31a(n):
    i = 1
    while i < n:
        if n % i == 0:
            print(i, end =" ")
        i = i + 1

def feladat_31b(n):
    for i in range(1, n + 1):
        if (n % i == 0):
            print(i, end= " ")


def feladat_32(n1,n2,k):
    for i in range(n1,n2+1):
        if i %k==0:
            print(i, end=";")

def feladat_34(n):
    primek = []
    for num in range(1, n + 1):
        limit = int(num ** 0.5) + 1
        for div in range(2, limit):
            if (num % div) == 0:
                break
        else:
            primek.append(num)
    return (primek)
def feladat_34a(num):
    primek = feladat_34(num)

    for i in range(num // 2 + 1):
        if num % 2 != 0:
            print(num)
            break
        if i in primek and (num - i) in primek:
            print(i, '+', num - i)


def feladat_33(n):
    eredmeny = []
    for i in range(n+1):
        c = 0
        for n in range(1, i + 1):
            if i % n == 0:
                c += 1
        eredmeny.append(c)
    print(eredmeny.index(max(eredmeny)))


def feladat_35(n):
    for i in range(2, n):
        if n % i == 0:
            return False
    return True

def feladat_36(l):
    sum=0
    n=100
    a=1
    b=1
    if n==1:
        print(a)
    elif n==2:
        print(a,b)
    else:
        c=a+b
        print(a,b,c)
        k=3
        while k<n:
            a=b
            b=c
            c=a+b
            print(c)
            if c>l-a:
                break
            else:
                k += 1
                sum+=1
        print("Darabszam: ",sum)


def feladat_37(l):
    n=100
    a=1
    b=1
    if n==1:
        print(a)
    elif n==2:
        print(a,b)
    else:
        c=a+b
        print(a,b,c)
        k=3
        while k<n:
            a=b
            b=c
            c=a+b

            if c>l:
                print(c)
                break
            else:
                k += 1

def feladat_38(szam,szamjegy):
    sum=0
    for i in str(szam):
        if i[0]== str(szamjegy):
            sum+=1
    print("Szamjegyek db: ",sum)

def szamjegysum(n):
    sum = 0
    kob=n*n*n
    while (n > 0):
        dig = n % 10
        sum = sum + dig
        n = n // 10
    print("Szamjegyek osszege:", sum)

def feladat_39(n):
    sum = 0
    kob = n * n * n
    while (n > 0): #for i in range(1,1001)
        dig = n % 10
        sum = sum + kob
        n = n // 10
    print("Szamjegyek osszege:", sum)

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
    feladat_12(100,63)
    feladat_13(4)
    feladat_14(2)
    feladat_15(100,20)
    feladat_16(360,225)
    feladat_17(131)
    feldat_18(45,17)
    feladat_19(7)
    feladat_20(5)
    feladat_21(6243353)
    feladat_22a(2,8)
    feladat_22(2,8)
    print(feladat_23(6))
    feladat_24()
    feladat_25(1000,100)
    feladat_26()
    feladat_27()
    feladat_28(4554)
    print(feladat_29(10))
    feladat_30(1999,1,5)
    feladat_31(100)
    feladat_31a(100)
    feladat_31b(100)
    feladat_32(2,160,5)
    feladat_34a(56)
    feladat_33(3240)
    feladat_35(21)
    feladat_36(236)
    feladat_37(236)
    feladat_38(1234222,2)
    szamjegysum(123)
    feladat_39(123)











if __name__=="__main__":
    main()