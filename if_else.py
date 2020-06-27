marks = int(input("Enter the marks? "))
if 85 < marks <= 100:
    print("Congrats ! you scored grade A ...")
elif 60 < marks <= 85:
    print("You scored grade B + ...")
elif 40 < marks <= 60:
    print("You scored grade B ...")
elif 30 < marks <= 40:
    print("You scored grade C ...")
else:
    print("Sorry you are fail ?")
