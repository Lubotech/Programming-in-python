# i = 4
# while i != 0:
#   print("I am a winner!")
#   i -= 1

# i = 0
# while i < 4:
#   print("I am a winner!")
#   i += 1

# for _ in range (3):
#   print("God is Great!\n")
  
# print("I am a winner!\n" *3, end="")

# while True:
#   n = int(input("What is n?"))
#   if n > 0:
#     break
  
# for _ in range(n):
#   print("I am a winner!")


def main():
  number = get_number()
  lets(number)

def get_number():
  while True: 
    n = int(input("What is n? "))
    if n > 0:
      return n
    
def lets(n):
      for _ in range(n):
        print("I am a winner!")
        
main()        