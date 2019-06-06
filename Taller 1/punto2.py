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
    ubicación geográfica del país que se analice. Por tanto, se analiza para cada continente
    hallando la media.


'''




gen = ['mujeres', 'hombres']

for g in gen:

    regiones = ['África', 'Asia', 'Europa', 'Oriente Medio', 'Oceanía', 'América']
    espvida = []
    espvida_std = [] #Desviación estandar para definir limites de las etiquetas lingüisticas

    var = 'Esperanza de vida ({})'.format(g)

    #Cálculo de la media y la desviación estandar para cada región
    for region in regiones:
        esp_vida = data[data['Región'] == region][var]
        espvida.append(esp_vida.mean())
        espvida_std.append(esp_vida.std())
        print('-'*50)
        print('[Región: {}]'.format(region))
        print(esp_vida.describe())
        print('\n')

    #Cálculo de vértices para el marco de cognición
    vertices_punto2 = []
    for i in range (0,6):
        vertices_punto2.append(int(espvida[i] - 4*espvida_std[i]))
        vertices_punto2.append(int(espvida[i] - 2*espvida_std[i]))
        vertices_punto2.append(int(espvida[i] + 2*espvida_std[i]))
        vertices_punto2.append(int(espvida[i] + 4*espvida_std[i]))

    vert_africa = vertices_punto2[0:4]
    vert_asia = vertices_punto2[4:8]
    vert_europa = vertices_punto2[8:12]
    vert_oriente_medio = vertices_punto2[12:16]
    vert_oceania = vertices_punto2[16:20]
    vert_america = vertices_punto2[20:24]

    #Opcional para visualizar los vértices de cada región
    '''
    print('Los vértices para {} son:'.format(regiones[0]))
    print('{}'.format(vert_africa))
    print('Los vértices para {} son:'.format(regiones[1]))
    print('{}'.format(vert_asia))
    print('Los vértices para {} son:'.format(regiones[2]))
    print('{}'.format(vert_europa))
    print('Los vértices para {} son:'.format(regiones[3]))
    print('{}'.format(vert_oriente_medio))
    print('Los vértices para {} son:'.format(regiones[4]))
    print('{}'.format(vert_oceania))
    print('Los vértices para {} son:'.format(regiones[5]))
    print('{}'.format(vert_america))
    '''

    promedio_mundial = data[var].mean()

    objects = (region for region in regiones)
    y_pos = np.arange(len(regiones))
    plt.bar(y_pos, espvida, align='center', alpha=0.5, label='Esperanza de vida')
    plt.xticks(y_pos, objects)
    plt.ylabel('Esperanza de vida (años)')
    plt.title('Esperanza de vida en {} según la región'.format(g))
    plt.plot(y_pos, [promedio_mundial for it in y_pos], 'k:', label='Promedio mundial')
    plt.legend(loc=4)
    plt.show()

    '''
        Inicio de marcos de cognición:
    '''
    #Se grafican los marcos de cognición de cada región

    z=0
    vertices=[vert_africa,vert_asia,vert_europa,vert_oriente_medio,vert_oceania,vert_america]

    for vertice in vertices:
        mc = MarcoDeCognicion(vertice, etiquetas=['Baja', 'Normal', 'Alta'])
        x_range = range(0, 110)
        y1 = []
        y2 = []
        y3 = []

        for x in x_range:
            gpx = mc.grado_de_pertenencia(x)
            y1.append(gpx['Baja'])
            y2.append(gpx['Normal'])
            y3.append(gpx['Alta'])
            
        plt.plot(x_range, y1,label='Esperanza Baja')
        plt.plot(x_range, y2,label='Esperanza Media')
        plt.plot(x_range, y3,label='Esperanza Alta')
        plt.title('Esperanza de vida de {} en {}'.format(g, regiones[z]))
        plt.xlabel('X (años)') #Universo del discurso
        plt.ylabel('µ(x)') #Grados de pertenencia
        plt.legend(loc=0) #Loc=0 permite la mejor ubicación
        plt.grid(True)
        plt.show()
        z=z+1