"""Built-in methords -3"""
s1="This is Demo"
print(s1)
#######replace
s1=s1.replace('is','IS')
print(s1)
######isalnum
s2="123abc"
print(s2.isalnum())
#############isalpha
s3="abc"
print(s3.isalpha())
###########isdigit()
s4="123"
print(s4.isdigit())
################islower & isupper
s5="abcd"
print(s5.islower())
print(s5.isupper())
##########center , ljust, rjust
print(s5.center(20,"#"))
print(s5.ljust(50,"%"))
print(s5.rjust(50,"$"))
################strip , lstrip, rstrip
s5="    Hey    "
print(s5)
s5=s5.strip()
print(s5)
s5=s5.lstrip()
print(s5)
s6=" HEY...    "
s6=s6.rstrip()
print(s6)
##################title , encode
s10="This is demo"
print(s10)
s10=s10.title()
print(s10)
s11=s10.encode()
print(s11)