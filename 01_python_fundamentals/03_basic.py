a = input()   # takes input as string e.g. "6"
b = input()   # takes input as string e.g. "4"
c = input()   # takes separator as string e.g. "&"

# Multiply string a, int(a) times → "6" * 6 = "666666"
result_1 = a * int(a)

# Multiply string b, int(b) times → "4" * 4 = "4444"
result_2 = b * int(b)

# Print both results separated by c → 666666&4444
print(result_1, result_2, sep=c)



# =================================================================================================================================

# -----------------MY MISTAKE AND FIX-----------------
# ❌ WRONG - int(a) converts "6" to 6 (integer)
# then 6 * "6" works but is confusing & bad practice
# result_1 = int(a) * a

# ✅ CORRECT - a is already a string, just convert for multiplication
# string * int is the standard readable way in Python
# result_1 = a * int(a)

# ------------Why a * int(a) is better?-----------------------
# pythonint(a) * a   # int * string → reads like math first, then string (confusing)
# a * int(a)   # string * int → clearly says "repeat this string N times" (clean)
# Rule of thumb → always write string * int, it clearly shows your intention that you are repeating a string, not doing math! 🎯