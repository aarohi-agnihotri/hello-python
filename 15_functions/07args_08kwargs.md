# *args and **kwargs

the problem *args solves
if you don't know how many inputs a function will receive, first thought is — just pass a list. find its length, loop through it:

```python
# works, but not ideal
def fun(nums):
    length = len(nums)          # find length
    for i in range(length):     # loop by index
        print(nums[i])
    
    # more better -
    # for i in nums:
    #     print(i)

fun([5, 10, 15])                # user has to manually wrap in []
```

this is logically sound but Python has a cleaner, more idiomatic way for this exact problem — `*args`. same result, less effort.

## What and Why
when defining a function, normally you fix how many parameters it takes. but what if you don't know in advance how many values will be passed? that's where `*args` and `**kwargs` come in — they let a function accept any number of arguments.

---

## *args — Non-Keyword Arguments
collects any number of **positional arguments** into a **tuple**.
positional means order matters — values are assigned by position, not by name.

```python
def fun(*args):
    return sum(args)

print(fun(5, 10, 15))   # 30
```

loop through them:
```python
def myFun(*args):
    for arg in args:
        print(arg)

myFun('Hello', 'Welcome', 'to', 'GeeksforGeeks')
```

use case — multiply any number of values:
```python
def multiply(*args):
    result = 1
    for num in args:
        result *= num
    return result

print(multiply(2, 3, 4))   # 24
```

---

**printing args vs \*args**
```python
def fun(*args):
    print(args)    # ('Hello', 'World') — prints as tuple
    print(*args)   # Hello World — unpacks, prints normally
```

---

**name `args` is just a convention**
the `*` is what matters, not the word `args`. you can name it anything, but not consider good practice and not recommend:
```python
def fun(*chai):
    print(chai)   # works exactly the same
```
---

## **kwargs — Keyword Arguments
collects any number of **keyword arguments** (key=value pairs) into a **dictionary**.
keyword means you pass values by name, so order doesn't matter.

```python
def fun(**kwargs):
    for k, val in kwargs.items():
        print(k, "=", val)

fun(s1='Python', s2='is', s3='Awesome')
```

use case — build formatted string:
```python
def introduce(**kwargs):
    details = []
    for k, v in kwargs.items():
        details.append(k + ": " + str(v))
    return ", ".join(details)

print(introduce(Name="Alice", Age=25, City="New York"))
# Name: Alice, Age: 25, City: New York
```

---

## Using both together
`*args` must always come before `**kwargs` in the function definition.

```python
def student_info(*args, **kwargs):
    print("Subjects:", args)    # tuple
    print("Details:", kwargs)   # dictionary

student_info("Math", "Science", Name="Alice", Age=20)
```
---
### Difference Between `args` and `kwargs` While Printing

| Code              | Meaning                     | Output                            |
| ----------------- | --------------------------- | --------------------------------- |
| `print(args)`     | Prints whole tuple          | `('OS', 'DBMS')`                  |
| `print(*args)`    | Unpacks tuple values        | `OS DBMS`                         |
| `print(kwargs)`   | Prints whole dictionary     | `{'Name': 'Aarohi', 'Age': '22'}` |
| `print(*kwargs)`  | Prints only dictionary keys | `Name Age`                        |
| `print(**kwargs)` | Passes as keyword arguments | Error ❌                           |

---

## Quick comparison

| | *args | **kwargs |
|---|---|---|
| type | positional | keyword (key=value) |
| stored as | tuple | dictionary |
| order matters | yes | no |
| use when | unknown number of values | unknown number of named values |

