'''
    Autor: García Ruiz Andrea

    Puntos requeridos por la gerencia:
        1. Productos más vendidos (50)
'''
from lifestore_file import lifestore_sales,lifestore_products

#Productos con mayores ventas
#..................................................Inicializa la lista con ceros
sales_by_product = []
for i in range(0,len(lifestore_products)):
    # temp[0] = id_product
    # temp[1] = sale
    sales_by_product.append(0)
#...............................................................................
#.......................Cuenta cuantas unidades se han comprado de cada producto
for sale in lifestore_sales:
    sales_by_product[sale[1]] += 1
#-------------------------------------------------------------------------------
#---------------------------------------Permite obtener los mejores 50 productos
quantities = []
index = 0
for value in sales_by_product:
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

top50 = []

for quantity in reversed(quantities):
    first = True
    for product in quantity:

        if(first == True):
            first = False
            if(product == 0):
                break
        else:
            if(len(top50) < 50):
                top50.append(product)
#-------------------------------------------------------------------------------