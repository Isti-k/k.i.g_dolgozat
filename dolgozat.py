import random
"""a)	Kérj be 1 páros számot a felhasználótól. (1 pont)
    Amennyiben nem páros számot ad meg a felhasználó, akkor kérd be újra a számot, addig, amíg páros számot nem ad meg!  (1 pont)
    A bekéréshez írj egy függvényt beker(), amely bekéri a kívánt feltételeknek megfelelő számot. . (1 pont)
    """

def beker():
    print("1. feladat:")
    print("a")
    szam:int=int(input("Kérek egy páros számot!"))
    while not(szam % 2 == 0):   
        szam:int=int(input("Ez nem páros! Páros számot kérek!"))
    return szam

def beker2():
    print("1. feladat:")
    print("b")
    i:int=1
    szam:int=int(input(f"Kérek az {i}. egy páros számot!"))
    for i in range(3): 
        if szam % 2 == 0:
            szam+=1
            return szam
        else:
            szam:int=int(input(f"Ez nem páros! {i+1} Páros számot kérek!"))
    return szam


lista=[]
def veletlen():
    szam1:random.randint(-40,150)
    


