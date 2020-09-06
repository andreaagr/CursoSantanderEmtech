from lifestore_file import lifestore_products
from top50 import quantities_top50

categories = []
sales_by_category = []
#...............................................Obtiene las categorías existentes
for product in lifestore_products:
    if(product[3] not in categories):
        categories.append(product[3])
        sales_by_category.append([])
#................................................................................
#---------------------------Obtener los 50 productos menos vendidos por categoría
index = 0
for quantity in quantities_top50:
    first = True
    for product in quantity:
        if(first):
            first = False
        else:
            if index < 50:
                #El producto con id = 0 no existe, por lo que no es tomado en cuenta
                if(product == 0):
                    index-=1
                #Se obtiene el índice de la categoría a la que pertenece el producto    
                category_index = categories.index(lifestore_products[product-1][3])
                #Se crea una lista que agrupa el producto y cantidad
                temp = []
                temp.append(product)
                temp.append(quantity[0])
            
                #Se realizan las validaciones correspondientes para ver si en la posición ya existen datos
                sales_by_category[category_index].append(temp)
                index+= 1
#................................................................................