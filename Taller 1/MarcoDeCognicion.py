'''
    Autores:
        Sebastián Castaño
        Nicolás Villegas
        Asignatura: Sistemas de Lógica Difusa. 
        Universidad Nacional de Colombia, Sede Medellín. 2019-01.

'''


class MarcoDeCognicion:

    def __init__(self, vertices=[], etiquetas=[]):

        self.a = vertices[0]
        self.b = vertices[1]
        self.c = vertices[2]
        self.d = vertices[3]
        self.e = self.d*1.3 # 30% más que el último vértice.

        self.etiqueta_1 = etiquetas[0]
        self.etiqueta_2 = etiquetas[1]
        self.etiqueta_3 = etiquetas[2]

    def grado_de_pertenencia(self, x):

        r = {}

        # Hombro izquierdo:

        if x < self.a:
            gp_hi = 1
        elif self.a <= x <= self.b:
            gp_hi = 1 + (self.a - x)/(self.b - self.a)
        else:
            gp_hi = 0

        r[self.etiqueta_1] = gp_hi


        # Medio:

        if self.a < x < self.b:
            gp_m = (x - self.a)/(self.b - self.a)
        elif self.b <= x <= self.c:
            gp_m = 1
        elif self.c < x <= self.d:
            gp_m = 1 + (self.c - x) / (self.d - self.c)
        else:
            gp_m = 0

        r[self.etiqueta_2] = gp_m


        # Hombro derecho:

        if self.c <= x <= self.d:
            gp_hd = (x - self.c) / (self.d - self.c)
        elif x > self.d:
            gp_hd = 1
        else:
            gp_hd = 0

        r[self.etiqueta_3] = gp_hd

        return r

class ModificadoresLinguisticos:

    def muy(vertices, x):
        
        a_orig = vertices[0]
        b_orig = vertices[1]
        c_orig = vertices[2]
        d_orig = vertices[3]

        a = 2/3 * a_orig
        b = (b_orig + c_orig) * 0.5 - 0.333*(c_orig - b_orig)
        c = (b_orig + c_orig) * 0.5 + 0.333*(c_orig - b_orig)
        d = 1.1*d_orig

        # Cálculo del grado de pertenencia:

        r = []

        # Hombro izquierdo:

        if x < a:
            gp_hi = 1
        elif a <= x <= b:
            gp_hi = 1 + (a - x)/(b - a)
        else:
            gp_hi = 0

        r.append(gp_hi)


        # Medio:

        if a < x < b:
            gp_m = (x - a)/(b - a)
        elif b <= x <= c:
            gp_m = 1
        elif c < x <= d:
            gp_m = 1 + (c - x) / (d - c)
        else:
            gp_m = 0

        r.append(gp_m)


        # Hombro derecho:

        if c <= x <= d:
            gp_hd = (x - c) / (d - c)
        elif x > d:
            gp_hd = 1
        else:
            gp_hd = 0

        r.append(gp_hd)

        return {
            'grados_pert' : [gp_hi**3, gp_m**3, gp_hd**3],
            'vertices' : [a, b, c, d]
        }

    def extremadamente(vertices, x):

        a_orig = vertices[0]
        b_orig = vertices[1]
        c_orig = vertices[2]
        d_orig = vertices[3]

        a = 1/3 * a_orig
        b = (b_orig + c_orig) * 0.5 - 0.1667*(c_orig - b_orig)
        c = (b_orig + c_orig) * 0.5 + 0.1667*(c_orig - b_orig)
        d = 1.15*d_orig

        # Cálculo del grado de pertenencia:

        r = []

        # Hombro izquierdo:

        if x < a:
            gp_hi = 1
        elif a <= x <= b:
            gp_hi = 1 + (a - x)/(b - a)
        else:
            gp_hi = 0

        r.append(gp_hi)


        # Medio:

        if a < x < b:
            gp_m = (x - a)/(b - a)
        elif b <= x <= c:
            gp_m = 1
        elif c < x <= d:
            gp_m = 1 + (c - x) / (d - c)
        else:
            gp_m = 0

        r.append(gp_m)


        # Hombro derecho:

        if c <= x <= d:
            gp_hd = (x - c) / (d - c)
        elif x > d:
            gp_hd = 1
        else:
            gp_hd = 0

        r.append(gp_hd)

        return {
            'grados_pert' : [gp_hi**5, gp_m**5, gp_hd**5],
            'vertices' : [a, b, c, d]
        }