import numpy as np
import matplotlib.pyplot as plt

x = np.linspace(-10, 10, 500)
y = np.linspace(-10, 10, 500)
X, Y = np.meshgrid(x, y)

x1, y1 = -2, 0
x2, y2 = 2, 0

r1 = np.sqrt((X - x1)**2 + (Y - y1)**2)
r2 = np.sqrt((X - x2)**2 + (Y - y2)**2)

k = 2 * np.pi / 1  # długość fali = 1

I = np.cos(k * r1) + np.cos(k * r2)

plt.imshow(I, extent=[-10,10,-10,10])
plt.colorbar()
plt.title("Interferencja dwóch źródeł")
plt.show()