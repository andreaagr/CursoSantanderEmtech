from lifestore_file import lifestore_products
from most_searched import quantities_searched
from categories_sales import categories

#-------------------------Obtener los 100 productos menos buscados por categoría
least_searched = []
for i in range(0,len(categories)):
    least_searched.append(0)

print(quantities_searched)
index = 0
for quantity in quantities_searched:
    first = True
    for product in quantity:
        if(first):
            first = False
        else:
            if index < 100:
                if(product == 0):
                    index-=1
                category_index = categories.index(lifestore_products[product-1][3])
                temp = []
                temp.append(product)
                temp.append(quantity[0])

                if(least_searched[category_index] == 0):
                    element = []
                    element.append(temp)
                    least_searched[category_index] = element
                else:                
                    least_searched[category_index].append(temp)
                index+= 1