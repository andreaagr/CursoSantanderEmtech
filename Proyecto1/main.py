from lifestore_file import lifestore_sales,lifestore_products,lifestore_searches
from categories_sales import categories, sales_by_category_reverse
from most_searched import quantities_searched
from top50 import quantities_top50
from categories_searches import least_searched
#----------------------------Imprime la lista de los 50 productos con más ventas
#YAAAAAAAAAAAAAAAAAAAAAAAAAAA
'''
index = 0
print("LOS 50 PRODUCTOS MÁS VENDIDOS SON:")
for quantity in reversed(quantities_top50):
    first = True
    for product in quantity:

        if(first == True):
            first = False
            if(product == 0):
                break
        else:
            if(index < 50):
                #top50.append(product)
                print("------------------------------------------------------",index+1,"------------------------------------------------------\n\n")
                print("Producto: ",lifestore_products[product-1][1])
                print("Cantidad: ",quantity[0])
                print("\n")
                index+=1
print("------------------------------------------------------------------------------------------------------------\n\n")
print("Mostrando un total de: ", index,"productos")
'''
#-----------------------------Imprime la lista de los 100 productos más buscados
#YAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA
'''
index = 0
print("LOS 100 PRODUCTOS MÁS BUSCADOS SON:")
for quantity in reversed(quantities_searched):
    first = True
    for product in quantity:
        if(first == True):
            first = False
            if(product == 0):
                break
        else:
            if(index < 100):
                print("------------------------------------------------------",index+1,"------------------------------------------------------\n\n")
                print("Producto: ",lifestore_products[product-1][1])
                print("Cantidad: ",quantity[0])
                print("\n")
                index += 1

print("------------------------------------------------------------------------------------------------------------\n\n")
print("Mostrando un total de: ", index,"productos")
'''

#--------------------------Imprime los 50 productos menos vendidos por categoría
#YAAAAAAAAAAAAAAAAAAAA
'''
print("LOS 100 PRODUCTOS MENOS VENDIDOS POR CATEGORÍA SON:")
count = 0
for i in range(0,len(categories)):
    print("#############################################################################################################")
    print("{:^105}".format(categories[i]))
    print("#############################################################################################################")
    products_and_quantities = sales_by_category_reverse[i]
    #print(products_and_quantities)
    #products_and_quantities.reverse()
    for product,quantity in products_and_quantities:
        if(product != 0):
            print("-------------------------------------------------------------------------------------------------------------\n\n")
            print("Producto: ",lifestore_products[product-1][1])
            print("Cantidad: ",quantity)
            print("Precio: $",lifestore_products[product-1][2],sep="")
            print("\n")
            count += 1
print("------------------------------------------------------------------------------------------------------------\n\n")
print("Mostrando un total de: ",count,"productos")
'''
#-------------Imprime la lista de los 100 productos menos buscados por categoría
#YAAAAAAAAAAAAAAAAAAAAAAAAAA
'''
print("LOS 100 PRODUCTOS MENOS BUSCADOS POR CATEGORÍA SON:")
count = 0
for i in range(0,len(categories)):
    print("#############################################################################################################")
    print("{:^105}".format(categories[i]))
    print("#############################################################################################################")
    products_and_quantities = least_searched[i]
    for product,quantity in products_and_quantities:
        if product != 0:
            print("-------------------------------------------------------------------------------------------------------------\n\n")
            print("Producto: ",lifestore_products[product-1][1])
            print("Cantidad: ",quantity)
            print("Precio: ",lifestore_products[product-1][2])
            print("\n")
            count += 1
print("------------------------------------------------------------------------------------------------------------\n\n")
print("Mostrando un total de: ",count,"productos")
'''