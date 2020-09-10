#Exo5.3
import pandas as pd

with open("C:/Users/Admin/Documents/Python M2 SRC Louis ADAM/diamonds.csv","r") as f:
    diamants = f.readlines()

count = 1
diamants_100 = []

while count <= 100:
    diamants_100.append(diamants[count],)
    count = count + 1

#print(diamants_100)
print(diamants_100[:20])