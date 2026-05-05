number = int(input("enter a number: "))

print("Table of", number ,":")
print("------------")

for i in range(1, 11):
    if i == 5:
        continue
    # print(f"{number} x {i} = {number * i}")
    print(number, 'x', i, '=', number * i)

