
# Declaring variables 
x = 5 # x is of type int
y= "John" # y is of type str

print(x)
print(y)
#-------------------------------
#Legal Varial names:
print("Leagal Varible names are :")
print("""
myVar = "John"
my_Var = "John"
_my_Var = "John"
myvar = "John"
MYVAR = "John"
MYVAR2 = "Jonh"
""")

#Illegal Varible names:
print("Illegal Varialble are :")
print("""
2myvar = "Vidushi"
my-var = "Vidushi"
my var = "Vidushi"
""")

#Assign Value to Multiple Variable

x ,y, z = "Orange","Banana","Cherry"

print(x)
print(y)
print(z)

x = y = z = "Orange"

print(x)
print(y)
print(z)


#concatnate to str 
firstName = "Vidushi"
lastName = "Infotech"

print(firstName + " " +  lastName)
x = 5 
y = 5

print(x + y)

# Global Variabl Declaration

x = "awesome"

def myfunc() :
	print("Python is " + x)

myfunc()
