# items = ["apple", "banana", "orange", "apple", "mango"]

# taking input from user
items = input("Enter items separated by comma: ").split(",")
# "apple,banana,apple" → ["apple", "banana", "apple"]

# using .count() method
for item in items:
    if items.count(item) > 1:
        print("Duplicate item (using count): ", item)
        break

# using set()
unique_set = set()
for item in items:
    if item in unique_set:   # already visited = duplicate
        print("Duplicate item (using set): ", item)
        break
    unique_set.add(item)

# using dictionary
char_count = {}  #empty dictionary
for item in items:
    if item in char_count:  # if item already exists as key in dictionary
        print("Duplicate item (using dict): ", item) # second time seeing it = duplicate
        break 
    char_count[item] = 1  # first time seeing it, add as key with value 1

print(" --------------About set()----------------------")
seen = set()        # empty set, stores only unique values
seen.add("apple")   # → {"apple"}
seen.add("banana")  # → {"apple", "banana"}
seen.add("apple")   # → {"apple", "banana"} duplicate ignored, set never stores duplicates!
print(seen)
# we use this behaviour to detect duplicates:
# if item not in seen → first time seeing it → add to seen
# if item in seen → already visited → its a duplicate! ✅
# Note: set uses add() not append() like lists!


# print ("---------------ABOUT DICTIONARY----------------------")
# How it works with ["apple", "banana", "apple"]:
# char_count = {}
# item = "apple"  → not in dict → add → char_count = {"apple": 1}
# item = "banana" → not in dict → add → char_count = {"apple": 1, "banana": 1}
# item = "apple"  → already in dict! ✅ → print "apple" → break
# Basically dictionary works same as set here, but instead of just storing the item, it stores item with a value 1. We don't even use that value, just checking if key exists! 

# -------------------ABOUT .COUNT()--------------------
# count method - scans whole list for each item
# Enter items separated by comma: 1,2,3,12,3,2   

# Duplicate item (using count):  2
# Duplicate item (using set):  3
# Duplicate item (using dict):  3

# count → scans whole string every time → finds 2 first because it scans full list for each item
# set/dict → tracks as it goes → finds 3 first because it catches duplicate as soon as it sees it second time