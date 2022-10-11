def sel_sort(lst):
	num=len(lst)
	for i in range(num):
		x=lst[i:]
		minim=x[0]
		for n in x:
			if n<minim:
				minim=n
			else: pass
				
		print("before",lst)
		lst.remove(minim)
		print(minim)
		lst.insert(i,minim)
		print("after",lst)
	print(lst)

ln=[5,4,8,2,3]
sel_sort(ln)
