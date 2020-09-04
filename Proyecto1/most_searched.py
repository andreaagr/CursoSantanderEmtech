'''
    Autor: García Ruiz Andrea

    Puntos requeridos por la gerencia:
        1. Productos más buscados (100)
'''
from lifestore_file import lifestore_searches,lifestore_products

#Productos con mayores ventas
#..................................................Inicializa la lista con ceros
searchs_by_product = []
for i in range(0,len(lifestore_products)):
    searchs_by_product.append(0)
#...............................................................................
#.......................Cuenta cuantas unidades se han comprado de cada producto
for search in lifestore_searches:
    searchs_by_product[search[1]] += 1
#-------------------------------------------------------------------------------
#---------------------------------Permite obtener los 100 productos más buscados
quantities = []
index = 0
for value in searchs_by_product:
    temp = []
    contains_value = False

    for quantity in quantities:
        if(quantity[0] == value and index != 0):
            quantity.append(index)
            contains_value = True

    if(contains_value == False):
        temp.append(value)
        temp.append(index)
        quantities.append(temp)
    index += 1

quantities.sort(key = lambda x : x[0])

most_searched = []

for quantity in reversed(quantities):
    first = True
    for product in quantity:
        if(first == True):
            first = False
            if(product == 0):
                break
        else:
            if(len(most_searched) < 100):
                most_searched.append(product)
#-------------------------------------------------------------------------------
#-----------------------------------Permite obtener los productos menos buscados
least_searched = []
for quantity in quantities:
    first = True
    for product in quantity:
        if(first == True):
            first = False
        else:
            if(len(least_searched) < 100):
                least_searched.append(product)