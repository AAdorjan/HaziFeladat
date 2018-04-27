import re

def elad(sorlap,sornev,nkorso,bevetel):
    if sornev in sorlap:
        if sorlap[sornev][0]/5>=nkorso:
            sorlap[sornev][0]=sorlap[sornev][0]-5*nkorso
            bevetel=bevetel+nkorso*sorlap[sornev][1]
        else:
            mennyivan=sorlap[sornev][0]/5
            sorlap[sornev][0]=0
            bevetel=bevetel+mennyivan*sorlap[sornev][1]
    return bevetel

def feltolt(sorlap,sornev,mennyi,ujar):
    if sornev in sorlap:
        sorlap[sornev][0]=sorlap[sornev][0]+mennyi
        sorlap[sornev][1]=ujar
    else:
        sorlap[sornev]=[mennyi,ujar]

def szoveg_hist():
    try:
        fajl=open('input.txt',mode='r')
        dic={}
        for sor in fajl:
            regex = re.compile("[^a-zA-Z]")
            sor = regex.sub(' ', sor)
            szavak=sor.split(' ')
            for szo in szavak:
                if szo in dic:
                    dic[szo]=dic[szo]+1
                else:
                    dic[szo]=1
        fajl.close()
        print(dic['Jon'])
    except Exception as e:
        print(e)


def main():
    bevetel = 0
    sorlap = {}
    sorlap['soproni'] = [600, 230]
    sorlap['borsodi'] = [700, 240]
    print(sorlap)
    print(sorlap.keys())
    print(sorlap.values())
    print(elad(sorlap, "borsodi", 10, bevetel))
    print (sorlap)

    feltolt(sorlap,"Csiki",1000,400)
    feltolt(sorlap, "Staropramen ", 200, 300)
    print(sorlap)

    s="alma,korte,szilva?"
    regex=re.compile("[^a-zA-Z]")
    s=regex.sub(' ',s)
    print(s)
    szoveg_hist()

    allat = {}
    allat['Liaz'] = "kutya"
    allat['Pamacs'] = "kutya"
    allat['Zizi'] = "kigyo"
    allat['Hajnal'] = "poni"

    for key,val in allat.items():
        print("%s egy %s" % (key,val))
    print(allat.items())

    for key in allat:
        print(key)
    allat2=allat.copy()
    allat.clear()#kiuriti a szotar tartalmat
    print(allat2.get("Liza")) #kiveszi a szotarbol a klcshoz tartozo elemet de nem torli
    print(allat2.pop("Hajnal")) #kiveszi a szotarbol es torli
    for val in allat2.values():
        print(val)

    gyumolcsok=['alma','korte','alma','szilva']
    kosar=set(gyumolcsok)
    print(kosar)

    a=set('abcabcefgh')
    b=set('ccgghhkks')
    print(a)
    print(b)
    print(a-b)
    print(a&b)
    print(a|b)
    print(a^b)

if __name__ == "__main__":
    main()


