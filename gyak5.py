def osztok_szama(szam):
    db=2
    for i in range(2,szam//2+1):
        if szam%i==0:
            db=db+1
    return db

def eros(n):
    max=1
    for i in range(2,n+1):
        if max<osztok_szama(i):
            max=osztok_szama(i)
            print(i)

def szavak_fordit(n):
    szo=input("szo: ")
    if n>1:
        szavak_fordit(n-1)
    else:
        print("A forditott sorrend")
    print(szo)

def faktorialis(n):
    if n==0:
        return 1
    else:
        return n*faktorialis(n-1)

def osszeg(szam):
    if szam==0:
       return 0
    else:
        return osszeg(szam//10)+szam%10

def osszeg2(n):
    s = 0
    while n:
        s += n % 10
        n //= 10
    return s

import numpy as np
def lnko(m,n):
    mar=m%n
    if mar==0:
        return n
    else:
        return lnko(n,mar)

def rel_prim(t,n):
    for i in range(0,n-1):
        for j in range(i+1,n):
            if lnko(t[i],t[j])!=1:
                return False
    return True

def main():
    n=int(input())
    tomb=np.empty(n,type="int")

    for i in range(0,n):
        tomb[i]=int(input())


if __name__=="__main__":
    main()


