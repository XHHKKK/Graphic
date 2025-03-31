import matplotlib.pyplot as plt
import numpy as np

plt.figure()

plt.xlim(-10, 10)
plt.ylim(-10, 10)
#Обозначения осей
plt.xlabel('X')
plt.ylabel('Y')
#сетка
plt.grid(color = 'gray', linestyle = '--', linewidth = 0.5)

x=np.linspace(-10, 10, 100)
y=x**2/2-2
plt.plot(x,y)
plt.title("Ось координат")
plt.show()
