import numpy as np
import matplotlib.pyplot as plt

plt.figure()
plt.subplot(2,1,1)
plt.gca().set_title("Método de Runge-Kutta 4 orden")
data = np.loadtxt("RK4.dat")
plt.plot(data[:,0], data[:,1])
plt.xlabel('t')
plt.ylabel('Y')

plt.subplot(2,1,2)
plt.gca().set_title("Método de Euler")
data = np.loadtxt("euler.dat")
plt.plot(data[:,0], data[:,1])
plt.xlabel('t')
plt.ylabel('Y')
plt.tight_layout()
plt.savefig("rk4.png")