print("Program to find factorial of a user defined number")
def factorial(n):
 '''This is a doc string & not a comment. Unlike a comment which we write to understand the intent and functionality of the program, docstring is
used to document our code. We can access these docstrings using the .__doc__ attribute.
 '''
 if (n==0 or n==1):
  return 1
 else:
  return(n*factorial(n-1))
n=int(input("Enter a Positive Number:"))
print("The Factorial of the given Number is:",factorial(n))
