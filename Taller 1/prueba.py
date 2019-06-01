from MarcoDeCognicion import MarcoDeCognicion

mc = MarcoDeCognicion(vertices=[10, 20, 40, 60], etiquetas=['Niño', 'Joven', 'Adulto'])

gp = mc.grado_de_pertenencia(30)
print(gp)