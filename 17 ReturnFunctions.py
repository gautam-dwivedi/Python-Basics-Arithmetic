
#Python Basics

def calculation(v1,v2):
	add = v1+v2
	sub = v1-v2
	mul = v1*v2
	div = v1/v2
	return add,sub,mul,div

def main():
	no1 = int(input("Enter first number \n"))
	no2 = int(input("Enter second number \n"))

	add,sub,mult,div = calculation(no1,no2)
	
	print("Addition is:",add)
	print("Subtraction is:",sub)
	print("Multiplication is:",mult)
	print("Division is:",div)


if __name__== "__main__":
	main()