# x = float(input ("what's x? "))
# y = float(input ("what's y? "))

# # Addition
# #z = round(x + y)
# #print(f"{z:,}")

# # Division
# #z = round(x / y , 2)
# #print(z)
# z = x / y
# print(f"{z:.2f}")

def division():
   x = float(input("Enter the first number: "))
   y = float(input("Enter the second number: "))
   z = x / y
   print(f"The result of {x} divided by {y} is {z:.2f}")
   
division()

def exponent():
   X = int(input("Enter a number "))
   print(f"{X} raised to the power of 2 is", square(X))
   
def square(n):
   return n ** 2   
    
exponent()   