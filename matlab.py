import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
data=pd.read_excel("F1.xlsx")
d_data=pd.read_excel("Drivers.xlsx")
print(len(data["Constructor"]))
print(data['Constructor'].value_counts())
my_const=["Ferrari","Williams", "McLaren" , "Mercedes","Lotus","RedBull","Cooper","Brabham" ,"Renault" , "Vanwall", "BRM" ,"Matra" ,"Tyrrell","Benetton","Brawn"]
no_champs=[16,9,8,8,7,5,2,2,2,1,1,1,1,1,1]
col=["Red","Blue","Orange","Black","Green","DarkBlue","Blue","Black","Yellow","Black","Orange","Blue","Green","Orange","Red"]
plt.barh(my_const,no_champs,color=col)
plt.xlabel("Championships")
plt.ylabel("Constructors")
plt.title("Top Constructors in F1")
plt.show()
print(d_data['Driver'].value_counts())
list = d_data["Driver"].tolist()
list_1=[1,5,2,1,3,1,2,2,1,1,3,1,2,3,1,1,1,1,3,1,4,3,1,7,1,1,2,2,1,1,4,7,1,2]
list_2=[]
for var in list:
  if var not in list_2:
    list_2.append(var)
print(list_2)    
print(len(list_2))
list_2.remove('Lewis Hamilton GBR)' )
list_1=[1,5,2,1,3,1,2,2,1,1,3,1,2,3,1,1,1,1,3,1,4,3,1,7,1,1,2,2,1,1,4,7,1,2]

print(len(list_1))
plt.barh(list_2,list_1)
plt.show()
colo=["Darkblue","Black","Black","Darkblue","Grey","Red","Yellow","Red","Red","Blue","Red","Red","Blue","Red","Blue","Red","Red","Orange","Blue","Blue","Red","Blue","Red","Red","Orange","Blue","Red","Blue","Red","Red","Blue","Red","Blue","Red"]
print(len(colo))
colo.reverse()
print(colo)
plt.barh(list_2,list_1,color=colo)
plt.show()