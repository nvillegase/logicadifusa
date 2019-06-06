from MarcoDeCognicion import MarcoDeCognicion
import matplotlib.pyplot as plt
import numpy as np

mc = MarcoDeCognicion(vertices=[10, 20, 40, 60], etiquetas=['Niño', 'Joven', 'Adulto'])



gp = mc.grado_de_pertenencia(15)

x_range = range(0, 30)
y1 = []
y2 = []
y3 = []

for x in x_range:
    gpx = mc.grado_de_pertenencia(x)
    y1.append(gpx['Niño'])
    y2.append(gpx['Joven'])
    y3.append(gpx['Adulto'])

y1 = np.array(y1)
y2 = np.array(y2)
y3 = np.array(y3)

plt.subplot(121)
plt.plot(x_range, y1,'r', label='µA(x)')
plt.plot(x_range, y2,'b', label='µB(x)')
plt.legend(bbox_to_anchor=(0., 1.02, 1., .102), loc=3,ncol=2, mode="expand", borderaxespad=0.)
#plt.plot(x_range, y3)
plt.grid(True)

plt.subplot(122)
plt.plot(x_range, y1+y2, 'm', label=' µA(x) + µB(x) ')
plt.legend(bbox_to_anchor=(0., 1.02, 1., .102), loc=3,ncol=1, mode="expand", borderaxespad=0.)
plt.ylim((0, 1.05))
plt.grid(True)

plt.show()