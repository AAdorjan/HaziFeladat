def fel6(fajl_nev):
    try:
        fajl=open(fajl_nev, mode="r")
        sor=fajl.readline()  # kiolvas egy adott sort, itt az elsot
        sor=sor.strip()
        kapcsolo=True
        x1,y1,sz1,m1=sor.split()
        x1=int(x1)
        y1=int(y1)
        sz1=int(sz1)
        m1=int(m1)

        for sor in fajl:
            sor = sor.strip()
            x2, y2, sz2, m2 = sor.split()
            x2 = int(x2)
            y2 = int(y2)
            sz2 = int(sz2)
            m2 = int(m2)
            if not (x2>x1 and y2>y1 and x2+sz2<x1+sz1 and y2+m2<y1+m1):
                kapcsolo=False
                break
            else:
                x1=x2
                y1=y2
                sz1=sz2
                m1=m2
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

def fel7_own():  # EZ IGY NEM JO MEG !
    try:
        fajl = open("be.txt", mode="r")
        sor = fajl.readline()
        sor = sor.strip()
        line = sor.split()
        x = int(line[0])
        vary = 0
        for line in fajl:
            for i in range(len(line[1])-1):
                if i != i+1:
                    vary+=1
            if vary == x:
                print("Good")
            elif vary < x:
                print("Bad")
            else:
                print("Average")
    except Exception as e:
        print(e)
    finally:
        fajl.close()

def fel7():
    try:
        fajl = open("be.txt", mode="r")
        tmp = "abcdefghijklmnopqrstuvwxyz"
        for sor in fajl:
            sor = sor.strip()
            line = sor.split()
            x = int(line[0])
            sum = 0
            for i in tmp:
                if i in line[1]:
                    sum+=1
            if sum == x:
                print("Good")
            elif sum < x:
                print("Bad")
            else:
                print("Average")
    except Exception as e:
        print(e)
    finally:
        fajl.close()


def fel8():
    try:
        fajl1=open("turista.txt", mode="r")
        fajl2=open("ki_turista.txt", mode="w")
        min = 2000
        max = 0
        count = 0
        for sor in fajl1:
            sor=sor.strip()
            sor=int(sor)
            count+=1
            if max<sor:
                max=sor
            if min>sor:
                min=sor
        fajl2.write("%d %d" % (max-min, (count-1)*200))
    except Exception as e:
        print(e)
    finally:
        fajl1.close()
        fajl2.close()

def main():
    fel6("tegla.txt")
    fel7()
    #fel7_own()
    fel8()
main()