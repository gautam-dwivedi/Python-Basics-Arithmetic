
#Python Basics

#definition of addition function
def Addition(no1,no2):
	ans= no1 + no2
	return ans

#definition of subtraction function
def Subtraction(no1,no2):
	ans= no1 - no2
	return ans
	

#entry point function
def main():
	print("enter first number")
	value1= int(input())
	print("enter second number")
	value2  = int(input())
	
	ret1= Addition(value1,value2)
	ret2= Subtraction(value1,value2)
	
	print("addition is:",ret1)
	print("subtraction is:",ret2)
	

#code starter
if __name__== "__main__":
	main()
