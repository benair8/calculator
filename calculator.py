import numbers 


def add(a,b):
   return a+b

def subtract(a,b):
   return a-b

def multiply(a,b):
    return a*b

def divide(a,b):
    if b==0:
        raise ValueError("Cannot divide by zero")
    return a/b

def power(a,b):
    return a**b

while True:
 try:
   num1 = float(input("Enter first number: "))
   num2 = float(input("Enter second number: "))
 except ValueError:
   print ("Invalid input! Please enter numbers only.\n")
   continue
  
 print ('Select operation:')
 print ('1. Add') 
 print ('2. Subtract') 
 print ('3. Multiply')
 print ('4. Divide')
 print ('5. Power ')

 if not isinstance(num1, numbers.Number) or not isinstance(num2, numbers.Number):
    print("Please enter a valid number.")
 else: 
    choice = input("enter choice(1/2/3/4):")
    if choice == "1":
       print(f"{num1} + {num2} ={add(num1,num2)}")
    elif choice == "2":
         print(f"{num1} - {num2} ={subtract(num1,num2)}")
    elif choice == "3":     
        print(f"{num1} * {num2} ={multiply(num1,num2)}")
    elif choice == "4": 
        print(f"{num1} / {num2} ={divide(num1,num2)}")
    elif choice == "5":
        print(f"{num1}^{num2} ={power(num1,num2)}")
    else:
        print("Invalid input")   
 while True:
    restart = input("Still want to calculate? (y/n):").strip().lower()
    if restart == 'y':
        break
    elif restart == 'n':
     print("Goodbye!!")
     exit()
    else:
     print("Invalid input! Please enter 'y' or 'n'.")
        









