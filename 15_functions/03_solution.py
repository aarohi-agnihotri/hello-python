def mutliply(first_val, second_val):
    return first_val * second_val

first_val = "p"
second_val = 5
print(f"mutliplication of {first_val} and {second_val} : {mutliply(first_val, second_val)}")

 # ---------Polymorphism----------
# The '*' operator behaves differently based on data type:
#   int * int   → arithmetic multiplication  (3 * 4 = 12)
#   str * int   → string repetition          ("p" * 5 = "ppppp")
# Same operator, different behaviour = POLYMORPHISM
# Polymorphism — the core concept. The * operator is polymorphic, meaning it adapts its behaviour to the types it receives. With two numbers it does arithmetic; with a string and an int it repeats the string. Same function, same operator — different behaviour based on input type.