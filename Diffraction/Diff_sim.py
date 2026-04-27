import numpy as np
import matplotlib.pyplot as plt

x = np.linspace(-10, 10, 600)
y = np.linspace(-10, 10, 600)
X, Y = np.meshgrid(x, y)

wavelength = 1.0
a = 1.0
k = 2 * np.pi / wavelength

eps = 1e-9

# kąt ~ X
theta = X / 10  

beta = (np.pi * a * theta) / wavelength

I = (np.sin(beta + eps) / (beta + eps))**2

plt.imshow(I, extent=[-10,10,-10,10])
plt.colorbar()
plt.title("Dyfrakcja na pojedynczej szczelinie")
plt.xlabel("x")
plt.ylabel("y")
plt.show()