# Codigo: Doctor Python

from   mpl_toolkits.mplot3d import axes3d
import matplotlib.pyplot as plt 
import random

figura = plt.figure()
ax =plt.axes(projection="3d")
puntos_x = [0] * 10
puntos_y = [0] * 10
puntos_z = [0] * 10
for i in range(10):
	puntos_x[i] = random.randint(0, 10)
	puntos_y[i] = random.randint(0, 10)
	puntos_z[i] = random.randint(0, 10)

ax.scatter(puntos_x, puntos_y, puntos_z,color='darkred',marker='^')
ax.set_xlabel('Eje x', color='r')
ax.set_ylabel('Eje y', color='b')
ax.set_zlabel('Eje z', color='g')
figura.text(0.41, 0.025, 'Siguenos en instagram @doctor_python',
        bbox={'facecolor': 'red', 'alpha': 0.5, 'pad': 10})
plt.show()
