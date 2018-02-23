"""import math as mt

def is_prim(n):
    prim=True
    if n==1:
        prim=False
    for i in range(2,int(mt.sqrt(n))+1):
        if n%i==0:
            prim= False
            break
    return prim


def lnko(a,b):
    while True:
        r=a%b
        a=b
        b=r
        if r==0:
            break
    return a


def palindrom(n):
    masolat=n
    uj_szam=0
    while n!=0:
        szj = n%10
        uj_szam=uj_szam*10+szj
        n=n//10

    return uj_szam==masolat


def fibsor(n):
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

def fibo2(n):
    a=1
    b=1
    k=1
    fajl=open("ki1.txt",mode="w")
    while k<n:
        fajl.write("%.4f " % (a/b))
        a=a+b
        b=a-b
        k=k+1
    fajl.close()

import codecs as cod
def feladat1(fajl_nev):
    fajl=cod.open(fajl_nev, encoding="utf-8",mode="r")

    max=0
    max_sor=""
    for sor in fajl:
        sor=sor.strip()
        if(sor[0].isupper() and  len(sor)> max):
            max=len(sor)
            max_sor=sor
    print(max,max_sor)
    fajl.close()



def feladat2():
    fajl=open("be2.txt", mode="r")
    for sor in fajl:
        if ("   " in sor):
            fajl= open("ki1.txt", mode="w")
            fajl.write(sor)
            fajl.close()
            break
"""

def fel7(lista,betu):
    li=[]
    fajl=open("ki2.txt",mode="w")
    for i in lista:
        if i[0]== betu:
            li.append(i)
    fajl.write(str(li))
    fajl.close()




def main():
    fel7(["alma","ananasz", "banan"],"a")



if __name__=="__main__":
    main()
