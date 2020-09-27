def ingresos_por_ruta(routes):
    result = {} 
    for key in routes.keys():
        for data in routes[key]:
            if key in result:
                result[key][1] += int(data[6])
                result[key][0] += 1
            else:
                result[key] = [0,int(data[6])]        
    return {key:result[key][1]/result[key][0] for key in routes.keys()}

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
