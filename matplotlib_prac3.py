# The lines `import matplotlib.pyplot as plt` and `import numpy as np` are importing two Python
# libraries, `matplotlib.pyplot` and `numpy`, respectively.
import matplotlib.pyplot as plt
import numpy as np
import random as ran

plt.figure(figsize=(10,10))
my_width=0.26
# `age_x` is a list that contains the ages of the developers. Each element in the list represents the
# age of a developer.
age_x=[18,19,20,21,22,23,24,25,26,27,28,29,30,31,32,33,34,35,36,37,38,39,40,41,42,43,44,45,46,47,48,49,50,51,52,53,54]

x=np.arange(len(age_x))
# `py_dev_y` is a list that contains the salaries of Python developers at different ages. Each element
# in the list represents the salary of a Python developer at a specific age.
py_dev_y=[48339, 48670, 48984, 49407, 49559, 51162, 51382, 52122, 53150, 53766, 54903, 54941, 55397, 55471, 56125, 56605, 56991, 57124, 57681, 57913, 59473, 61559, 63953, 64048, 66222, 66258, 66391, 67224, 67297, 67371, 68665, 69293, 70460, 76963, 77503, 78423, 79327]

# `js_dev_y` is a list that contains the salaries of JavaScript developers at different ages. Each
# element in the list represents the salary of a JavaScript developer at a specific age.
js_dev_y=[45907, 49574, 50859, 51055, 51826, 53107, 54883, 55278, 55347, 55384, 56897, 56949, 57580, 57607, 59909, 60384, 61267, 61367, 62122, 62662, 63541, 63776, 63798, 65734, 66340, 67180, 67937, 69372, 70794, 71888, 73697, 73799, 74590, 74935, 77008, 77047, 78306]

# `dev_y` is a list that contains the salaries of developers at different ages. Each element in the
# list represents the salary of a developer at a specific age. The initial values in `dev_y` are the
# salaries of Python developers (`py_dev_y`) and JavaScript developers (`js_dev_y`) at different ages.
# The loop at the end of the code randomly generates additional salaries for developers and appends
# them to the `dev_y` list.
dev_y=[45374, 46596, 47905, 48512, 48565, 50223, 50688, 51455, 52434, 53896, 55624, 57019, 57823, 59791, 60575, 60702, 60997, 62221, 62535, 62742, 62788, 64566, 64962, 66196, 66552, 66752, 67906, 68430, 68876, 70046, 70185, 70786, 71394, 71894, 71962, 73460, 75441]
plt.style.use('ggplot')
# plt.plot(age_x,py_dev_y, label='python',linewidth=2)
plt.bar(x+my_width,py_dev_y, label='python',width=my_width,color='red')
# plt.plot(age_x,js_dev_y, label='java',linewidth=2)
plt.bar(x,js_dev_y, label='java',width=my_width,color='green')
# plt.plot(age_x,dev_y, label='other',linewidth=2)
plt.bar(x-my_width,dev_y, label='other',width=my_width,color='blue')
#plt.grid()
plt.xticks(ticks=x,labels=age_x)
plt.yticks(np.arange(0,85000,5000))
plt.legend()

# plt.savefig('final_fig_section3.png')
plt.show()
