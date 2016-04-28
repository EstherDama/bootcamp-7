def factorial(n):
   """Function to return the factorial
   of a number using recursion"""
   if n == 1:
       return n
   else:
       return n*factorial(n-1)

print factorial(2)
print factorial(5)