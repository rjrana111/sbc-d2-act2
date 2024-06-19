#print(b.title())

#print(f"{b.capitalize().replace("p", "P")}")
#replace1 = b.replace("b", "L")
#print(f"{replace1[8:12]}")

#print(f"{b[12:16].replace("p", "E")}")
#print(a.find("a"))
#print(a.find("r"))
#print(f"{b[13].title()}{b[6].title()}")

#print(b.replace(" ", "").isalpha)




#import random 

#num = random.randint(0,100)
#print(num)

#|========================


#age = int(input("pag tawas:"))
#if age < 18:
   # print("Baho ka")
#if age < 18:
    #print("baho ka baba")
#else:
 #   print("dili baho")

from random import randint as com
import os
os.system('cls')

p1 = int( input("1 - Fold  \n2 0- Unfold \n Enter Your number: "))
c1, c2= com(0,1),com(0,1)

def selected(x,y,z):
    select = ["Unfold","Fold"]
    return select[x],select[y],select[z]

def procces(p1,c1,c2):
    if p1 != c1 and p1 != c2:
        return "P1 win"
    elif c1 != c1 and c1 != c2:
        return "C1 win"
    elif c2 != c1 and c2 != c1:
        return "c2 win"
    else:
        return "DRAW!!!"


if (p1 > 1) or (p1< 0):
    print("Invalid Selection")
else:
    player, com1, com2 = selected(p1,c1,c2)
    print(f"P1 = {player}\nC1 = {com1}\nC2 = {com2}\n")
    print(procces(p1,c1,c2))










