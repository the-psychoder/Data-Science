import matplotlib.pyplot as plt 
import pandas as pd 
data=pd.read_csv('countries.csv')
us=data[data.country=='United States'] #get all US data
china=data[data.country=='China'] #get all China data
us_growth=us.population/us.population.iloc[0]*100 #making intial population 100 and calculating growth
china_growth=china.population/china.population.iloc[0]*100
plt.plot(us.year,us_growth)
plt.plot(china.year,china_growth)
plt.legend(['United States','China'])
plt.xlabel('year')
plt.ylabel('population growth')
plt.title('population growth in U.S. and China')
plt.show()

