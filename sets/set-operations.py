#operations in set
set1={1,2,3,4,5,6,7}
set2={3,4,5,6,8,9}
#union
a=set1.union(set2)
print("union of set is:",a)
print("=====================================")
#intersection
a=set1.intersection(set2)
print("Intersection of set is:",a)
#difference
a=set1.difference(set2)
print("Difference:",a)
#symetric Diffrence
a=set1.symmetric_difference(set2)
print("Symmetric Difference:",a)
