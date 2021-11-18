"""program to convert length which is in m to inch , feet and cm """
l=float(input("Enter Length in meters:"))  #take input form user in float format
cm=100*l                                   # multiply given length with 100 to convert length to cm (1m=100cm)
ft=3.280*l                                  # multiply given length with 3.280 to convert to feets  (1ft=3.280m)
inch=39.970*l                               # multiply given length with 3.970 to convert to inches (1inch=39.970m)
print("Given length in m is :\t",l)
print("The values in \nINCH: \n",inch,"\nFT: \n",ft,"\nCM: \n",cm)