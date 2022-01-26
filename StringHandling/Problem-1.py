"""Bob has found two very old sheets of paper, each of which originally contained a string of lowercase Latin letters.
The strings on both the sheets have equal lengths.
However, since the sheets are very old, some letters have become unreadable.
Bob  would like to estimate the difference between these strings.
Let's assume that the first string is named S1, and the second S2.
The unreadable symbols are specified with the question mark symbol '?'.
The difference between the strings equals to the number of positions i, such that S1i is not equal to S2i,
where S1i and S2i denote the symbol at the i the position in S1 and S2, respectively.
BOb would like to know the minimal and the maximal difference between the two strings,
if he changes all unreadable symbols to lowercase  letters.
Input:

a?c
??b
Output:
1 3   """
s1='aac'
s2='aab'

for i in range(len(s1)):
    x1=0
    for j in range(len(s2)):
        if s1[i]==s2[j]:
            break
        elif i!=j:
            x1+=1

print(x1)