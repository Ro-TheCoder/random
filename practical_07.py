def push3_5(N:list):
	only3_5=[]
	for i in N:
		if i%3==0 or i%5==0:
			only3_5.append(i)
		else: continue
	return only3_5

def main():
	Num=[]
	for i in range(5):
		Num.append(int(input("Enter list element: ")))
	
	x=push3_5(Num)
	for i in range(len(x)):
		x[i]+=10
	print(x)
	
if __name__=="__main__":
	main()
# Write a user defined function named as 'push3_5(N)' which accepts list of integer in a parameter 'N'and pushes all those integers which are divisible by 3 or 5 from the list 'N' intoa list named "only3_5".
# Write  
