import pandas as pd
import matplotlib.pyplot as plt
import numpy as np


#family_number_slice
slice=[7,1,4,9,2.5,0.9]
slice.sort()
#faimly_name_labels
labels=['Adames','charlies','watson','farhadi','changeh','oliver']

#color
colors=['#aabbcc','#452648','#ccadaa','#fffcad','#abbcfa','#ddcbdf']

#exploed
exploeds=[0,0,0,0.1,0,0]

plt.pie(slice,labels=labels,colors=colors,wedgeprops={'edgecolor':'#000'},explode=exploeds,shadow=True,autopct='%1.1f')
plt.savefig('final_fig_section6.png')
plt.show()
 