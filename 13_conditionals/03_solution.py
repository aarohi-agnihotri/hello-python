grade = int(input("enter your score: "))

if grade < 0 or grade > 100:
    print("Invalid score entered")
    exit() # stops the program immediately, no further code will run
elif (grade < 60):
    print("You got grade F")
elif(grade < 70):
    print("You got grade D")
elif(grade < 80):
    print("You got grade C")
elif(grade < 90):
    print("You got grade B")
else:
    print("You got grade A")