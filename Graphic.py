import matplotlib.pyplot as plt
import numpy as np

plt.figure()

#Обозначения осей
plt.xlim(-10, 10)
plt.ylim(-10, 10)

plt.axhline(0, color='black',linewidth=0.5, ls='-')  # Горизонтальная ось
plt.axvline(0, color='black',linewidth=0.5, ls='-')  # Вертикальная ось


plt.xlabel('X')
plt.ylabel('Y')


x=np.linspace(-5, 5, 100)
y= x**2/2-2
plt.plot(x,y)
text=plt.text(-3.65, 4.25, '$y=x^2/2-2$', fontsize=10)
plt.title("Ось координат")
plt.show()

