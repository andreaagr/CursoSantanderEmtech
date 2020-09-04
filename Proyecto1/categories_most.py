from lifestore_file import lifestore_products
from top50 import quantities

categories = []
sales_by_category = []
sales_by_category_reverse = []
#-----------------------------------------------------Obtiene las categorías
for product in lifestore_products:
    if(product[3] not in categories):
        categories.append(product[3])
        sales_by_category.append(0)
        sales_by_category_reverse.append(0)

#---------------------------------------Productos más vendidos por categoría
'''
for quantity in reversed(quantities):
    first = True
    for product in quantity:
        if(first):
            first = False
        else:
            category_index = categories.index(lifestore_products[product][3])
            temp = []
            temp.append(product)
            temp.append(quantity[0])
            if(sales_by_category[category_index] == 0):
                element = []
                element.append(temp)
                sales_by_category[category_index] = element
            else:                
                sales_by_category[category_index].append(temp) 
'''
#----------------------------Imprime los 50 productos más vendidos por categoría
'''
for i in range(0,len(categories)):
    print("#############################################################################################################")
    print("{:^105}".format(categories[i]))
    print("#############################################################################################################")
    products_and_quantities = sales_by_category[i]
    for product,quantity in products_and_quantities:
        if quantity != 0:
            print("-------------------------------------------------------------------------------------------------------------\n\n")
            print("Producto: ",lifestore_products[product-1][1])
            print("Cantidad: ",quantity)
            print("Precio: ",lifestore_products[product-1][2])
            print("\n")
'''
#---------------------------Obtener los 50 productos menos vendidos por categoría
index = 0
for quantity in quantities:
    first = True
    for product in quantity:
        if(first):
            first = False
        else:
            if index < 50:
                category_index = categories.index(lifestore_products[product][3])
                temp = []
                temp.append(product)
                temp.append(quantity[0])
            
                if(sales_by_category_reverse[category_index] == 0):
                    element = []
                    element.append(temp)
                    sales_by_category_reverse[category_index] = element
                else:                
                    sales_by_category_reverse[category_index].append(temp)
                index+= 1
#---------------------------Obtener los 50 productos menos vendidos por categoría