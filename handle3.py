import pickle

f1=open("binary_wali.dat",'wb')

lst=[10,2,3,4,5,6]
pickle.dump(lst,f1)

f1.close()
f2=open("binary_wali.dat",'rb')
x=pickle.load(f2)
print(x)
