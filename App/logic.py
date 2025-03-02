import time
import os
import csv
import sys
import pprint
from tabulate import tabulate

sys.path.append(os.path.join(os.path.dirname(os.path.abspath(__file__)), '..'))

from DataStructures.List import array_list as lt
from DataStructures.Queue import queue as q
from DataStructures.Stack import stack as st 


data_dir = os.path.dirname(os.path.realpath('__file__')) + '/Data/'



""" #plantilla para tomar tiempo
start_time = time.time()
#funcion llamado
end_time = time.time() 
execution_time = end_time - start_time 
print(f"\nTiempo de ejecución: {execution_time:.6f} segundos")
 """

def new_logic():
    """
    Crea el catalogo para almacenar las estructuras de datos
    """
    
    catalog = {
        'registros' : None
    }
    catalog['registros'] = lt.new_list()
    return catalog
    
    
# Funciones para la carga de datos

def load_data(catalog):
    """
    Carga los datos del reto
    """
    files = data_dir + 'agricultural-20.csv'
    
    input_file = csv.DictReader(open(files, encoding='utf-8'))
    for row in input_file:
        lt.add_last(catalog['registros'], row)
    
    headers = ['year_collection','load_time','state_name','source','unit_measurement','value']
    size = lt.size(catalog['registros'])
    primeros, ultimos = head_y_tail(catalog['registros'])
    menor, mayor = menor_mayor(catalog)
    registros = catalog['registros']['elements']
    
    return registros, size, menor, mayor, primeros, ultimos, headers
        
       
def head_y_tail(registros):
    head = registros['elements'][:5]
    size = registros['size'] 
    tail = registros['elements'][size - 5:size]
    return head, tail

def menor_mayor(catalog):
    size = catalog['registros']['size']
    elementos = catalog['registros']['elements']
    a = [int(elementos[i]["year_collection"]) for i in range(size) if "year_collection" in elementos[i]]
    return min(a),max(a)
    
#ayuda a ver si un string es un numero
def es_numero(value):
    try:
        float(value.replace(',', ''))
        return True
    except ValueError:
        return False


def get_data(catalog, id):
    """
    Retorna un dato por su ID.
    """
    #TODO: Consulta en las Llamar la función del modelo para obtener un dato
    pass


def req_1(catalog):
    """
    Retorna el resultado del requerimiento 1
    """
    # TODO: Modificar el requerimiento 1
    pass


def req_2(catalog):
    """
    Retorna el resultado del requerimiento 2
    """
    # TODO: Modificar el requerimiento 2
    pass


def req_3(catalog, departamento, inicial, final):
    """
    Listar los registros recopilados según el nombre del departamento para un periodo de tiempo de interés 
    """
    registros = catalog['registros']['elements']
    size = catalog['registros']['size']
    respuestas = lt.new_list()
    census = 0
    survey = 0
    i = 0
    while i < size and registros[i] != None:
        
        if registros[i]['state_name'] == departamento and int(registros[i]['year_collection']) >= inicial and int(registros[i]['year_collection']) <= final:
            lt.add_last(respuestas, registros[i])
            if registros[i]['source'] == 'CENSUS':
                census +=1
            if registros[i]['source'] == 'SURVEY':
                survey +=1
            
        i += 1

    return respuestas, census, survey

def req_4(catalog):
    """
    Retorna el resultado del requerimiento 4
    """
    # TODO: Modificar el requerimiento 4
    pass


def req_5(catalog):
    """
    Retorna el resultado del requerimiento 5
    """
    # TODO: Modificar el requerimiento 5
    pass

def req_6(catalog):
    """
    Retorna el resultado del requerimiento 6
    """
    # TODO: Modificar el requerimiento 6
    pass


def req_7(catalog, departamento, inicial, final):
    """
    Retorna el resultado del requerimiento 7
    """
    registros = catalog['registros']['elements']
    size = catalog['registros']['size']
    anios = {}
    i = 0
    registros_total = 0
    
    min_anio = None
    max_anio = None
    min_valor = float('inf')
    max_valor = float('-inf')
    
    while i < size and registros[i] != None:
        if registros[i]['state_name'] == departamento and int(registros[i]['year_collection']) >= inicial and int(registros[i]['year_collection']) <= final and registros[i]['unit_measurement'] == '$':
            #cumple con el filtro principal entonces se agrega a total registros
            registros_total += 1
            anio = registros[i]['year_collection']
                
            if anio not in anios:
                    anios[anio] = {
                        'regtotal': 0,
                        'regvalidos':0,
                        'reginvalidos': 0,
                        'survey': 0,
                        'census': 0,
                        'valor':0
                    }
            #verificar si es census o survey y agregar al correspondiente año
            if registros[i]['source'] == 'CENSUS':
                anios[anio]['census'] +=1 
                
            if registros[i]['source'] == 'SURVEY':
                anios[anio]['survey'] +=1
            #como cumple el filtro añadir a numero de registros por año que cumple el filtro
            
            anios[anio]['regtotal'] += 1
            
            #verificar si el valor de value es un numero y no otra cosa
            if es_numero((registros[i]['value'])) == True:   
                anios[anio]['valor'] += float(registros[i]['value'].replace(',', ''))
                anios[anio]['regvalidos'] += 1
                
                if anios[anio]['valor'] < min_valor:
                    min_valor = anios[anio]['valor']
                    min_anio = anio
                    
                if anios[anio]['valor'] > max_valor:
                    max_valor = anios[anio]['valor']
                    max_anio = anio
                
            elif es_numero((registros[i]['value'])) == False:          
                anios[anio]['reginvalidos'] += 1
                
        i += 1

    min_regtotal, min_regval, min_reginval, minsur, mincen = anios[min_anio]['regtotal'], anios[min_anio]['regvalidos'], anios[min_anio]['reginvalidos'], anios[min_anio]['survey'], anios[min_anio]['census']
    max_regtotal, max_regval, max_reginval, maxsur, maxcen = anios[max_anio]['regtotal'], anios[max_anio]['regvalidos'], anios[max_anio]['reginvalidos'], anios[max_anio]['survey'], anios[max_anio]['census']

    return registros_total, min_anio, min_valor, min_regtotal, min_regval, min_reginval, minsur, mincen, max_anio, max_valor, max_regtotal, max_regval, max_reginval, maxsur, maxcen

def req_8(catalog):
    """
    Retorna el resultado del requerimiento 8
    """
    # TODO: Modificar el requerimiento 8
    pass


# Funciones para medir tiempos de ejecucion

def get_time():
    """
    devuelve el instante tiempo de procesamiento en milisegundos
    """
    return float(time.perf_counter()*1000)


def delta_time(start, end):
    """
    devuelve la diferencia entre tiempos de procesamiento muestreados
    """
    elapsed = float(end - start)
    return elapsed
