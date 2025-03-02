import time
import os
import csv
import sys
import pprint
from tabulate import tabulate
from datetime import datetime

sys.path.append(os.path.join(os.path.dirname(os.path.abspath(__file__)), '..'))

from DataStructures.List import array_list as lt
from DataStructures.Queue import queue as q
from DataStructures.Stack import stack as st 


data_dir = os.path.dirname(os.path.realpath('__file__')) + '/Data/'



# Funciones para calcular el tiempo

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
    tiempo_inicial = get_time()
    files = data_dir + 'agricultural-20.csv'
    
    input_file = csv.DictReader(open(files, encoding='utf-8'))
    for row in input_file:
        lt.add_last(catalog['registros'], row)
    
    headers = ['year_collection','load_time','state_name','source','unit_measurement','value']
    size = lt.size(catalog['registros'])
    primeros, ultimos = head_y_tail(catalog['registros'])
    menor, mayor = menor_mayor(catalog)
    registros = catalog['registros']['elements']
    
    tiempo_final = get_time()
    tiempo_total = delta_time(tiempo_inicial, tiempo_final)
    
    return registros, size, menor, mayor, primeros, ultimos, headers, tiempo_total
        
       
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



def ultimo_registro(catalogo,anio):
    
    elementos = catalogo['registros']['elements']
    size = catalogo['registros']['size']
    elemento_ultimo = None
    
    datos = 0
    i = 0
    
    if size > 0 :
        
        mayor = datetime.strptime(elementos[0]['load_time'],'%Y-%m-%d %H:%M:%S')
    
    while  i < size and elementos[i] is not None:
        
        tiempo_carga = datetime.strptime(elementos[i]['load_time'],'%Y-%m-%d %H:%M:%S')
        index_el = elementos[i]
        
        if index_el is not  None and 'year_collection' in index_el:
            
            
            year = int(index_el['year_collection'])
            
            if year == anio and mayor < tiempo_carga:
                
                elemento_ultimo = elementos[i]
                
            elif year == anio:
                 
                 datos += 1
                 
                 
                    
        i += 1
        
        
    return elemento_ultimo, datos
    
    



def req_1(catalog,anio_interes):
    """
    Retorna el resultado del requerimiento 1
    """
    
   
    
    inicio = get_time()
    registro, datos = ultimo_registro(catalog,anio_interes)
    fin = get_time()
    dif = fin - inicio
    
    
    return dif , registro, datos
    
    

catalogo = new_logic()

load_data(catalogo)



    
def registro_departamento(catalogo,dep):
    
    elementos = catalogo['registros']['elements']
    size = catalogo['registros']['size']
    i = 0
    mayor = datetime.strptime(elementos[0]['load_time'],'%Y-%m-%d %H:%M:%S')
    num_datos = 0
    ultimo_registro = None
    
    while i < size and elementos[i] is not None:
        
        tiempo_carga = datetime.strptime(elementos[i]['load_time'],'%Y-%m-%d %H:%M:%S')
        
        departamento = elementos[i]['state_name']
        
        if mayor < tiempo_carga and departamento == dep :
            
            mayor = tiempo_carga
            ultimo_registro= elementos[i]
            
        
        if departamento == dep:
            
            num_datos += 1
            
        
        
        i += 1
        
        
    return ultimo_registro, num_datos
            
            
            
            
    
    


def req_2(catalog,dep):
    """
    Retorna el resultado del requerimiento 2
    """
    inicio = get_time()
    ultimo_registro, num_datos= registro_departamento(catalog,dep)
    final = get_time()
    
    dif = final -inicio
    
    
    return dif, ultimo_registro, num_datos




def req_3(catalog, departamento, inicial, final):
    """
    Listar los registros recopilados según el nombre del departamento para un periodo de tiempo de interés 
    """
    tiempo_inicial = get_time()
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
    tiempo_final = get_time()
    tiempo_total = delta_time(tiempo_inicial, tiempo_final)

    return respuestas, census, survey, tiempo_total


def registros_producto(catalogo,prod,anio_inicial,anio_final):
    
    
     elementos = catalogo['registros']['elements']
     size = catalogo['registros']['size']
     
     elementos_list = lt.new_list()
     census = 0
     survey = 0 
     i = 0
     
     while i < size and elementos[i] != None:
         
        index_el = elementos[i]
        index_el_year = elementos[i]['year_collection']
        index_el_prod = elementos[i]['commodity']
        index_el_org = elementos[i]['source']
        
        if index_el_prod == prod and  anio_inicial < int(index_el_year) < anio_final:
            
             if index_el_org == 'SURVEY':
                 
                 survey += 1
                 
             if index_el_org == 'CENSUS':
                 
                 census += 1
                 
            
             new_resiter = {
                 'source' : index_el_org,
                 'year_collection': index_el_year,
                 'load_time': index_el['load_time'],
                 'freq_collection': index_el['freq_collection'],
                 'state_name':index_el['state_name'],
                 'unit_measurement':index_el['unit_measurement']
                 
             }
                 
             lt.add_last(elementos_list,new_resiter)
             
        i += 1
    
    
    

         
     return elementos_list, lt.size(elementos_list), survey,census
            
            






def req_4(catalog,prod,anio_inicial,anio_final):
    """
    Retorna el resultado del requerimiento 4
    """
    inicio = get_time()
    lista_el, tamanio, survey, census = registros_producto(catalog,prod,anio_inicial,anio_final)
    final = get_time()
    dif = final - inicio
    
    return dif, lista_el,tamanio,survey,census






