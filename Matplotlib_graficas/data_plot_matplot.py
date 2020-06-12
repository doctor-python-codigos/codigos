# Codigo: Doctor Python

import matplotlib.pyplot as plt 
import numpy as np 

n = np.arange(-2 * np.pi , 2 * np.pi, 0.2) # inicio,final,step
x = np.sin(n)
y = np.cos(n)

fig, axs = plt.subplots(2, 2)
fig.suptitle('~ Grafica de Funciones ~ ',color='darkred',size=19)
fig.text(0.41, 0.025, 'Siguenos en instagram @doctor_python', style='italic',
        bbox={'facecolor': 'red', 'alpha': 0.5, 'pad': 10})

axs[0, 0].plot(n, x,'m')
axs[0, 0].legend(['sin(x)'])
axs[0, 0].set_title('Funcion SEN', style='italic', size=9)
axs[0, 0].set(ylabel='Amplitud')	
axs[0, 0].plot(1.60, 1,'o')
axs[0,0].annotate('punto maximo', xy=(1.60, 1), xytext=(-3, 0.5),color='green',
            arrowprops=dict(facecolor='darkblue', shrink=0.05))

axs[0, 1].plot(n, y, 'bs')
axs[0, 1].legend(['cos(x)'])
axs[0, 1].grid(color='r', linestyle='-', linewidth=0.5)
axs[0, 1].set_title('Funcion COS',size=9)

axs[1, 0].plot(n, x, '4', n, y,':')
axs[1, 0].legend(['sin(x)', 'cos(x)'])
axs[1, 0].set_title('Funciones SEN y COS', size=9)

axs[1, 1].plot(n, x,'r--', n, y , 'g^')
axs[1, 1].legend(['sin(x)', 'cos(x)'])
axs[1, 1].set_title('Funciones SEN y COS', size=9)
axs[1, 1].set_facecolor(color='black')
axs[1, 1].grid(color='white', linestyle='-', linewidth=0.5)
plt.show()