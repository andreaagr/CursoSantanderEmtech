from rating import num_sales,refounds
from lifestore_file import lifestore_products,lifestore_sales 

index = 0
#---------------------------------------------------------------------------------Ventas promedio mensuales
#Tomando en cuenta las ventas de 3 años de la tienda
position = 0
months = ["Enero","Febrero","Marzo","Abril","Mayo","Junio","Julio","Agosto","Septiembre","Octubre","Noviembre","Diciembre"]
years = []
sales_per_year = [] #Guarda el id del producto comprado en el año y mes correspondiente
subtotals = []      #Guarda la suma de los productos comprados por cada mes

for sale in lifestore_sales:
    #Obtiene la fecha de compra,para después localizar el año y mes
    date = sale[3]
    month = date[3:5]
    year = date[6:]
    #------------------------------------------------------
    #Guarda el id y precio del producto en el mes y año correspondientes
    if year not in years:
        years.append(year)
        sales_per_year.append([])
        subtotals.append([])
        for i in range(0,12):
            sales_per_year[position].append([])
            subtotals[position].append(0)
        position += 1

    index_year = years.index(year)
    sales_per_year[index_year][int(month)-1].append(sale[1])
    subtotals[index_year][int(month)-1] += lifestore_products[sale[1]-1][2]
    #------------------------------------------------------

index = 0
month_sales_avg = []
num_years = len(years)

for i in range(0,12):
    sum_sales = 0
    for j in range(0,num_years):
        sum_sales += subtotals[j][i] 
    #Obtiene el promedio de las ventas de cada mes, tomando en cuenta los 3 años
    month_sales_avg.append(sum_sales/num_years)