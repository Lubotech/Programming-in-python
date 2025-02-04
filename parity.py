# x = int(input("Enter a number: "))

# if x % 2 == 0:
#   print(f"{x} is an even number")
# else:
#   print(f"{x} is an odd number")

def main():
  x = int(input("Enter a number: "))
  if is_even(x):
    print(f"{x} is an even number")
  else:
    print(f"{x} is an odd number")
    
# def is_even(n):
#   if n % 2 == 0:
#     return True
#   else:
#     return False
  
def is_even(n):
  return n % 2 == 0
  
main()
        