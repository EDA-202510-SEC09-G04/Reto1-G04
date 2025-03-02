import time
import os
import csv
import sys

sys.path.append(os.path.join(os.path.dirname(os.path.abspath(__file__)), '..'))

from DataStructures.List import array_list as lt
from DataStructures.Queue import queue as q
from DataStructures.Stack import stack as st 


data_dir = os.path.dirname(os.path.realpath('__file__')) + '/Data/'

print(data_dir)


def new_logic():
    """
    Crea el catalogo para almacenar las estructuras de datos
    """
    #TODO: Llama a las funciónes de creación de las estructuras de datos
    
    
    nueva_lista = lt.new_list()
    return nueva_lista
    



# Funciones para la carga de datos

def load_data(catalog,filename):
    """
    Carga los datos del reto
    """
    # TODO: Realizar la carga de datos
    
    
    files = data_dir + 'agricultural-20.csv'
    input_file = open(files, newline='',encoding='utf-8')
    
    reader = csv.reader(input_file)
    
    for row in reader:
        
        lt.add_last(catalog,row)
        
        
        
    

# Funciones de consulta sobre el catálogo


catalogo = new_logic()

load_data(catalogo)


print(catalogo)




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


def req_3(catalog):
    """
    Retorna el resultado del requerimiento 3
    """
    # TODO: Modificar el requerimiento 3
    pass


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


def req_7(catalog):
    """
    Retorna el resultado del requerimiento 7
    """
    # TODO: Modificar el requerimiento 7
    pass


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
