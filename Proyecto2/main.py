import csv

exports = {}
imports = {}
countries = set()
transports = set()
total_value = 0
total_ops = {}
'''
Entrada: Diccionario con una clave de tipo tupla, el cual representa una ruta de importación o exportación

Salida: Diccionario con el promedio de las operaciones valor total/número de operaciones
'''
def ingresos_por_ruta(routes):
    result = {} 
    for key in routes.keys():
        # Realiza la suma de los valores totales de esa ruta y realiza un conteo del número de operaciones
        for data in routes[key]:
            if key in result:
                result[key][1] += int(data[6])
                result[key][0] += 1
            else:
                result[key] = [0,int(data[6])]        
        #-------------------------------------------------------------------------------------------------
    return {key:result[key][1]/result[key][0] for key in routes.keys()}


'''
Entrada: Diccionario con una clave de tipo tupla, el cual representa una ruta de importación o exportación y un número (0/1) 
el cual representa si el dato de retorno será un diccionario o una lista

Salida: Diccionario o lista ordenada con los datos de cada ruta, a partir de los valores obtenidos según el medio de transporte 
utilizado
'''
def agrupar_por_vehiculo(routes,tipo_retorno):
    transport = {}  
    for key in routes.keys():
        for data in routes[key]:
            if data[4] in transport:
                transport[data[4]] += int(data[6])
            else:
                transport[data[4]] = 0
    if tipo_retorno == 0:
        return sorted(transport.items(), key = lambda x : x[1], reverse = True)
    else: 
        return transport

'''
Entrada: Diccionario con el promedio de operaciones, cadena que indica si es exportación o importación y un booleano saber en que orden
se necesita la lista que retorna

Salida: Salida en pantalla de los datos en la lista ordenada, la cual muestra las 10 mejores rutas de importación y exportación
'''
def obtener_top(results_per_country, tipo_mov, invertir = False):
    sorted_dict = sorted(results_per_country.items(), key = lambda x : x[1],reverse = invertir)
    cont = 0
    print("LAS 10 MEJORES RUTAS DE %s SON:\n" % (tipo_mov.upper()))
    print("-------------------------------------------------------------------------------------\n\n")
    for data in sorted_dict:
        if cont < 10:
            print("Ruta: ",data[0][0],"-",data[0][1])
            print("Promedio de %s :" % (tipo_mov),data[1])
            print("-------------------------------------------------------------------------------------\n\n")

        cont += 1

#Recibe diccionarios
'''
Entrada: Recibe 2 diccionarios con los datos de importación y exportación agrupados por vehículos

Salida: Salida en pantalla de los datos sumados y ordenados de mayor a menor, obtenidos del diccionario de entrada
'''
def imprimir_info_vehiculos(imports,exports):
    results = {}
    for transport in transports:
        results[transport] = imports[transport] + exports[transport]
    
    sorted_res = sorted(results.items(), reverse = True)
    print("MEDIOS DE TRANSPORTE MÁS IMPORTANTES:")
    print("-------------------------------------------------------------------------------------\n\n")
    for i in range(3):
        print("Medio de transporte: %s" % sorted_res[i][0])
        print("Valor de las importaciones: %i" % imports[sorted_res[i][0]])
        print("Valor de las exportaciones: %i" % exports[sorted_res[i][0]])
        print("Suma de valores: %i" % sorted_res[i][1])
        print("-------------------------------------------------------------------------------------\n\n")

    print("EL MEDIO QUE SE DEBE REDUCIR ES: %s" % (sorted_res[3][0]))

'''
Entrada: Diccionario cuya clave es un conjunto, el cual tiene los datos de las rutas que involucren 2 países

Salida: Salida en pantalla de las rutas que generan el 80% del valor de las importaciones y exportaciones
'''
def valor_paises(total_ops):
    suma = 0
    cont = 0
    _80_percent = []
    # El diccionario se convierte en una lista ordenada de mayor a menor
    sorted_ops = sorted(total_ops.items(), reverse = True, key = lambda x : x[1])
    
    # Mientras no se haya llegado al 80% del valor total
    while suma < (total_value*0.8):
        # Se agrega la información de otra ruta
        _80_percent.append(sorted_ops[cont][0])
        # Se suma su valor
        suma += sorted_ops[cont][1]
        # Se suma uno al contador que sirve para recorrer la lista sorted_ops
        cont += 1
    
    print("RUTAS QUE GENERAN EL 80% DEL VALOR DE LAS IMPORTACIONES Y EXPORTACIONES:")
    print("-------------------------------------------------------------------------------------\n\n")
    for route in _80_percent:
        set_route = set(route)
        print("Ruta: %s - %s" % (set_route.pop(),set_route.pop())) 
        print("-------------------------------------------------------------------------------------\n\n")


# Recabando los datos del archivo csv

with open("synergy_logistics_database.csv") as csv_file:
    reader = csv.reader(csv_file)
    
    for line in reader:
        #Esta es la clave para identificar la ruta
        route = (line[2],line[3])       
        #Datos restantes del archivo
        info = [line[0],line[4],line[5],line[6],line[7],line[8],line[9]]    

        if line[2] != "origin" and line[3] != "destination":
            # Los datos se agrupan en 2 diccionarios diferentes, cuya clave es una tupla con los países origen - destino
            if line[1] == "Exports":
                dictionary = exports
            else:   
                dictionary = imports

            if route in dictionary:
                dictionary[route].append(info)
            else:
                dictionary[route] = [info]
            #---------------------------------------------------------------------------------------------------------------
            # Se genera un diccionario cuya clave es un conjunto de valores, el cual se utilizará en el punto 3
            # De esta forma si se tiene {país1, país2}, cualquier combinación que involucre esos 2 países se considera igual
            set_route = frozenset(route)
            
            if set_route in total_ops:
                total_ops[set_route] += int(line[9])
            else:
                total_ops[set_route] = int(line[9])

            #---------------------------------------------------------------------------------------------------------------

            transports.add(line[7])

            # Obtiene el valor total, tanto de importaciones como exportaciones
            total_value += int(line[9])


# Menú que despliega la información requerida

salir = False

while not salir:

    principal = False

    while not principal: 
        print("Elige una opción:")
        print("\n1)Rutas de importación y exportación \n2)Medio de transporte utilizado\n3)Valor total de importaciones y exportaciones\n4)Salir")

        entrada = input("\nIngresa tu elección:\n\n")

        if entrada == "1":
            obtener_top(ingresos_por_ruta(imports),"importación", True)
            obtener_top(ingresos_por_ruta(exports), "exportación", True)
        elif entrada == "2":
            imprimir_info_vehiculos(agrupar_por_vehiculo(imports,1),agrupar_por_vehiculo(exports,1))
        elif entrada == "3":
            valor_paises(total_ops)
        elif entrada == "4":
            salir = True
            principal = True
        else:
            print("Elige una opción válida")
