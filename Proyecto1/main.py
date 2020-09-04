from lifestore_file import lifestore_sales,lifestore_products,lifestore_searches
from top50 import top50
from most_searched import most_searched,least_searched,quantities
from categories_most import categories, sales_by_category, sales_by_category_reverse
from categories_least import least_searched

#----------------------------Imprime la lista de los 50 productos con más ventas
#YA
'''
print("Los 50 productos con mejores ventas son:\n")
index = 1
for product in top50:
    print(index,". ",lifestore_products[product-1][1])
    index += 1
'''
#-----------------------------Imprime la lista de los 100 productos más buscados
#YA
'''
print("Los 100 productos con más búsquedas son:\n")
index = 1
for product in most_searched:
    print(index,". ",lifestore_products[product-1][1])
    index += 1
'''



#--------------------------Imprime los 50 productos menos vendidos por categoría
#YA
'''
count = 0
for i in range(0,len(categories)):
    print("#############################################################################################################")
    print("{:^105}".format(categories[i]))
    print("#############################################################################################################")
    products_and_quantities = sales_by_category_reverse[i]
    #products_and_quantities.reverse()
    for product,quantity in products_and_quantities:
        print("-------------------------------------------------------------------------------------------------------------\n\n")
        print("Producto: ",lifestore_products[product-1][1])
        print("Cantidad: ",quantity)
        print("Precio: ",lifestore_products[product-1][2])
        print("\n")
        count += 1
'''
#-------------Imprime la lista de los 100 productos menos buscados por categoría
count = 0
for i in range(0,len(categories)):
    print("#############################################################################################################")
    print("{:^105}".format(categories[i]))
    print("#############################################################################################################")
    products_and_quantities = least_searched[i]
    #products_and_quantities.reverse()
    for product,quantity in products_and_quantities:
        print("-------------------------------------------------------------------------------------------------------------\n\n")
        print("Producto: ",lifestore_products[product-1][1])
        print("Cantidad: ",quantity)
        print("Precio: ",lifestore_products[product-1][2])
        print("\n")
        count += 1


'''
Tal vez no
print("LOS 100 PRODUCTOS CON MENORES BÚSQUEDAS SON;\n")
for quantity in quantities:
    first = True
    for product in quantity:
        if(first == True):
            first = False
        else:
            print("-------------------------------------------------------------------------------------------------------------\n\n")
            print("Producto: ",lifestore_products[product-1][1])
            print("Cantidad: ",quantity[0])
            print("\n")
'''