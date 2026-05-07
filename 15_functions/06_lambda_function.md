# Lambda Function

## Syntax
```
variable = lambda parameter : expression
```
no `def`, no `return` — expression after `:` is returned automatically.

## Anonymous?
lambda has no built-in name unlike `def`. assigning to `cube` is just a variable pointing to it.
true anonymous use — no variable at all:
```python
sorted(items, key=lambda x: x[1])
```

## Expression vs Statement
**Statement** = does something, no value returned
**Expression** = produces a value

```python
# statements — can't be assigned
if x > 0: ...       # decides what to do
for i in range(5):  # loops
x = 5               # assigns

# expressions — give back a value, can be assigned
2 + 3                            # gives 5
"even" if x % 2 == 0 else "odd" # gives a string
cube(3)                          # gives 27
```

quick test:
- `result = ___` works → expression ✅
- `result = ___` crashes (SyntaxError) → statement ❌

| allowed in lambda | not allowed in lambda |
|---|---|
| `lambda x: "even" if x%2==0 else "odd"` | `lambda x: if x>0: ...` |
| `lambda x: [i for i in x]` | `lambda x: for i in x: ...` |

lambda only allows expressions — because it needs something it can return as a value.

## Point is about **intent and best practice**, not technical limitation.

```python
# you CAN store lambda in another variable — but it's just a reference
another_cube = cube2        # both point to the same lambda
another_cube(3)             # works, gives 27

# BUT this goes against lambda's purpose
# lambda  → one-time, on-the-go use (pass directly, no reuse planned)
# def     → reusable, modular, can be redefined and extended

# best practice:
# ✅ lambda → short, throwaway logic
sorted(items, key=lambda x: x[1])

# ✅ def → logic you'll reuse multiple times
def cube(number):
    return number ** 3
```

so technically both work — but **if you're storing and reusing, just use `def`.**