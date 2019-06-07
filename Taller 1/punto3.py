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

esp_vida_real_CO = data[data['País'] == 'Colombia']['Esperanza de vida (mujeres)'].mean()


try:
    etiqueta_linguistica = input('Seleccione la etiqueta lingüística:\n1: Esperanza de vida baja\n2: Esperanza de vida media\n3: Esperanza de vida alta.\n')
    if int(etiqueta_linguistica) not in [1, 2, 3]:
        raise ValueError('La opción seleccionada no es correcta.')
except ValueError as ve:
    print(ve)
    exit()

try:
    grado_pert_estimado = float(input('Ingrese el grado de pertenencia estimado:\n'))
    if 1 < float(grado_pert_estimado) or float(grado_pert_estimado)<0:
        raise ValueError('Debe ingresar un número entre 0 y 1.')
except ValueError as ve:
    print(ve)
    exit()
except TypeError:
    print('Debe ingresar un número.')

try:
    x_ingresado = float(input('Ingrese un valor de x en años:\n'))
    if float(x_ingresado)<0:
        raise ValueError('El valor no pertenece al Universo del discurso')
except ValueError as ve:
    print(ve)
    exit() 
 

# esp_vida_real = 

# mc_delta = MarcoDeCognicion([0.1, 0.25, 0.4], ['Cierto', 'Poco cierto', 'Falso'])

