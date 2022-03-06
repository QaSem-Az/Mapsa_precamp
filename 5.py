# Soal 5 , my_mutable(x,y)

def my_multiple(x,y):
   
    j=0
    while y >= 1 :
        y-=1
        j=x+j
    return(j)
print(my_multiple(int(input("X: ")),int(input("y: "))))
