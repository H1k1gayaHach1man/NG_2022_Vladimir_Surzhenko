newNumber = int(input("Enter you number: "))

for a in range (0, newNumber+1):
    for b in range(newNumber-a, 0, -1):
        print(b, end=" ")
    print ()

    
    