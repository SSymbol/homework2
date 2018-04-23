# coding=utf-8
import pandas as pd

obj = pd.read_csv("e:/Building_Permits.csv",low_memory=False)

attr=[]

for item in obj.columns:
    n = obj[item].value_counts()
    if n.count() < 100:
        attr.append(item)
        print(item,n.count())


df = obj[attr]

df.to_csv("e:/test.csv",index=False,header=False)
