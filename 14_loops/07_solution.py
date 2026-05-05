# using for loop
# for i in range(0, 100):
    # input_num = int(input("Enter a number: "))
    # if 0 < input_num < 10:
    #     print("That is correct!!")
    #     break
    # else:
    #     print("Invalid input, try again!!")

# using while loop
while True: # while True means loop runs forever until a break is hit
    input_num = int(input("Enter a number: "))
    if 0 < input_num < 10:
        print("That is correct!!")
        break
    else:
        print("Invalid input, try again!!")

# while True version is better and preferred here because:
# keeps asking until correct input is given
# no unnecessary limit of attempts
# cleaner and more logical