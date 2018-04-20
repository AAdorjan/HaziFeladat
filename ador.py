import numpy as np
import matplotlib.pyplot as plt
import mpmath as mpimg

def mean_filter3(img):
    resImg=np.zeros(img.shape)

    for x in range(1,img.shape[0]-1):
        for y in range(1,img.shape[1]-1):
            resImg[x][y]=np.mean(img[x-1:x+2,y-1:y+2])
    return resImg

def mean_filter5(img):
    resImg=np.zeros(img.shape)

    for x in range(2,img.shape[0]-2):
        for y in range(2,img.shape[1]-2):
            resImg[x][y]=np.mean(img[x-2:x+3,y-2:y+3])
    return resImg

def gaus_filter(img):
    kernel=np.array([[1,2,1],[2,4,2],[1,2,1]])
    resImg = np.zeros(img.shape)
    for x in range(1, img.shape[0] - 1):
        for y in range(1, img.shape[1] - 1):
            resImg[x][y] =np.sum(kernel[:,:]*img[x-1:x+2,y-1:y+2])/np.sum(kernel)

def elad(sorlap,sornev,nkorso,bevetel):
    if sornev in sorlap:
        if sorlap[sornev][0]/5>=nkorso:
            sornev[sornev][0]=sorlap[sornev][0]-5*nkorso
            bevetel=bevetel+nkorso*sorlap[sornev][1]
        else:
            mennyivan=sorlap[sornev][0]/5
            sorlap[sornev][0]=0
            bevetel=bevetel+mennyivan*sorlap[sornev][1]
    return bevetel
def main():

    img=mpimg.imread('lena2.jpg')
    res1=mean_filter3(img)
    res2 = gaus_filter(img)
    plt.subplot(131)
    plt.imshow(res1,cmap='gray')
    plt.subplot(132)
    plt.imshow(res2,cmap="gray")
    plt.show()

    bevetel=0
    sorlap={}
    sorlap['soproni']=[600,230]
    sorlap['borsodi'] = [700, 240]
    print(sorlap)
    print(sorlap.keys())
    print(sorlap.values())
    print(elad(sorlap,"borsodi",10,bevetel))
    print (sorlap)