def req_5(catalog,categoria, anio_inicial, anio_final):
    """
    Retorna el resultado del requerimiento 5
    """
    tiempo_inicial = get_time()
    
    registros = catalog['registros']['elements']
    size = catalog['registros']['size']
    respuestas = lt.new_list()
    census_contador = 0
    survey_contador = 0

    
    i = 0
    while i < size and registros[i] != None:
        registro = registros[i]
        anio = int(registro['year_collection'])
        
        if registro["statical_category"] == categoria and anio >= anio_inicial and anio <= anio_final:
            lt.add_last(respuestas, registro)
            if registro['source'] == 'CENSUS':
                census_contador += 1
            elif registro['source'] == 'SURVEY':
                survey_contador += 1
        i +=1
                
    tiempo_final = get_time()
    tiempo_total = delta_time(tiempo_inicial, tiempo_final)
    
    return respuestas, census_contador, survey_contador, tiempo_total

def req_6(catalog, departamento, inicial, final):
    """
    Retorna el resultado del requerimiento 6
    """
    tiempo_inicial = get_time()
    
    registros = catalog['registros']['elements']
    size = catalog['registros']['size']
    
    respuestas = lt.new_list()
    i = 0
    census = 0
    survey = 0
    
    inicial = inicial.strip()
    final = final.strip()
    
    while i < size and registros[i] != None:
        
        fecha = registros[i]['load_time'][:10]
     
        if registros[i]['state_name'] == departamento and fecha < final and fecha > inicial:
            
            lt.add_last(respuestas, registros[i])
            if registros[i]['source'] == 'CENSUS':
                census +=1 
            
            if registros[i]['source'] == 'SURVEY':
                survey+=1
        
        i+=1
    tiempo_final = get_time()
    tiempo_total = delta_time(tiempo_inicial, tiempo_final)

    return respuestas, census, survey, tiempo_total

def req_7(catalog, departamento, inicial, final):
    """
    Retorna el resultado del requerimiento 7
    """
    tiempo_inicial = get_time()
    
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
    tiempo_final = get_time()
    tiempo_total = delta_time(tiempo_inicial, tiempo_final)
    return registros_total, min_anio, min_valor, min_regtotal, min_regval, min_reginval, minsur, mincen, max_anio, max_valor, max_regtotal, max_regval, max_reginval, maxsur, maxcen, tiempo_total

def req_8(catalog):
    """
    Retorna el resultado del requerimiento 8
    """
    tiempo_inicial = get_time()
    registros = catalog['registros']['elements']
    size = catalog['registros']['size']
    
    i = 0
    
    total_departamentos = 0
    
    total_registros = 0
    total_tiempo = 0
    
    menor_anio_rec = 0
    mayor_anio_rec = 0
    
    mayor_diferencia= float('-inf')
    mayor_estado = None
    
    departamentos = {}
    
    while i < size and registros[i] != None:
        state = registros[i]['state_name']
        
        if state not in departamentos:
            total_departamentos += 1
            departamentos[state] = {
            'tiempo_promedio': 0,
            'registros': 0,
            'anio_menor': None,
            'anio_mayor':None,
            'tiempo_menor':None,
            'tiempo_mayor':None,
            'survey':0,
            'census':0
        }
        
        load_year =  int(registros[i]['load_time'][:4])
        collected_year = int(registros[i]['year_collection'])
        diferencia = load_year-collected_year
        
        
        departamentos[state]['registros'] += 1
        
        #handle el calculo del promedio tiempo del state
        departamentos[state]['tiempo_promedio'] += (diferencia - departamentos[state]['tiempo_promedio'])/departamentos[state]['registros']
        
        #handle el calculo del promedio tiempo de tooodos los states
        total_registros +=1
        total_tiempo += (diferencia - total_tiempo)/total_registros
        #handle comparacion de estado con mayor diferencia
        if departamentos[state]['tiempo_promedio'] > mayor_diferencia:
            mayor_diferencia = departamentos[state]['tiempo_promedio']
            mayor_estado = state
        
        #handle menor y mayor anio total
        menor_anio_rec = min(
            collected_year, menor_anio_rec or collected_year
        )
        mayor_anio_rec = max(
            collected_year, mayor_anio_rec or collected_year
        )
        
        #handle menor y mayor diferencia entre reco y carga de cada estado
        departamentos[state]['tiempo_menor'] = min(
            diferencia, departamentos[state]['tiempo_menor'] or diferencia
        )
        departamentos[state]['tiempo_mayor'] = max(
            diferencia, departamentos[state]['tiempo_mayor'] or diferencia
        )
        
        #handle año mayor y menor de recoleccion de cada estado
        departamentos[state]['anio_menor'] = min(
            collected_year, departamentos[state]['anio_menor'] or collected_year
        )
        departamentos[state]['anio_mayor'] = max(
            collected_year, departamentos[state]['anio_mayor'] or collected_year
        )
        #handle suveyr y census
        if registros[i]['source'] == 'CENSUS':
            departamentos[state]['census'] += 1 
        if registros[i]['source'] == 'SURVEY':
            departamentos[state]['survey'] += 1 
        
        i += 1
        
    tiempo_final = get_time()
    tiempo_total = delta_time(tiempo_inicial, tiempo_final)
    
    return total_departamentos, total_tiempo, total_registros ,departamentos, menor_anio_rec, mayor_anio_rec, mayor_estado, mayor_diferencia, tiempo_total
    
    
   


# Funciones para medir tiempos de ejecucion

