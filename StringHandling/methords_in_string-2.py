"""Built in methords"""
s1="This is String1"
########find
x=s1.find('is')
print(x)
x=s1.find('is',x+1)
print(x)
x=s1.find('is',7)
print(x)
#############index
x=s1.index('is')
print(x)
# x=s1.index('is',7)                    #this gives Expection
# print(x)
#rfind
x=s1.rfind('is',7)
print(x)
#rindex
x=s1.index('is')
print(x)
############################################################################
s2="  This is String 2 "
s3="""  This is  String1
  this is  string 2"""
#######split
aw=s2.split(" ")
print(aw)
#######join
s2="".join(aw)
print(s2)
###########splitLines
a=s3.splitlines()
print(a)
########strip
print(s3.strip())
print(s3)