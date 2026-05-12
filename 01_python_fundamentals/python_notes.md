# 🐍 Python Introduction

> Python is a high-level programming language known for its **simple and readable syntax**.  
> Created in **1991 by Guido van Rossum** to make programming easy to learn and use.

---

## ✨ Key Features

- ✅ Write programs with **fewer lines of code**, improving readability
- ✅ **Automatically detects variable types** at runtime — no explicit declarations needed
- ✅ Used in **web development, data analysis, automation**, and many more fields
- ✅ Supports **object-oriented, functional, and procedural** programming styles
- ✅ **Dynamically typed** with automatic garbage collection

---

## 👋 Hello World Program

```python
# This is a comment. It will not be executed.
print("Hello, World!")
```

**Output:**
```
Hello, World!
```

### How it works:
- `print()` → built-in Python function that displays text on the screen
- `"Hello, World!"` → a **string** (sequence of text), enclosed in single `' '` or double `" "` quotes

---

## 📐 Indentation in Python

In Python, **indentation** defines blocks of code.  
All statements with the same indentation level belong to the **same block**.

> ✅ Convention: use **4 spaces** per indentation level

```python
print("I have no Indentation ")
    print("I have tab Indentation ")   # ❌ This will cause an error!
```

**Output:**
```
ERROR!
Traceback (most recent call last):
  File "<main.py>", line 2
    print("I have tab Indentation ")
IndentationError: unexpected indent
```

### Why the error?
- The first `print` has no indentation → executes correctly
- The second `print` has unexpected indentation → Python expects consistent indentation within the same block → throws `IndentationError`
---
</br>
 
# 💬 Python Comments
 
Comments are lines in the code that are **ignored by the interpreter** during execution.
 
**Why use comments?**
- Enhances readability of the code
- Identifies functionality or structures the code-base
- Helps understand unusual or tricky scenarios — prevents accidental removal or changes
- Temporarily disables specific parts of code while testing or making changes
---
 
## 1️⃣ Single Line Comments
 
Single line comments start with the `#` symbol.
 
```python
# sample comment
name = "geeksforgeeks"
print(name)
```
 
**Output:**
```
geeksforgeeks
```
 
---
 
## 2️⃣ Multi-Line Comments
 
Python does **not** have a built-in multiline comment syntax.  
There are two workarounds:
 
### Method 1 — Multiple `#` symbols
 
Each line is treated as a separate single-line comment.
 
```python
# Python program to demonstrate
# multiline comments
print("Multiline comments")
```
 
### Method 2 — String Literals
 
Python ignores string literals that are **not assigned to a variable**.  
So they can be used as comments.
 
```python
'Single-line comment using string literal'
 
"""
Python program to demonstrate
multiline comments
"""
print("Multiline comments")
```
 
> ⚠️ Note: `""" """` is technically a string, not a true comment — but Python ignores it if not assigned to anything.
 
---

## ❓ Quiz Questions
 
**Q1. What is the difference between a comment and a docstring in Python?**
 
- A) Comments are ignored by the interpreter; docstrings are not.
- B) Comments use #, while docstrings use triple quotes.
- C) Docstrings can be accessed during runtime, but comments cannot.
- D) All of the above. ✅
> **Explanation:** Comments (using `#`) are ignored by the Python interpreter and serve as annotations for developers. Docstrings, enclosed in triple quotes, are string literals used for documentation and can be accessed at runtime using special methods like `help()`.
 
---
 
**Q2. Which of the following represents a multi-line comment in Python?**
 
- A) `/* This is a multi-line comment */`
- B) Triple single quotes (`'''`)
- C) Triple double quotes (`"""`)
- D) Both b and c ✅
> **Explanation:** Python does not have a dedicated multi-line comment syntax. Instead, developers use triple single quotes (`'''`) or triple double quotes (`"""`) to create multi-line comments.
 
---
 
**Q3. How can we use comments to generate documentation in Python?**
 
- A) By writing single-line comments.
- B) By using docstrings (`"""` or `'''`) in functions and classes. ✅
- C) By using `#` before each function definition.
- D) By adding comments at the end of the script.
> **Explanation:** Docstrings are special types of multi-line strings used as documentation for functions, classes, or modules. These strings are enclosed in triple quotes (`"""` or `'''`) and provide a convenient way to describe the purpose and functionality of the code.
 ----- 
 </br>
 

 # ⚖️ Python — Advantages & Disadvantages
 
## ✅ Advantages
 
| # | Advantage | Short Note |
|---|-----------|------------|
| 1 | Third-party modules | Rich ecosystem of libraries for almost any task |
| 2 | Extensive support libraries |  Python boasts extensive support libraries like NumPy for numerical calculations and Pandas for data analytics, making it suitable for scientific and data-related applications. |
| 3 | Open source & large community | Free to use, huge community support |
| 4 | Easy to read, learn & write | Simple syntax, great for beginners |
| 5 | Dynamically typed | No need to declare data types explicitly |
| 6 | OOP + Procedural | Supports multiple programming styles |
| 7 | Portable & interactive | Runs on any OS, supports real-time code testing |
 
---
 
## ❌ Disadvantages
 
| # | Disadvantage | Short Note |
|---|--------------|------------|
| 1 | Slow performance | Interpreted language — slower than C or Java |
| 2 | Global Interpreter Lock (GIL) | The Global Interpreter Lock (GIL) is a mechanism in Python that prevents multiple threads from executing Python code at once. This can limit the parallelism and concurrency of some applications. |
| 3 | High memory consumption | Uses more memory with large data or complex tasks |
| 4 | Dynamically typed (double-edged) | Python is a dynamically typed language, which means that the types of variables can change at runtime. This can make it more difficult to catch errors and can lead to bugs. |
| 5 | Packaging & versioning issues | Many packages can cause version conflicts |
| 6 | Lack of strictness | Flexibility can lead to hard-to-maintain code |
| 7 | Not ideal for all domains | Weak for mobile apps, embedded systems, frontend |
 
