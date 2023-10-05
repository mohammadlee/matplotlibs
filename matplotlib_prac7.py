import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

#data
weeks=[1,2,3,4,5,6,7,8,9,10]

mohammad=[15,85,40,24,40,16,25,34,50,65]
alice=[25,70,20,26,23,50,60,63,20,25]
michel=[20,24,150,100,40,60,20,20,65,54]

#label
labels=['mohammad','alice','michel']
#colors
colors=['#302','#940','#245']
#plot
plt.style.use('ggplot')
plt.stackplot(weeks,alice,michel,mohammad,labels=labels,colors=colors)
plt.legend()
plt.savefig('final_fig_section7.png')
plt.show()
