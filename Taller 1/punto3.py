from MarcoDeCognicion import MarcoDeCognicion
import matplotlib.pyplot as plt
import pandas as pd
import numpy as np

# Cargar base de datos:

data = pd.read_csv('../Indicadores Mundiales_act.csv')
# datos_disponibles = data.columns.values.tolist()
# print("Datos disponibles: {}".format(datos_disponibles))
# print(data)

espvida = []
espvida_std = [] #Desviación estandar para definir limites de las etiquetas lingüisticas

esp_vida = data[data['Región'] == 'América']['Esperanza de vida (mujeres)']
espvida.append(esp_vida.mean())
espvida_std.append(esp_vida.std())

vertices_p3 = []

vertices_p3.append(int(espvida[0] - 4*espvida_std[0]))
vertices_p3.append(int(espvida[0] - 2*espvida_std[0]))
vertices_p3.append(int(espvida[0] + 2*espvida_std[0]))
vertices_p3.append(int(espvida[0] + 4*espvida_std[0]))

etiqueta_linguistica_str = ['Baja', 'Media', 'Alta']

mc_esperanza_vida = MarcoDeCognicion(vertices_p3, etiqueta_linguistica_str)

# Extraer de la base de datos la expectativa de vida de las mujeres en Colombia:
esp_vida_real_CO = data[data['País'] == 'Colombia']['Esperanza de vida (mujeres)'].mean()

try:
    etiqueta_linguistica = int(input('Seleccione la etiqueta lingüística:\n1: Esperanza de vida baja\n2: Esperanza de vida media\n3: Esperanza de vida alta.\n')) - 1
    if etiqueta_linguistica not in [0, 1, 2]:
        raise ValueError('La opción seleccionada no es correcta.')
except ValueError as ve:
    print(ve)
    exit()

try:
    grado_pert_estimado = float(input('Ingrese el grado de pertenencia estimado:\n'))
    if not (0 <= grado_pert_estimado <=
     1):
        raise ValueError('Debe ingresar un número entre 0 y 1.')
except ValueError as ve:
    print(ve)
    exit()

grado_pert_real = mc_esperanza_vida.grado_de_pertenencia(esp_vida_real_CO)
grado_pert_real = grado_pert_real[etiqueta_linguistica_str[etiqueta_linguistica]]
delta_gp = abs(grado_pert_estimado - grado_pert_real)

mc_delta = MarcoDeCognicion([0.1, 0.2, 0.35, 0.45], ['Cierto', 'Poco cierto', 'Falso'])
grado_verdad = mc_delta.grado_de_pertenencia(delta_gp)

#esp_vida_real = 
max_gv = 0
veredicto = ''

for g in grado_verdad:
    if grado_verdad[g] > max_gv:
        max_gv = grado_verdad[g]
        veredicto = g

print(
    '\n\nResultado:\n\nEsperanza de vida promedio en América: {} años\n'.format(int(esp_vida.mean())) + \
    'Esperanza de vida promedio en Colombia: {} años\n'.format(int(esp_vida_real_CO)) + \
    'Grado de pertenencia al conjunto con esperanza de vida {}: {}\n'.format(etiqueta_linguistica_str[etiqueta_linguistica], grado_pert_real) + \
    'Al evaluar el grado de la afirmación "Las mujeres en Colombia tienen un grado de pertenencia de {}'.format(grado_pert_estimado) + \
    ' al conjunto de las mujeres con esperanza de vida {}"\n'.format(etiqueta_linguistica_str[etiqueta_linguistica]) + \
    'Se determina que dicha afirmación es {}.'.format(veredicto)
)

