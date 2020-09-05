from rating import num_sales
from lifestore_file import lifestore_products,lifestore_sales 

total = 0
index = 0
sales_per_month = []
months = ["Enero","Febrero","Marzo","Abril","Mayo","Junio","Julio","Agosto","Septiembre","Octubre","Noviembre","Diciembre"]

#-------------------------------------Obtiene el total de ingresos
for  i in range(0,12):
    sales_per_month.append(0)

for sale in num_sales:
    if sale != -1:
        subtotal = (sale * lifestore_products[index-1][2])
        total += subtotal
    index+=1
#-----------------------------------------------------------------
#-------------------------------------...Cuenta las ventas por mes
for sale in lifestore_sales:
    date = sale[3]
    month = int(date[3:5])
    sales_per_month[month-1] += 1