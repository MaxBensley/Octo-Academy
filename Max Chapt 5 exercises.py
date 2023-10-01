# Exc 5.1 - len
print(len(input("Hey there, please write some stuff:")))

#Exc 5.2 - pythag
from math import sqrt
sidea = input("put in length o one triangle side here:")
sidea= int(sidea)
sideb= input("aaand the other side?:") #I would getinteger but cant get pcinput module to load
sideb= int(sideb)
asq = int(sidea*sidea)
bsq= int(sideb*sideb) 
csq= asq+bsq
print(f"So {sidea} sqaured + {sideb} squared = {csq}")
print(f"and so the other side c= {sqrt(csq)}") 

#Exc 5.3 - min max avg
var1= input("Hiii please input 3 numbers, first:")
var1= float(var1)
var2= input("great! and the next one?:")
var2= float(var2)
var3= input("just one more pls:")
var3= float(var3)
avrg= (var1+var2+var3)/3
print(f"the largest is {max(var1,var2,var3)} ")
print(f"the smallest is {min(var1,var2,var3)}")
print(f"The average of these is {avrg}")

#Exc 5.4 values of e
from math import exp
e1 = round(exp(1), 5)
e2 = round(exp(2), 5)
e3 = round(exp(3),5)
en1 = round(exp(-1), 5)
e0 = round(exp(0), 5)
print(f"the values of 'e' to power of 1, 2, 3, -1, and 0 respectively are: {e1, e2, e3, en1, e0} ") 
#not sure why it's printing with brackets?

#Exc 5.5 -
from random import random
rando= round(10*random(),20)
if rando >= 1:
    print(rando)
#this feels cheeky but works? must be cleaner way to get random in these value ranges