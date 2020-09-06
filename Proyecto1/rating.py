'''
    Autor: García Ruiz Andrea

    Puntos requeridos por la gerencia:
        2. Productos con mejores y peores reseñas (20)
'''
from lifestore_file import lifestore_products,lifestore_sales

#---------------------------------------------------------------------------Datos para el análisis
#-----------------------------------------------------------------------------------Inicialización
sum_scores = []        #Almacena la suma de los scores de cada producto
num_sales = []         #Almacena el número de ventas de cada producto
refounds = []          #Almacena el número de reembolsos de cada producto

rating_average = []    #Almacena los promedios de score de cada producto
product_rating = []    #Almacena la asociación del id del producto con el promedio de score
product_refounds = []  #Almacena la asociación del id del producto con el porcentaje de devolución
percent = []           #Almacena los porcentajes de devolución existentes
best_products = []     #Los mejores productos serán aquellos que tengan un menor porcentaje de 
                       #devolución y un mayor promedio de score

for product in lifestore_products:
    sum_scores.append(-1)
    num_sales.append(-1)
    refounds.append(-1)
#--------------------------------------------------------------------------------------------------
#---------------------------Obteniendo la cantidad de reembolsos, suma de scores y número de ventas
for sale in lifestore_sales:
    if(sum_scores[sale[1]] == -1):
        sum_scores[sale[1]] = 0
        num_sales[sale[1]] = 0
        refounds[sale[1]] = 0

    if(sale[4] == 1):
        refounds[sale[1]] += 1

    sum_scores[sale[1]] += sale[2]
    num_sales[sale[1]] += 1
#-------------------------------------------------------------------------------------------------
#------------------------Obteniendo el promedio de score de cada producto y promedio de devolución
for i in range(0,len(sum_scores)):
    if(num_sales[i] != -1):
        rating_info = []
        refound_info = []

        rating_info.append(i)
        rating_info.append(sum_scores[i] / num_sales[i])
        product_rating.append(rating_info)
        
        refound_info.append(i)
        refound_info.append(refounds[i] / num_sales[i])
        product_refounds.append(refound_info)
#--------------------------------------------------------------------------------------------------
#----------------------------------------------------------------Obtiene los porcentajes existentes
for product in product_refounds:
    if(product[1] not in percent):
        percent.append(product[1])
        best_products.append([])

percent.sort()   #Ordena los porcentajes de menor a mayor
#--------------------------------------------------------------------------------------------------
#------------------------------------------------------------------------------------------Análisis
#---------------------------------------------------------------------------------MEJORES PRODUCTOS
#-Asocia a todos los productos con un mismo porcentaje de devoluciones y los guarda en la localidad
#corresponidente, basándose en la lista percent
index = 0
for product in product_refounds:
    temp = []
    temp.append(product[0])
    temp.append(product_rating[index][1])
    best_products[percent.index(product[1])].append(temp)
    index += 1
#---------------------------------------------------------------------------------------------------
#-----------------------------------------------Ordena los productos de cada índice de mayor a menor
for product in best_products:
    product.sort(key = lambda x : x[1])
    product.reverse()
#---------------------------------------------------------------------------------------------------