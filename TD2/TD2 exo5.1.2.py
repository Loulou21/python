#Exo5
import pandas as pd

with open("C:/Users/Admin/Documents/Python M2 SRC Louis ADAM/diamonds.csv","r") as f:
    diamants = f.readlines()

count = 0

while count != len(diamants):
    #print(count)
    print(diamants[count].split(","))
    count = count + 1
