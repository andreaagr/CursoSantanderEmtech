from rating import num_sales
from lifestore_file import lifestore_products 

total = 0
index = 0
for sale in num_sales:
    
    if sale != -1:
        print(index)
        print("Producto:",lifestore_products[index-1][1])
        print("Num sale:",sale)
        subtotal = (sale * lifestore_products[index-1][2])
        print(subtotal)
        total += subtotal
    index+=1

print(total)
