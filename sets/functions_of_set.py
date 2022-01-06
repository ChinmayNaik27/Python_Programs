#Functions Of Set
set1={1,2,3,4,5,6,7,8,9}
set2={3,4,5,6,8,9}
set3={11,12,13}
#isdisjoint()
print(set1.isdisjoint(set2))
print(set1.isdisjoint(set3))
#issubset()
print(set1.issubset(set2))
print(set2.issubset(set1))
#issuperset()
print(set1.issuperset(set2))
print(set2.issuperset(set1))