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

def main():
    print(feladat_1(8))
    print(feladat_2(5))
    print(feladat_3(513))
    print(feladat_4())
    feladat_5(20)
    print(feladat_6("122","211"))
    feladat_7(342)
    feladat_7a()

if __name__ == "__main__":
    main()