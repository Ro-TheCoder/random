print("Enter list of elements you want to enter: ")
l=[]
for x in range(10):
	t=float(input())
	l.append(t)
ele=float(input("Enter the element whose location you want to know: "))
if ele in l:
	print("{} in list is at index = {}".format(ele,l.index(ele)))
else:
	print("{} not found in list".format(ele))
