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


def fel7(lista,betu):
    li=[]
    fajl=open("ki2.txt",mode="w")
    for i in lista:
        if i[0]== betu:
            li.append(i)
    fajl.write(str(li))
    fajl.close()




def kivetel():
    s="alma"
    try:
        print(1/0)
        print(s[10])
        print("try-ban benn")
    except ZeroDivisionError as e:
        print("Zeroval osztottunk !")
    except Exception as e:
        print("legaltalanosabb kivetel dobodott",e)
    finally:
        print("Ez vegre hajtodik")

    print("vege a try-nak")

import sys
def fel3():
    try:
        fajl = open(sys.argv[1],mode="r")
        nagy=True
        for sor in fajl:
            li=sor.split(" ")
            for szo in li:
                if(not szo[0].isupper()):
                    nagy=False
            if nagy:
                print(sor)
                break
            else:
                nagy=True

    except Exception as e:
        print("valamilyen kivetel dobodott",e)


import sys


def fel4():
    try:
        fajl = open(sys.argv[2], mode="r")
        scoreA = 0
        scoreB = 0
        for sor in fajl:
            sor = sor.strip()
            a, b = sor.split("-")
            if a == "ko" and b == "ollo":
                scoreA = scoreA + 1
            elif a == "ko" and b == "papir":
                scoreB = scoreB + 1
            elif a == "papir" and b == "ko":
                scoreA = scoreA + 1
            elif a == "papir" and b == "ollo":
                scoreB = scoreB + 1
            elif a == "ollo" and b == "papir":
                scoreA = scoreA + 1
            elif a == "ollo" and b == "ko":
                scoreB = scoreB + 1
            else:
                scoreA = scoreA + 1
                scoreB = scoreB + 1
        if scoreB > scoreA:
            print("A masodik nyert")
        elif scoreA > scoreB:
            print("Az elso nyert")
        else:
            print ("Dontetlen")
    except OSError:
        print ("hiba a fajl megnyitasa kozben")
    except Exception:
        pass

def fel5():
    try:
        fajl=open("hallgato.txt",mode="r")
        fajl2=open("ki_hallgato.txt",mode="w")
        for sor in fajl:
            sor=sor.strip()
            h=sor.split(";")
            sum=0
            for i in h[2:]:
                sum=sum+int(i)
            fajl2.write("%s %d\n" %(h[1],sum))
    except OSError as e:
        print(e)
    except Exception:
        pass
    finally:
        fajl.close()
        fajl2.close()
"""



def main():
    fel5()


if __name__ == "__main__":
    main()

