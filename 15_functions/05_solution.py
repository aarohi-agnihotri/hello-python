# HERE, WE USE DEFAULT PARAMETER VALUE
# If no argument is passed while calling the function,
# Python automatically uses "user".

def greeting(name = "user"):
    return name

name = input("Enter your name: ")

# If user enters a value, that value is passed to the function and replaces the default value.
print(f"Good morning!! {greeting(name)}")

# Here, no argument is passed, so default value "user" is used.
print(f"Good morning!! {greeting()}")


# ---------------------------------------------------
# IMPORTANT CONCEPT:
#
# greeting()           -> uses default value "user"
#
# greeting("Aarohi")   -> uses "Aarohi"
#
# greeting("")         -> empty string is STILL a value so default value will NOT be used
#
# Default value works ONLY when argument is NOT passed.
# It does NOT work for empty input.
# ---------------------------------------------------

# ------- for empty input -------
# like user was asked to input name
# but pressed Enter without typing anything 
def greeting2(name): 
    return "user" if "none" else name 
    
name2 = input("Enter your name: ")
print(f"Good morning!! {greeting2(name2)}")