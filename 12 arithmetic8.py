

# Python Basics

# Note we are importing marevellous file here so it should be in the same directory 
# otherwise we have to give path (actual address)


import marvellous
	

def main():

	a= int(input("enter a number\n"))
	b= int(input("enter a number\n"))

	add = marvellous.addition(a,b)
	print("addition is:", add)
		
	
if __name__ == "__main__":  #OS task
	main()
	
	
	
