
# Python Basic

def addition(v1,v2):
    ret = v1+v2
    return ret


a= int(input("enter a number\n"))
b= int(input("enter a number\n"))


add = addition(a,b)
print("addition using function is:", add)


#Reusability of the function
# No need to define or create another function (for addition of two numbers)

a= int(input("enter a number\n"))
b= int(input("enter a number\n"))

add = addition(a,b)
print("addition is:", add)