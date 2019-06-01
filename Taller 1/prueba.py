from MarcoDeCognicion import MarcoDeCognicion
import matplotlib.pyplot as plt

mc = MarcoDeCognicion(vertices=[10, 20, 40, 60], etiquetas=['Niño', 'Joven', 'Adulto'])



gp = mc.grado_de_pertenencia(15)

x_range = range(0, 70)
y1 = []
y2 = []
y3 = []

for x in x_range:
    gpx = mc.grado_de_pertenencia(x)
    y1.append(gpx['Niño'])
    y2.append(gpx['Joven'])
    y3.append(gpx['Adulto'])
    
plt.plot(x_range, y1)
plt.plot(x_range, y2)
plt.plot(x_range, y3)
plt.grid(True)
plt.show()