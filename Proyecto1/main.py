from lifestore_file import lifestore_sales,lifestore_products,lifestore_searches
from categories_sales import categories, sales_by_category_reverse
from most_searched import quantities_searched
from top50 import quantities_top50
from categories_searches import least_searched
from rating import best_products,percent
from statistics import total,sales_per_month,months

#---------------------------------------------------------------------------------
users = [["Admin","admin"],["Invitado","guest"],["Otro usuario","pass"]]
salir = True
autenticado = True
logged = False
print("Bienvenido al sistema de gestión de Lifestore\nAutenticate para poder comenzar :)")
while(salir):
    while(autenticado):
        user_log = input("Ingresa tu usuario: ")
        for user in users:
            if(user[0] == user_log):
                password = input("Ingresa tu contraseña: ")
                if user[1] == password:
                    print("Correcto, bienvenido :D")
                    logged = True
                else:
                    print("Contraseña incorrecta :(")
            #else:
            #    
   
        
        if(logged == True):
            principal = True
            while(principal):
                print("¿Qué deseas consultar?\n1) 50 productos más vendidos \n2) 100 productos más buscados")
                print("3) 50 productos menos vendidos por categoría\n4) 100 productos menos buscados por categoría")
                print("5) 20 productos con mejores reseñas \n6) 20 productos con menos reseñas")
                print("7) Total de ingresos\n8) Número de ventas por mes\n9) Meses con más ventas\n10) Salir")
                seleccion = input("Ingresa el número de opción: ")
                if(seleccion == "1"):
                    #----------------------------Imprime la lista de los 50 productos con más ventas
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
                                    print("------------------------------------------------------",index+1,"------------------------------------------------------\n\n")
                                    print("Producto: ",lifestore_products[product-1][1])
                                    print("Cantidad: ",quantity[0])
                                    print("\n")
                                    index+=1
                    print("------------------------------------------------------------------------------------------------------------\n\n")
                    print("Mostrando un total de: ", index,"productos")
                elif(seleccion == "2"):
                    #-----------------------------Imprime la lista de los 100 productos más buscados
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
                elif(seleccion == "3"):
                    #--------------------------Imprime los 50 productos menos vendidos por categoría
                    print("LOS 100 PRODUCTOS MENOS VENDIDOS POR CATEGORÍA SON:")
                    count = 0
                    for i in range(0,len(categories)):
                        print("#############################################################################################################")
                        print("{:^105}".format(categories[i]))
                        print("#############################################################################################################")
                        products_and_quantities = sales_by_category_reverse[i]
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
                elif(seleccion == "4"):
                    #-------------Imprime la lista de los 100 productos menos buscados por categoría
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
                elif(seleccion == "5"):
                    #--Imprime la lista de los 20 productos con mejores reseñas y menos devoluciones
                    print("LOS 20 PRODUCTOS CON MEJORES RESEÑAS SON:")
                    count = 0
                    percent_count = 0
                    for products in best_products:
                        if count == 20:
                            break
    
                        print("###############################################################################################################")
                        print("{:^105}".format("Porcentaje de devoluciones: %.1f" % percent[percent_count]))
                        print("###############################################################################################################")
    
                        for product in products:
                            if(count < 20):
                                print("------------------------------------------------------",count+1,"------------------------------------------------------\n\n")
                                print("Producto: ",lifestore_products[product[0]-1][1])
                                print("Promedio de calificaciones: ",product[1])
                                print("\n")
                                count+=1
                            else:
                                break
                        percent_count += 1
                elif(seleccion == "6"):
                    #-----Imprime la lista de los 20 productos con peores reseñas y más devoluciones
                    print("LOS 20 PRODUCTOS CON PEORES RESEÑAS SON:")
                    count = 0
                    percent_count = 0
                    for products in reversed(best_products):
    
                        if count == 20:
                            break
    
                        print("###############################################################################################################")
                        print("{:^105}".format("Porcentaje de devoluciones: %.4f" % percent[len(percent)-percent_count-1]))
                        print("###############################################################################################################")
    
                        for product in reversed(products):
                            if(count < 20):
                                print("------------------------------------------------------",count+1,"------------------------------------------------------\n\n")
                                print("Producto: ",lifestore_products[product[0]-1][1])
                                print("Promedio de calificaciones: ",product[1])
                                print("\n")
                                count+=1
                            else:
                                break

                        percent_count += 1
                elif(seleccion == "7"):
                    #--------------------------------------------------------------Total de ingresos
                    print("Total de ingresos: ",total)
                elif(seleccion == "8"):
                    #-------------------------------------------------------Número de ventas por mes
                    index = 0
                    for num_sales in sales_per_month:
                        print("#############################################################################################################")
                        print("{:^105}".format(months[index]))
                        print("#############################################################################################################")
                        print("Número de ventas:", num_sales) 
                        index+=1

                elif(seleccion == "9"):
                    #-----------------------------------------------------------Meses con más ventas
                    print("------------------------------------------------------------------------------------------------------------")
                    print("MESES EN ORDEN DE VENTAS:")
                    months_sort = sorted(sales_per_month)
                    temp_sales_per_month = sales_per_month[:]
                    months_sort.reverse()
                    for sales in months_sort:
                        position = temp_sales_per_month.index(sales)
                        print(months[position])
                        temp_sales_per_month[position] = -1
                    print("------------------------------------------------------------------------------------------------------------")
                elif(seleccion == "10"):
                    principal = False
                    autenticado = False
                    salir = False     
        else:
            print("Usuario no registrado, prueba de nuevo :(")