def feladat_1(szam):
    ossz=2
    for i in range(2,szam-1):
        if szam%i==0:
            ossz=ossz+1
    if ossz==4:
        return True
    else:
        return False

def is_prime(n):
    if n < 2:
        return False
    i = 2
    while (i * i <= n):
        if n % i == 0:
            return False
        i = i + 1
    return True

def feladat_2(n):
    i = 2
    while n > 0:
        if is_prime(i):
            n = n - 1
            if n == 0:
                return i
        i = i + 1
    return -1

def feladat_3(n):
    if n > 0:
        last = n
        n &= n - 1
        while n:
            last = n
            n &= n - 1
        return last


def feladat_4():
    lista = []
    for a in range(1,10):
          for b in range(0,10):
               if a!=b:
                  for c in range(0,10):
                      if b!=c and a!=c:
                                   lista.append(str(a)+str(b)+str(c))
    return lista

def osztok_szama(szam):
    db=2
    for i in range(2,szam//2+1):
        if szam%i==0:
            db=db+1
    return db

def feladat_5(n):
    max=1
    for i in range(2,n+1):
        if max<osztok_szama(i):
            max=osztok_szama(i)
            print(i)

def feladat_6(szam1,szam2):
    list(str(szam1))
    list(str(szam2))
    if szam1[0]==szam2[0] or szam1[0]==szam2[1] or szam1[0]==szam2[2] :
        if szam1[1]==szam2[0] or szam1[1]==szam2[1] or szam1[1]==szam2[2]:
            return True
    return False

def feladat_7(szam):
    print(bin(szam), "kettes")
    print(oct(szam), "nyolcas.")
    print(hex(szam), "tizenhatos")

def feladat_7a():
    print(int("1011010101", 2))

def feladat_8a(n):
    sum=0
    for i in range(n+1):
        sum=sum+i
    print("A szamok osszege: ",sum)

def feladat_8(n):
    sum=0
    db=0
    for i in range(n+1):
        sum=sum+i
        db=db+1
        if sum>=n:
            break
        # print(db)
    print("Ennyi számot kell összeadni:",db-1)

def feladat_9():
    perc=1
    magassag=1
    while magassag<301:
        magassag = magassag + 1 / magassag
        perc = perc + 1
    print("Ennyi perc alatt jut el: ",perc)

def feladat_10():
    max = 0
    max_sor = ""
    fajl = open("be1.txt", mode="r")
    for sor in fajl:
        sor = sor.strip()
        if (sor[0].isupper() and len(sor) > max):
            max = len(sor)
            max_sor = sor
    print("Leghosszabb nagybetus szo hossza:",max)
    fajl.close()

def feldat_11():
    min = 100
    min_sor = ""
    fajl = open("be1.txt", mode="r")
    for sor in fajl:
        sor = sor.strip()
        if ("." in sor and len(sor) < min):
            min = len(sor)
            min_sor = sor
        elif( "?" in sor and len(sor) < min):
            min = len(sor)
            min_sor =sor
        elif ( "!" in sor and len(sor) < min):
            min = len(sor)
            min_sor = sor
    print("Legrövidebb . ! ? szo hossza:", min,min_sor)
    fajl.close()

def feladat_12():
    fajl = open("be.txt", mode="r")
    for sor in fajl:
        sor = sor.strip()
        fajl = open("ki2.txt", mode="w")
        fajl.write(sor)
        fajl.close()

def osszeg2(n):
    s = 0
    while n:
        s -= n % 10
        n //= 10
    return s

def feladat_13(szam):
    db=0
    fajl = open("be.txt", mode="r")
    for sor in fajl:
        sor = sor.strip()
        if sor >osszeg2(szam):
            db=db+1


def feladat_14():
    fajl = open("be.txt", mode="r")
    for sor in fajl:
        sor = sor.strip()
        fajl = open("ki2.txt", mode="w")
        fajl.write(sor)
        fajl.close()


def feladat_15():
    fajl = open("be3.txt", mode="r")
    for sor in fajl:
        if sor=="":
            break
        else:
            fajl = open("ki1.txt", mode="w")
            sor = sor.strip()
            fajl.write(sor)
            fajl.close()
            print(sor)

def feladat_16():
    try:
        fajl = open("be5.txt",mode="r")
        nagy=True
        for sor in fajl:
            li=sor.split(" ")
            for szo in li:
                if(not szo[0].isupper()):
                    nagy=False
            if nagy:
                fajl = open("ki2.txt", mode="w")
                fajl.write(sor)
                fajl.close()
                print(sor)
                break
            else:
                nagy=True
    except Exception as e:
        print("valamilyen kivetel dobodott",e)


def feladat_17():
    try:
        fajl = open("be6.txt",mode="r")
        kicsi=True
        for sor in fajl:
            li=sor.split(" ")
            for szo in li:
                if(not szo[0].islower()):
                    kicsi=False
            if kicsi:
                fajl = open("ki3.txt", mode="w")
                fajl.write(sor)
                fajl.close()
                print(sor)
                break
            else:
                kicsi=True
    except Exception as e:
        print("valamilyen kivetel dobodott",e)

def feladat_18():
    try:
        fajl = open("be7.txt",mode="r")
        scoreA = 0
        scoreB = 0
        for sor in fajl:
            sor = sor.strip()
            a, b = sor.split(":")
            print(a,b)
            if a>b:
                scoreA=scoreA+1
            elif b>a:
                scoreB=scoreB+1
        if scoreB > scoreA:
            print("A masodik nyert")
        elif scoreA > scoreB:
            print("Az elso nyert")
    except OSError:
        print ("hiba a fajl megnyitasa kozben")
    except Exception:
        pass


def feladat_19():
    li=[]
    fajl = open("be8.txt", mode="r")
    for sor in fajl:
        sor=sor.strip()
        a,b = sor.split(" ")
        print(b)
        li.append(b)
    print(li)
    print("Legtobb nezzetseg: ",max(li))

def feladat_20():
    li = []
    fajl = open("be9.txt", mode="r")
    for sor in fajl:
        sor = sor.strip()
        a,b,c = sor.split(";")
        print(c)
        li.append(c)
    print(li)
    kutya=max(li)
    print("Város: ",kutya)

def feladat_21():
    fajl = open("be11.txt", mode="r")
    for sor in fajl:
        sor = sor.strip()
        sor = sor.split(";")
        print(sor)
        #print(sum(sor))

def feladat_22():
    li = []
    fajl = open("be10.txt", mode="r")
    for sor in fajl:
        sor = sor.strip()
        a, b, c = sor.split(";")
        print(c)
        li.append(c)
    print(li)
    kutya = min(li)
    print(kutya)

def feladat_23():
    try:
        fajl = open("be1.txt", mode="r")
        sor = fajl.readline()
        sor = sor.strip()
        kapcsolo = True
        x1, y1= sor.split()
        x1 = int(x1)
        y1 = int(y1)
        for sor in fajl:
            sor = sor.strip()
            x2, y2, sz2, m2 = sor.split()
            x2 = int(x2)
            y2 = int(y2)
            sz2 = int(sz2)
            m2 = int(m2)
            if not (x2 > x1 and y2 > y1 and x2 + sz2 < x1 ):
                kapcsolo = False
                break
            else:
                x1 = x2
                y1 = y2
        if kapcsolo:
            print("YES")
        else:
            print("NO")
    except OSError as e:
        print(e)
    except Exception as e:
        print(e)
    finally:
        fajl.close()

def main():
    print(feladat_1(8))
    print(feladat_2(5))
    print(feladat_3(513))
    print(feladat_4())
    feladat_5(20)
    print(feladat_6("122","211"))
    feladat_7(342)
    feladat_7a()
    feladat_8a(5)
    feladat_8(5)
    feladat_9()
    feladat_10()
    feldat_11()
    #feladat_12()
    #feladat_13()
    #feladat_14()
    feladat_15()
    feladat_16()
    feladat_17()
    feladat_18()
    feladat_19()
    feladat_20()
    feladat_21()
    feladat_22()
    #feladat_23()
    #print(osszeg2(28))








if __name__ == "__main__":
    main()