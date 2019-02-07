import matplotlib.pyplot as plt 
import pandas as pd 
dataset1={'year':[2016,2017,2018,2019],'emp':[1000,1200,1100,1500],'avgsalaryf':[15500,16500,15700,18500],'avgsalarym':[18050,15000,12500,17750]}
df=pd.DataFrame(dataset1)
print(df)
plt.subplot(2,1,1)
plt.title('Avg salary 2016-2019')
plt.hist(df.avgsalaryf,edgecolor='black')
plt.ylabel('Avg salary F')
plt.subplot(2,1,2)
plt.hist(df.avgsalarym,edgecolor='black')
plt.ylabel('Avg salary M')
plt.show()