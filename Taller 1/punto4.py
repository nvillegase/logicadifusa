from MarcoDeCognicion import MarcoDeCognicion, ModificadoresLinguisticos
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

gp_bajo = []
gp_medio = []
gp_alto = []

gp_muy_bajo = []
gp_muy_medio = []
gp_muy_alto = []

gp_ext_bajo = []
gp_ext_medio = []
gp_ext_alto = []

rango_edad = range(0, 120)

for edad in rango_edad:

    mc = MarcoDeCognicion(vertices_p3, etiquetas=['Baja', 'Normal', 'Alta'])
    gp = mc.grado_de_pertenencia(edad)
    gp_bajo.append(gp['Baja'])
    gp_medio.append(gp['Normal'])
    gp_alto.append(gp['Alta'])

    v_muy = ModificadoresLinguisticos.muy(vertices_p3, edad)
    gp_muy_bajo.append(v_muy['grados_pert'][0])
    gp_muy_medio.append(v_muy['grados_pert'][1])
    gp_muy_alto.append(v_muy['grados_pert'][2])

    v_ext = ModificadoresLinguisticos.extremadamente(vertices_p3, edad)
    gp_ext_bajo.append(v_ext['grados_pert'][0])
    gp_ext_medio.append(v_ext['grados_pert'][1])
    gp_ext_alto.append(v_ext['grados_pert'][2])

plt.plot(rango_edad, gp_bajo, 'r', label='Esperanza Baja')
plt.plot(rango_edad, gp_medio, 'k', label='Esperanza Media')
plt.plot(rango_edad, gp_alto, 'b', label='Esperanza Alta')

plt.plot(rango_edad, gp_muy_bajo, 'r--', label='Esperanza Muy Baja')
plt.plot(rango_edad, gp_muy_medio, 'k--', label='Esperanza Muy Media')
plt.plot(rango_edad, gp_muy_alto, 'b--', label='Esperanza Muy Alta')

plt.plot(rango_edad, gp_ext_bajo, 'r:', label='Esperanza Extr. Baja')
plt.plot(rango_edad, gp_ext_medio, 'k:', label='Esperanza Extr. Media')
plt.plot(rango_edad, gp_ext_alto, 'b:', label='Esperanza Extr. Alta')

plt.xlabel('X (años)') #Universo del discurso
plt.ylabel('µ(x)') #Grados de pertenencia
plt.legend(loc=0) #Loc=0 permite la mejor ubicación
plt.grid(True)
plt.show()

