a=int(input("Enter a number to check the weather number is divisible by 5 or not:"))
try:
    assert a%5==0
    print("Divisible by 5")
except AssertionError:
    print("Not Divisible by 5")
print("End")