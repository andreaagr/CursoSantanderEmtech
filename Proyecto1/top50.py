'''
    Autor: García Ruiz Andrea

    Puntos requeridos por la gerencia:
        1. Productos más vendidos (50)
'''
from lifestore_file import lifestore_sales,lifestore_products

#..................................................Inicializa la lista con ceros
sales_by_product = []
for i in range(0,len(lifestore_products)):
    sales_by_product.append(0)
#...............................................................................
#.......................Cuenta cuantas unidades se han comprado de cada producto
for sale in lifestore_sales:
    sales_by_product[sale[1]] += 1
#-------------------------------------------------------------------------------
#---------------------------------------Permite obtener los mejores 50 productos
quantities_top50 = []
index = 0
for value in sales_by_product:
    temp = []
    contains_value = False
    #if(index != 0):
    for quantity in quantities_top50:
        if(quantity[0] == value and index != 0):
            quantity.append(index)
            contains_value = True

    if(contains_value == False):
        temp.append(value)
        temp.append(index)
        quantities_top50.append(temp)
    #else:
    index += 1

quantities_top50.sort(key = lambda x : x[0])
#-------------------------------------------------------------------------------