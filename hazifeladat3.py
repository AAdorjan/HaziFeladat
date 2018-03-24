def feladat_1(n):
    sum = 1
    list = []
    k=[]
    k1=[]
    for n in range(n):
        x = int(input('Enter number : '))
        list.append(x)
    print(list)
    for i in range(len(list)):
        if list[i]<7:
            k.append(list[i])
            sum = sum * k[i]
        i+=1
    for i in range(len(list)):
        if list[i]>10:
            k1.append(list[i])

        i+=1


    print(k)
    print(k1)
    print(sum)





def main():

    feladat_1(5)



if __name__ == "__main__":
    main()