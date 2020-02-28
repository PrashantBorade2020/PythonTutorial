import string


print("----------String Literals ----------------") 
print("Hello")

print("----------Assign string ro variable------")

a = "Hello"
print(a)

print("----------Multiline strings------------")

a = """Lorem ipsum dolor sit amet,
consectetur adipiscing elit,
sed do eiusmod tempor incididunt
ut labore et dolore magna aliqua."""
print(a)

print("-------------- or use three single quotes ----------")

print('''Lorem ipsum dolor sit amet,
consectetur adipiscing elit,
sed do eiusmod tempor incididunt
ut labore et dolore magna aliqua.''')
print(a)

print("------- strings are arrays")

a = "hello World"

print(a[1])
print(a[2:5])
print(a[-5:-2])
print(len(a))

print("-------String Methods")
print("It returns the string")
print("The string is :" + a.strip())

print("Convert the first character to upper case ")
print("Capitalize string :" + a.capitalize())

print("Convert string into lower case")
print("lower case string :" + a.casefold())

txt = "Hello, And Welcome To My World!"

x = txt.casefold()

print(x)

print("Centered String : " + a.center(10))

txt = "I love apples, apple are my favorite fruit"

x = txt.count("apple")

print("string no of times found " + str(x))



