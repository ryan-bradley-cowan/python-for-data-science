# Import libraries
import numpy as np
import matplotlib.pyplot as plt

# Create data
x = np.arange(0, 100)
y = x*2
z = x**2


# Create a figure object called fig
fig = plt.figure()
ax = fig.add_axes([0.15, 0.1, 0.8, 0.8])
ax.plot(x, y)
ax.set_xlabel('x')
ax.set_ylabel('y')
ax.set_title('title')
# plt.show()

# Create a figure object and put 2 axis on it, x y
fig = plt.figure()
ax1 = fig.add_axes([0, 0, 1, 1])
ax2 = fig.add_axes([0.2, 0.5, 0.2, 0.2])
ax1.plot(x, y)
ax2.plot(x, y)
# plt.show()

# Create a figure object and put 2 axis on it, x y z
fig = plt.figure()
ax1 = fig.add_axes([0, 0, 1, 1])
ax2 = fig.add_axes([0.2, 0.5, 0.2, 0.2])
ax1.plot(x, z)
ax2.plot(x, y)
ax2.set_title('zoom')
ax2.set_xlabel('x')
ax2.set_ylabel('y')
ax2.set_xlim(20, 22)
ax2.set_ylim(30, 50)
# plt.show()

# Subplots
fig, axes = plt.subplots(nrows=1, ncols=2)
axes[0].plot(x, y)
axes[1].plot(x, z)
plt.show()