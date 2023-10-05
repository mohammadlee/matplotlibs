# The lines `import pandas as pd`, `import matplotlib.pyplot as plt`, and `import numpy as np` are
# importing external libraries in Python.
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np




# The code `data_set=pd.read_csv('sample.csv')` is reading the contents of a CSV file named
# 'sample.csv' and storing it in a variable called `data_set`. The `pd.read_csv()` function is a part
# of the pandas library and is used to read CSV files.
data_set=pd.read_csv('sample.csv')
print(data_set)


x=data_set['student']
y=data_set['living_costs']
plt.plot(x,y,color='red')
plt.bar(x,y,color='yellow')
plt.show()