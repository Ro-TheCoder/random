
# write a program to write a binary file with only dictionaries and read it later as per menu. 
import pickle

def create_f(filename:str,m_admno:list,m_values:list):
	try:
		f1=open(filename, 'wb')
		d={}
		for i in m_admno:
			d[i]=m_values[i.index()]
		pickle.dump(f1,d)
		return {"process":"completed"}
	except:
		return {"process":"error"}

def read_f(filename):
	try:
		f1=open(filename,'rb')
		content=pickle.load(f1)
		return {"contents":content}
	except:
		return{"contents":False}
		
def main():
	flag=True
	while flag==True:
		print("1 --> Create a file of data\n2 --> Read a file of data\n3 --> Exit the program")
		choice=int(input("Enter choice: "))
		if choice==1:
			admno=[]
			values=[]
			try:
				x=int(input("enter number of records you want to enter:"))
				for i in range(x):
					admno.append(input("Enter admno of record no.{}".format(i).strip()))
