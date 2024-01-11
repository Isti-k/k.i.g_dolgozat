import random
"""a)	Kérj be 1 páros számot a felhasználótól. (1 pont)
    Amennyiben nem páros számot ad meg a felhasználó, akkor kérd be újra a számot, addig, amíg páros számot nem ad meg!  (1 pont)
    A bekéréshez írj egy függvényt beker(), amely bekéri a kívánt feltételeknek megfelelő számot. . (1 pont)
    """
paros_lista=[]
def beker(paros_lista):
    print("1. feladat:")
    print("a")
    szam:int=int(input("Kérek egy páros számot!"))
    while not(szam % 2 == 0):   
        szam:int=int(input("Ez nem páros! Páros számot kérek!"))
    return szam

def beker2(paros_lista):
    print("1. feladat:")
    print("b")
    i:int=1
    szam:int=int(input(f"Kérek az {i}. egy páros számot!"))
    for i in range(3): 
        if szam % 2 == 0:
            i+=1
        else:
            szam:int=int(input(f"Ez nem páros! {i+1}. Páros számot kérek!"))
    return (szam * 3).append(paros_lista)


def beker(paros_lista):
    min:int=0
    for i in range(0,len(paros_lista),1):
        if paros_lista[i] <= paros_lista[min]:
            min+=i
    print(f"{i}. lépésben adta meg a legkisebb páros számot, melynek értéke:{min}")
    return paros_lista


lista=[]
def veletlen():
    for i in range(0,13,1):
        szam=random.randint(-40,150)
        lista.append(szam)
        if i > 12:
            print(szam, end=",")
        else:
            print(szam,end=" ")

def ketjegyuek_szama(lista):
    osszeg=0
    for i in range(0, len(lista), 1):
        if 100 > lista[i] > 9 or -100 < lista[i] < -9:
            osszeg += 1
    return osszeg
    
def paratlan_osszege(lista):
    osszeg = 0
    for i in range(0, len(lista), 1):
        if lista[i] % 2 != 0:
            osszeg += lista[i]
    return osszeg

def paros_osszege(lista):
    osszeg = 0
    for i in range(0, len(lista), 1):
        if lista[i] % 2 == 0:
            osszeg += lista[i]
    return osszeg

def kiir():
    
