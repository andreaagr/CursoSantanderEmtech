'''
    Autor: García Ruiz Andrea

    Puntos requeridos por la gerencia:
        1. Productos más vendidos (50)
'''
from lifestore_file import lifestore_sales,lifestore_products
#.................................................................Inicializa la lista con ceros
sales_by_product = []
for i in range(0,len(lifestore_products)):
    sales_by_product.append(0)
#..............................................................................................
#......................................Cuenta cuantas unidades se han comprado de cada producto
for sale in lifestore_sales:
    sales_by_product[sale[1]] += 1
#..............................................................................................
#.......................................Agrupa los productos, a partir de su cantidad de ventas
quantities_top50 = []
index = 0
for value in sales_by_product:
    temp = []
    contains_value = False
    
    #Revisa si el valor ya se ha agregado antes, de ser así agrega el id_producto a la lista
    for quantity in quantities_top50:
        if(quantity[0] == value and index != 0):
            quantity.append(index)
            contains_value = True

    #Si el valor no se ha agregado a la lista, genera una nueva posición en quantities_top50
    if(contains_value == False):
        temp.append(value)
        temp.append(index)
        quantities_top50.append(temp)
    index += 1

#Ordena la lista obtenida de menor a mayor
quantities_top50.sort(key = lambda x : x[0])
#..............................................................................................