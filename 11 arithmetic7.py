
# Python Basics

def addition(v1,v2):
    ret = v1+v2
    return ret
	
def substraction(v1,v2):
    ret = v1-v2
    return ret

def main():

	a= int(input("enter a number\n"))
	b= int(input("enter a number\n"))

	add = addition(a,b)
	print("addition is:", add)


	a= int(input("enter a number\n"))
	b= int(input("enter a number\n"))

	sub = substraction(a,b)
	print("Substraction is:", sub)
	
	
	
if __name__ == "__main__":  #OS task
	main()