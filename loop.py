i = 1
num = int(input("Enter a number:"))
for i in range(1, 11, 1):
    print("%d X %d = %d" % (num, i, num * i))

n = int(input("Enter the number of rows you want to print?"))
i, j = 0, 0
for i in range(0, n):
    print()
    for j in range(0, i + 1):
        print("*", end="")

i = 1
b = 9
number = int(input("Enter the number?"))
while i <= 10:
    print("%d X %d = %d" % (number, i, number * i), end='\n')
    i = i + 1
