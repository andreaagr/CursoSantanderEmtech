'''
    Autor: García Ruiz Andrea

    Puntos requeridos por la gerencia:
        1. Productos más buscados (100)
'''
from lifestore_file import lifestore_searches,lifestore_products

#..................................................Inicializa la lista con ceros
searchs_by_product = []
for i in range(0,len(lifestore_products)):
    searchs_by_product.append(0)
#...............................................................................
#.......................Cuenta cuantas unidades se han comprado de cada producto
for search in lifestore_searches:
    searchs_by_product[search[1]] += 1
#...............................................................................
#..................................Se realiza el mismo proceso que para el top50
quantities_searched = []
index = 0
for value in searchs_by_product:
    temp = []
    contains_value = False

    for quantity in quantities_searched:
        if(quantity[0] == value and index != 0):
            quantity.append(index)
            contains_value = True

    if(contains_value == False):
        temp.append(value)
        temp.append(index)
        quantities_searched.append(temp)
    index += 1

quantities_searched.sort(key = lambda x : x[0])
#...............................................................................