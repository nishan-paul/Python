str = "Hello"  # not mutable
str1 = " world"
str2 = "python"
str3 = "Welcome to my 2nd world"
str4 = "abcde-bat-fghij-bat-klmno"

print(str * 3)  # prints HelloHelloHello
print(str + str1)  # prints Hello world
print(str[4])  # prints o
print(str[2:4])  # prints ll
print('w' in str)  # prints false as w is not present in str
print('wo' not in str1)  # prints false as wo is present in str1.
print(r'C://python37')  # prints C://python37 as it is written
print("The string str : %s" % str)  # prints The string str : Hello

print(str2.capitalize())
print(str3.title())
print(str3.upper())
print(str3.lower())
print(len(str4))
print(str4.count("bat"), 0, 25)
print(str4.find("bat"), 0, 25)

# isupper()
# islower()
# isnumeric()
# isdigit()
# isalpha()
