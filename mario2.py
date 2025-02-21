# def main():
#   print_square(3)
  
# def print_square(size):
#   # For each row in square
#   for i in range(size):
    
#     # For each brick in row
#     for j in range(size):
      
#       # Print a brick 
#         print("#", end="")
        
          
#     print()

  
# main()  

# def main():
#   print_square(3)
  
# def print_square(size):
#   # For each row in square
#   for i in range(size):
#     # Print the top and bottom borders
#     print("#" * size)
    
#     # Print the middle bricks
#     for _ in range(size - 2):
#       print("#", end="")
#       print(" " * (size - 2), end="")
#       print("#")
      
# main()

def main():
  print_triangle(4)
  
def print_triangle(size):
  for i in range(size):
    print(" " * (size - 1 - i) + "#" * (2 * i + 1))
    
main()  

print("")    


def main1():
   print_square(4)
   
def print_square(size):
  for i in range(size):
    print_row(size)
    
def print_row(width):
  print("?" * width)
  
main1()         
   