"""Write a Python program to get the Fibonacci series between 0 to 50.
Note : The Fibonacci Sequence is the series of numbers :
0, 1, 1, 2, 3, 5, 8, 13, 21, ...."""
n1 = 0                        #assign n1 to 0
n2 = 1                         #assign n2 to 1
i = 0                         #intitialize i to 1
print("Fibonacci sequence:")
while i < 51:
       print(n1)
       fb = n1 + n2
       n1 = n2          # update values n2 values to n1
       n2 = fb          # update values fb to n2
       i += 1
