input_str = input("Input a string: ")
str_len = len(input_str)

for char in input_str: 
    if input_str.count(char) == 1:   # count() counts how many times char appears, it scans the whole string every time
        print("First non-repeated char is: ", char)     # prints only if it appears exactly once
        break

print("---------Using a dictionary----------- ")
char_count = {}

# Loop 1 - builds a count of every character:
for char in input_str:
    if char in char_count:
        char_count[char] += 1 # seen before → increment count/value
    else:
        char_count[char] = 1 # first time -> add with value 1

# Loop 2 - finds first character with count 1:
for char in input_str:
    if char_count[char] == 1:
        print("First non-repeated char is: ", char)
        break

# With "abacd":
# char = "a" → not in dict → {"a": 1}
# char = "b" → not in dict → {"a": 1, "b": 1}
# char = "a" → already in dict → {"a": 2, "b": 1}
# char = "c" → not in dict → {"a": 2, "b": 1, "c": 1}
# char = "d" → not in dict → {"a": 2, "b": 1, "c": 1, "d": 1}

# Why two loops? - first loop counts everything and second loop finds first non repeated in original order