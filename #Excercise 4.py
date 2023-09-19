#Excercise 4.1 
var1= 10
var2= 20
var3 = 50
average= (var1+var2+var3)/3 #surely a way to make a count of different values used in an average
print(average) #tried to find an average function but nothing seemed to work right


#4.2)
pi = 3.14159
radius = 5
print(str("The surface area of a circle with radius"), radius, str("is"), (radius**2)*pi) 

# 4.3)
amount = 9999
dollars= 100
quarters= 25
dimes= 10
nickels= 5
pennies= (((amount%dollars)%quarters)%nickels)/1
print('$',amount//dollars, int((amount%dollars)//quarters), 'quarters', int(((amount%dollars)%quarters)//dimes),
      'dimes', int(((amount%dollars)%quarters)//nickels), 'nickels', int(pennies), 'pennies')

#4.4 
a = 17
b = 23
print( "a =", a, "and b =", b )
a += b
b = a-b
a -=b
print( "a =", a, "and b =", b )
