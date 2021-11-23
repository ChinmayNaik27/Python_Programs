"""WAP TO PRINT THE GIVEN OUTPUT:
A B C D
A B C
A B
A
"""
for i in range(65,69):
    a = 65                                                 #assigning a = 65
    for j in range(i,69):
        print("",chr(a),end="")                                #convering ACII to Letter
        a += 1                                                #increment a by 1
    print("")