import re
str='rat bat cat cartoon crane cro rus rod cra ronaldo rever rot rum ror'
obj=re.search(r'r\w\w',str)
print(obj)
if obj:
    print(obj.group())
else:
    print("Not present")
ob1=re.findall(r'c[ar]\w',str)
print(ob1)
ob=re.match(r'r\w\w',str)
if ob:
    print(ob.group())
else:
    print("Not macthed!!")
obj2=re.search(r'c\w\w',str)
if obj2:
    print(obj2.group())
else:
    print("Not macthed!!")

str='gopi 21 1-5-2022 Vijay 34 22-11-2023 raju 34 23-12-3033'
a1=re.findall(r'\d{1,2}-\d{1,2}-\d{4}',str)
print(a1)
a2=re.findall(r'\D+',str)
print(a2)
for i in a2:
    a2.remove('-')
    print(i,end='')
print(a2)
a3=re.split(r'\+',str)
a3.pop(0)
print(a3)
str1='Kumbhmela is to be held in ahemadabad , book tickets for ahemadabad now!!!'
sw=re.sub('ahemadabad','Nashik',str1)
print(sw)

import urllib.request as r
import re
f=r.urlopen('file:///F:/new1.html')
data=f.read()
print(data)
data=data.decode()
print(data)
ad=re.findall(r'<td>\d</td> <td>\w+</td> <td>\d{2}.\d{2}</td>',data)
print(ad)
ad1=re.findall(r'<td>(\d)</td> <td>(\D+)</td> <td>(\d{2}.\d{2})</td>',data)
print(ad1)
for i in ad1:
    print(i[0],i[1],i[2])

sr1='aaaaaaaaaaaaaaaaccccccccccccccccccccccccccchinmasgduydddddddasvdbjasbduagdiakdjaodhlasdsssssssssssssssssds'

nod=re.sub(r'([a-z])\1+',r'\1',sr1)
print(nod)
import urllib.request
import re
n=urllib.request.urlopen('https://parivahan.gov.in/parivahan/')
new2=n.read()
new2=new2.decode()
print(new2)
q1=re.findall(r'<span class="(\D+)"><a href="(\D+)</a></span>',str)
print(q1)

df=urllib.request.urlopen('https://publicholiday.co.nz/nz-public-holidays-2022.html')
df1=df.read()
df1=df1.decode()
# print(df1)
e1=re.findall(r'<p>(\D+).</p>',df1)
for i in e1:
    print(i)
print(e1)