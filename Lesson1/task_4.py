a = float (input("Enter a: "))   
b = float (input("Enter b: ")) 
c = float (input("Enter c: ")) 
#Request coefficients
D = b**2 - 4*a*c    
#Calculate the discriminant of the quadratic equation
if D < 0:    
    print ("Discriminant = 0")
    print ("no roots")
elif D == 0:     
    x = (-b + D** .5) / (2*a)
    print ("Discriminant = ", D)
    print ("One root: ", x)
else:    
    x1 =  (-b + D** .5) / (2*a)
    x2 =  (-b - D** .5) / (2*a)
    print ("Disriminant = ", D)
    print ("There are 2 roots: ")
    print ("Root 1 =  ", x1)
    print ("Root 2 =  ", x2)
