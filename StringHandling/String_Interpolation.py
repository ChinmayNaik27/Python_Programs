"""String interpolation"""
id=10
age=18
name='Chinmay'
#1st way
print("Your Name Is",name+",Your Age Is",str(age)+",Your Id Is",str(id))
#2nd way by string Interpolation
s1=f"Your Name is {name},Your age is {age},Your id is {id}"
print(s1)