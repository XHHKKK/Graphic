import matplotlib.pyplot as plt

plt.figure()

plt.xlim(-10, 10)
plt.ylim(-10, 10)

plt.xlabel('X')
plt.ylabel('Y')

plt.grid(color = 'gray', linestyle = '--', linewidth = 0.5)

plt.title("Ось координат")
plt.show()

