import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
from arabic_reshaper import reshape
from bidi.algorithm import get_display
import matplotlib



data_set=pd.read_csv('orders.csv',encoding='utf-8')

city=data_set['city_name_fa'].value_counts().to_dict()

cities=list(city.keys())[:50]
amout=list(city.values())[:50]

cities.reverse()
amout.reverse()


persian_label=[get_display(reshape(lable)) for lable in cities]

matplotlib.rc('xtick',labelsize=3)
matplotlib.rc('ytick',labelsize=3)
matplotlib.rc('font',family='B Nazanin')


plt.style.use('ggplot')
# plt.figure(figsize=(10,10),dpi=200)
plt.barh(persian_label,amout)

# plt.savefig('final_fig_section5_4.png')

plt.show()

