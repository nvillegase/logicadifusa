from MarcoDeCognicion import MarcoDeCognicion
import matplotlib.pyplot as plt
import pandas as pd
import numpy as np

# Cargar base de datos:

data = pd.read_csv('../Indicadores Mundiales_act.csv')

datos_disponibles = data.columns.values.tolist()
print("Datos disponibles: {}".format(datos_disponibles))

# for d in datos_disponibles:
#     print('Para la columna "{}":\n{}\n\n\n'.format(d, data[d].describe()))

'''

    La descripción estadística de cada columna permite tener un criterio para asignar las
    etiquetas lingüísticas para cada categoría en el universo del lenguaje.
    Por ejemplo, para la esperanza de vida en mujeres se encontró:

    count    2568.000000
    mean       71.159268
    std        10.708262
    min        39.000000
    25%        64.000000
    50%        75.000000
    75%        79.000000
    max        87.000000
    Name: Esperanza de vida (mujeres), dtype: float64

    Adicionalmente, es posible que la esperanza de vida en mujeres sea diferente según la
    ubicación geográfica del país que se analice. Por ejemplo, para las mujeres en África,
    se tiene:


'''

regiones = ['África', 'Asia', 'Europa', 'Oriente Medio', 'Oceanía', 'América']
espvida = []

var = 'Esperanza de vida (mujeres)'

for region in regiones:
    esp_muj_afr = data[data['Región'] == region][var]
    espvida.append(esp_muj_afr.mean())
    print('-'*50)
    print('[Región: {}]'.format(region))
    print(esp_muj_afr.describe())
    print('\n')

promedio_mundial = data[var].mean()

objects = (region for region in regiones)
y_pos = np.arange(len(regiones))
plt.bar(y_pos, espvida, align='center', alpha=0.5, label='Esperanza de vida')
plt.xticks(y_pos, objects)
plt.ylabel('Esperanza de vida (años)')
plt.title('Esperanza de vida en mujeres según la región')
plt.plot(y_pos, [promedio_mundial for it in y_pos], 'k:', label='Promedio mundial')
plt.legend(loc=4)
plt.show()

'''

    Inicio de marcos de cognición:

'''

mc = MarcoDeCognicion(vertices=[10, 20, 40, 60], etiquetas=['Niño', 'Joven', 'Adulto'])

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