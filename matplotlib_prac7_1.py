import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

#data
years=[2013,2014,2015,2016,2017,2018,2019,2020,2021]

coin_1=np.array([6.5,25.7,6.47,15.49,237.47,65.33,130.45,539.04,631.98]) /1000
coin_2=np.array([5.69,114.54,65.87,14.58,73.17,98.65,1450,1254,1660]) /1000
coin_3=np.array([1.96,9.87,230.63,210.799,1245,1252,1425,1420,1980]) /1000

#color
colors=['#214','#562','#982']
#label
labels=['coin_1','coin_2','coin_3']
#plot
plt.style.use('seaborn')
plt.stackplot(years,coin_1,coin_2,coin_3,labels=labels,colors=colors,alpha=0.7)

# plt.legend(loc='upper left')
plt.legend(loc=(0.1,0.8))
plt.ylabel('Price in billion $')
plt.xlabel('Years(dec/2013-dec/2021)')
plt.title('criptocurrencies market time coinprice[2013-2021]')
plt.savefig('final_fig_section8.png')
plt.show()