# soal 3 =====> Max Min

a= int (input ("Enter First Number : "))
b= int (input("Enter 2st Number : "))
c= int (input (" Enter 3st Number : "))
max = a
min = b
if max < b :
    max = b
if max < c :
    max = c 
print ("max is : ", max) 
if min > a :
    min = a 
if min > c :
    min = c 
print ("min is : ", min )

