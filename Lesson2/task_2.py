listInput = (input("Enter you list: "))
#print (str(list))
clearList = list(map(int,listInput.split(",")))
print (str(set(clearList)))