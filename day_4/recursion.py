print("Function for Factorial of a given Number")
n=int(input("Enter a Number to find its Factorial:"))
def factorial(n):
 '''This is a docstring. The difference between a docstring and a comment is that, comment are decsription that help programmers better understand
    the intent and functionality of the program and Docstring are the strings used right after the definition of a function, method, class, or module,
    They are used to document our code.
 '''
 if (n==0 or n==1):
  return 1
 else:
  return (n*factorial(n-1))

print("The Factorial of the given number is:",factorial(n))
