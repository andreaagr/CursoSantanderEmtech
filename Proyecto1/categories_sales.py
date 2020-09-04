from lifestore_file import lifestore_products
from top50 import quantities_top50

categories = []
sales_by_category = []
sales_by_category_reverse = []
#-----------------------------------------------------Obtiene las categorías
for product in lifestore_products:
    if(product[3] not in categories):
        categories.append(product[3])
        sales_by_category.append(0)
        sales_by_category_reverse.append(0)
#---------------------------Obtener los 50 productos menos vendidos por categoría
index = 0
for quantity in quantities_top50:
    first = True
    for product in quantity:
        if(first):
            first = False
        else:
            if index < 50:
                if(product == 0):
                    index-=1
                category_index = categories.index(lifestore_products[product-1][3])
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
#----------------------------------------------------------------------------------