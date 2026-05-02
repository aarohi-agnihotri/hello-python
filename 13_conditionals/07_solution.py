order_size = input("Enter cup size (small, medium or large): ").lower()

if order_size not in ("small", "medium", "large"):
    print("Please enter right order size!!")
    exit()

extra_shot = input("Do you want extra shot of espresso (yes/no): ")
if extra_shot in ("yes", "y"):
    coffee = order_size.capitalize() + " coffee with an extra shot"
else:
    coffee = order_size.capitalize() + " coffee"

print("Order:", coffee)

