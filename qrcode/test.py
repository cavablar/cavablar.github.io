import pandas as pd

adlar=[]
qiymetler=[]

while True:
    ad=input("Ad:")
    qiymet=int(input("Qiymet:"))
    adlar.append(ad)
    qiymetler.append(qiymet)
    print("Items Add Succesfuly")
    a=input("")
    if a!="":
        break


d= {"Ad":adlar, "Qiymet":qiymetler}
data=pd.DataFrame(data=d)
check=lambda x:{x["Ad"][count]:"5" if x["Qiymet"][count]>=80 else ('4' if x["Qiymet"][count]>=60 else ("3" if x["Qiymet"][count]>=30 else '2'))}
count=0
for i in range(4):
    print(check(data))
    count+=1



