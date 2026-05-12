a = input()
b = input()

separator = input()[0]
# This reads a line of input and takes only the first character. [0] is just index 0
# Why use [0]?
# Because the problem wants only the separator character, not the whole input line. It's a safety measure — even if the user types extra text, it grabs just the first character.

# Print with space
print(a, b)

# Print without newline at the end
print(a, b, end ="")

# Print with separator
# print(a, b, sep = "&") # before (hardcoded)
print(a,b, sep = separator)

# Print without space
print(a,b, sep = "")

# sep="" → controls what goes between values (default is " ")
# end="" → controls what goes after everything (default is "\n")