import pandas as pd
import matplotlib.pyplot as plt
import numpy as np



data_set=pd.read_csv('orders.csv',encoding='utf-8')

city=data_set['city_name_fa'].value_counts().to_dict()

citys=list(city.keys())
amout=list(city.values())
plt.figure(figsize=(10,10),dpi=200)
plt.bar(citys,amout)

plt.savefig('final_fig_section4.png')
plt.show()

