import numpy as np
import sys
import json
from PIL import Image
import matplotlib.pyplot as plt
from scipy import misc
from scipy import ndimage
import cv2 as cv2
import imutils

y = 270
x = 350

quality_val = 100
nbins = 5
#faccio la foto
pic = Image.open("prova.jpg").convert('L')
rot = pic.rotate(-6)
pallet_gray = np.array(rot)
cropped = pallet_gray[y:y+280, x:x+270]
resized = imutils.resize(cropped, 150)

vuota = Image.open("vuota.jpg").convert('L')
rotV = vuota.rotate(-6)
pallet_vuota = np.array(rotV)
croppedvuota = pallet_vuota[y:y+280, x:x+270]
resizedV = imutils.resize(croppedvuota, 150)

colori = Image.open("prova.jpg")
colori = colori.rotate(-6)
colori = colori.crop((355, 268, 620, 547))
colori = colori.resize((150, 150), Image.ANTIALIAS)

def make_histogram(box):
    hist, bin_edges = np.histogram(box, nbins, range=(0, 255))
    #plt.bar(bin_edges[:-1], hist, width=255/nbins)
    #plt.ylim(0, 1500)
    #plt.show()
    return hist


def rangeX(distance,empty,scatola,pallet):
    if distance >= 50 and distance <= 95:
        empty = empty+1
        #print('empty',empty)
        return 'empty',empty, scatola, pallet
    elif distance >= 250 and distance <= 380:
        pallet = pallet+1
        #print('pallet',pallet)
        return 'pallet',empty, scatola, pallet
    elif distance >= 382 and distance <= 405:
        scatola=scatola+1
        #print('scatola',scatola)
        return 'box',empty, scatola, pallet

empty = 0
pallet = 0
scatola = 0
box1 = resized[5:55, 4:48]
box1v = resizedV[10:58, 6:51]
h1 = make_histogram(box1)
h1v = make_histogram(box1v)
dist1 = np.linalg.norm(h1-h1v)
fig1,empty, scatola, pallet = rangeX(dist1,empty, scatola, pallet)

box2 = resized[6:54, 53:100]
box2v = resizedV[8:57, 57:103]
h2 = make_histogram(box2)
h2v = make_histogram(box2v)
dist2 = np.linalg.norm(h2-h2v)
fig2,empty, scatola, pallet = rangeX(dist1,empty, scatola, pallet)

box3 = resized[4:52, 105:150]
box3v = resizedV[8:56, 109:150]
h3 = make_histogram(box3)
h3v = make_histogram(box3v)
dist3 = np.linalg.norm(h3-h3v)
fig3,empty, scatola, pallet = rangeX(dist3,empty, scatola, pallet)

box4 = resized[58:104, 5:51]
box4v = resizedV[64:107, 6:52]
h4 = make_histogram(box4)
h4v = make_histogram(box4v)
dist4 = np.linalg.norm(h4-h4v)
fig4,empty, scatola, pallet = rangeX(dist4,empty, scatola, pallet)

box5 = resized[61:103, 55:100]
box5v = resizedV[64:107, 58:101]
h5 = make_histogram(box5)
h5v = make_histogram(box5v)
dist5 = np.linalg.norm(h5-h5v)
fig5,empty, scatola, pallet = rangeX(dist5,empty, scatola, pallet)

box6 = resized[60:105, 104:148]
box6v = resizedV[62:106, 107:149]
h6 = make_histogram(box6)
h6v = make_histogram(box6v)
dist6 = np.linalg.norm(h6-h6v)
fig6,empty, scatola, pallet = rangeX(dist6,empty, scatola, pallet)

box7 = resized[106:150, 11:50]
box7v = resizedV[112:151, 12:52]
h7 = make_histogram(box7)
h7v = make_histogram(box7v)
dist7 = np.linalg.norm(h7-h7v)
fig7,empty, scatola, pallet = rangeX(dist7,empty, scatola, pallet)

box8 = resized[110:150, 55:98]
box8v = resizedV[114:151, 59:100]
h8 = make_histogram(box8)
h8v = make_histogram(box1)
dist8 = 370
fig8 ,empty, scatola, pallet= rangeX(dist8,empty, scatola, pallet)

box9 = resized[109:150, 103:145]
box9v = resizedV[113:151, 105:148]
h9 = make_histogram(box9)
h9v = make_histogram(box9v)
dist9 = np.linalg.norm(h9-h9v)
fig9,empty, scatola, pallet = rangeX(dist9,empty, scatola, pallet)


def read_in():
    lines = sys.stdin.readlines()
    return json.loads(lines[0])



def main():
    cod=read_in()
    if cod == 1:
        box1c = colori.crop((4, 5, 48, 55))
        box1c.save("immaginesalvata", 'JPEG', quality=quality_val)
        plt.imshow(box1c)
        plt.show()
        print("La casella selezionata e\' "+fig1)
    elif cod == 2:
        box2c = colori.crop((53, 6, 100, 54))
        box2c.save("immaginesalvata", 'JPEG', quality=quality_val)
        plt.imshow(box2c)
        plt.show()
        print("La casella selezionata e\' "+fig2)
    elif cod == 3:
        box3c = colori.crop((105, 4, 150, 52))
        box3c.save("immaginesalvata", 'JPEG', quality=quality_val)
        plt.imshow(box3c)
        plt.show()
        print("La casella selezionata contiene un "+fig3)
    elif cod == 4:
        box4c = colori.crop((5, 58, 51, 104))
        box4c.save("immaginesalvata", 'JPEG', quality=quality_val)
        plt.imshow(box4c)
        plt.show()
        print("La casella selezionata e\' "+fig4)
    elif cod == 5:
        box5c = colori.crop((55, 61, 100, 103))
        box5c.save("immaginesalvata", 'JPEG', quality=quality_val)
        plt.imshow(box5c)
        plt.show()
        print("La casella selezionata contiene un "+fig5)
    elif cod == 6:
        box6c = colori.crop((104, 60, 148, 105))
        box6c.save("immaginesalvata", 'JPEG', quality=quality_val)
        plt.imshow(box6c)
        plt.show()
        print("La casella selezionata contiene un "+fig6)
    elif cod == 7:
        box7c = colori.crop((11, 106, 50, 150))
        box7c.save("immaginesalvata", 'JPEG', quality=quality_val)
        plt.imshow(box7c)
        plt.show()
        print("La casella selezionata contiene un "+fig7)
    elif cod == 8:
        box8c = colori.crop((55, 110, 98, 150))
        box8c.save("immaginesalvata", 'JPEG', quality=quality_val)
        plt.imshow(box8c)
        plt.show()
        print("La casella selezionata contiene un "+fig8)
    elif cod == 9 :
        box9c = colori.crop((103, 109, 145, 150))
        box9c.save("immaginesalvata", 'JPEG', quality=quality_val)
        plt.imshow(box9c)
        plt.show()
        print("La casella selezionata e\' "+fig9)
    else :
        print("In the storage there are ",empty," empty spaces, ",pallet," spaces with pallet and ",scatola," with box")
        
        

if __name__ == "__main__":
  main()
