# -*- coding: utf-8 -*-
"""
Editor de Spyder

Este es un archivo temporal.
"""

import pandas as pd
import numpy as np


#13) ¿Como combinar varias series para hacer un DataFrame?

ser1 = pd.Series(list('abcedfghijklmnopqrstuvwxyz'))
ser2 = pd.Series(np.arange(26))
df_juntado = pd.DataFrame(data=(ser1,ser2),index=['a','b'])
df_juntado

#¿Como obtener los items que esten en una serie A y no en una serie B?
ser1 = pd.Series([1, 2, 3, 4, 5])
ser2 = pd.Series([4, 5, 6, 7, 8])
dif = []
for i in ser1:
    if((i not in ser2)):
        dif.append(i)
print(ser1.iloc[dif])

#¿Como obtener los items que no son comunes en una serie A y serie B?
        
#¿Como obtener el numero de veces que se repite un valor en una serie?
serPiten = pd.Series(np.take(list('abcdefgh'), np.random.randint(8, size=30)))


#¿Como mantener los 2 valores mas repetidos de una serie, y a los demas valores cambiarles por 0 ?
ser = pd.Series(np.random.randint(1, 5, [12]))

# 18) ¿Como transformar una serie de un arreglo de numpy a un DataFrame con un shape definido?
ser = pd.Series(np.random.randint(1, 10, 35))
shape(7,5)

# 19) ¿Obtener los valores de una serie conociendo la posicion por indice?
ser = pd.Series(list('abcdefghijklmnopqrstuvwxyz'))
pos = [0, 4, 8, 14, 20]
# a e i o u

#20) ¿Como anadir series vertical u horizontalmente a un DataFrame?
ser1 = pd.Series(range(5))
ser2 = pd.Series(list('abcde'))

# 21)¿Obtener la media de una serie agrupada por otra serie?
groupby tambien esta disponible en series.

frutas = pd.Series(np.random.choice(['manzana', 'banana', 'zanahoria'], 10))
pesos = pd.Series(np.linspace(1, 10, 10))
print(pesos.tolist())
print(frutas.tolist())
#> [1.0, 2.0, 3.0, 4.0, 5.0, 6.0, 7.0, 8.0, 9.0, 10.0]
#> ['banana', 'carrot', 'apple', 'carrot', 'carrot', 'apple', 'banana', 'carrot', 'apple', 'carrot']

# Los valores van a cambiar por ser random
# apple     6.0
# banana    4.0
# carrot    5.8
# dtype: float64

# 22) ¿Como importar solo columnas especificas de un archivo csv?
path = 'C:\\Users\Gorky\Documents\GitHub\examen-primer-bimestre-munoz-gorky\data\BostonHousing.csv'
df = pd.read_csv(
        path,
        usecols=['indus','nox']
        )