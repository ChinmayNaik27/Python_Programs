"""WAP to Print Following Structure
*       *
  *   *
    *
  *   *
*       *
"""

i=0
j =4
for a in range(5):
    for b in range(5):
        if a == i and b == j:
            print("*", end=" ")
            i = i + 1
            j = j - 1
        elif a == b:
            print("*", end=" ")

        else:
            print(" ", end=" ")
    print()