def func(**kwargs):
    for key, val in kwargs.items():
        print(f"{key} : {val}")

func(fruit = "mango", vegetable = "capsicum")
func(color = "white", thing = "flower", social_media = "pinterest")

# here we can change name kwarags to args, but again same words = not recommend
# for key value pairs,  we use two asterisk - that's matters most

# -------formatted string (string arranged in a clean, readable structure using variables or values)--------------
# common ways to create formatted strings - f-atring, using +, format()
# def introduce(**kwargs):
#     details = []   # [] creates an empty list, this will store formatted string
#     for key, value in kwargs.items():
#         details.append(key + ": " + str(value))   # building formatted string using +, str() converts int to string, append() - add item in the end of list
#     return ", ".join(details)    # join() to combine all list items into one string, ", " is separator

# print(introduce(Name = "Alice", Age = 25, City = "New York"))


# --------using both args and kwargs------
# def student_info(*args, **kwargs):
#     print("Subjects:", *args) #tuple
#     print("Details:", kwargs) #dictonary
#     # print("Details:", *kwargs) #prints only dictonary keys, if use **kwargs -> throw error

# student_info("OS", "DBMS", Name = "Aarohi", Age = "22")