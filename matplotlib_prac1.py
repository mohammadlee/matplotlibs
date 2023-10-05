import matplotlib.pyplot as plt
import numpy as np
plt.style.use('_classic_test_patch')
x=np.linspace(-5,5,10)
FX1=x**2
FX2=x**3
plt.plot(x,FX1, color='#ff2435',linewidth=2.8,marker="*", markersize=6,label='X^2')
plt.plot(x,FX2, color='#AA1268',linewidth=2.5,marker="^", markersize=6,label='X^3')
plt.legend(['x**2','x**3'])
plt.title('first_figure')
plt.xlabel('X')
plt.ylabel('F(X)')
plt.grid()
#plt.savefig('final_image1.pdf')
plt.figure(figsize=(8,8),dpi=200)
plt.show()