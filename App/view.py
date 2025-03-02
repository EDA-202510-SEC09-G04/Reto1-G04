import sys
import App.logic as logic
from tabulate import tabulate
import time


def new_logic():
    """
        Se crea una instancia del controlador
    """
    control = logic.new_logic()
    return control

def format_table(data, headers, max_col_width=15):
    """Funcion de formateo de la tabla"""
    formatted_data = [
        [str(row[col])[:max_col_width] + ("..." if len(str(row[col])) > max_col_width else "") for col in headers]
        for row in data
    ]

    return tabulate(formatted_data, headers=headers, tablefmt="grid")

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

def print_menu():
    print("Bienvenido")
    print("1- Cargar información")
    print("2- Ejecutar Requerimiento 1")
    print("3- Ejecutar Requerimiento 2")
    print("4- Ejecutar Requerimiento 3")
    print("5- Ejecutar Requerimiento 4")
    print("6- Ejecutar Requerimiento 5")
    print("7- Ejecutar Requerimiento 6")
    print("8- Ejecutar Requerimiento 7")
    print("9- Ejecutar Requerimiento 8 (Bono)")
    print("0- Salir")

def load_data(control):
    """
    Carga los datos
    """
    registros, size, menor, mayor, primeros, ultimos, headers, tiempo_total = logic.load_data(control)
    return registros, size, menor, mayor, primeros, ultimos, headers, tiempo_total

def print_data(control, id):
    """
        Función que imprime un dato dado su ID
    """
    #TODO: Realizar la función para imprimir un elemento
    pass

def print_req_1(control):
    """
        Función que imprime la solución del Requerimiento 1 en consola
    """
    # TODO: Imprimir el resultado del requerimiento 1
    anio_interes = int(input("Ingrese el año de interés para buscar el último registro: "))

    registro, execution_time = logic.req_1(control, anio_interes)

    print(f"\nTiempo de ejecución: {execution_time:.6f} milisegundos")

    if registro:
        print("\nÚltimo registro recopilado en el año", anio_interes)
        print(f"Año de recolección: {registro['year_collection']}")
        print(f"Fecha de carga: {registro['load_time']}")
        print(f"Tipo de fuente: {registro['source']}")
        print(f"Frecuencia de recolección: {registro['freq_collection']}")
        print(f"Nombre del departamento: {registro['state_name']}")
        print(f"Tipo de producto: {registro['commodity']}")
        print(f"Unidad de medición: {registro['unit_measurement']}")
        print(f"Valor de la medición: {registro['value']}")
    else:
        print(f"No se encontraron registros para el año {anio_interes}.")


def print_req_2(control):
    """
        Función que imprime la solución del Requerimiento 2 en consola
    """
    # TODO: Imprimir el resultado del requerimiento 2
    departamento = input('Ingrese el nombre del departamento a filtrar: ')

    tiempo_total, respuesta = logic.req_2(control, departamento)

    if respuesta:
        print(f"\nTiempo de ejecución: {tiempo_total:.6f} milisegundos")
        print(f"Último registro cargado en {departamento}:")
        print(f"Año de recolección: {respuesta['year_collection']}")
        print(f"Fecha de carga: {respuesta['load_time']}")
        print(f"Tipo de fuente: {respuesta['source']}")
        print(f"Frecuencia de recolección: {respuesta['freq_collection']}")
        print(f"Nombre del departamento: {respuesta['state_name']}")
        print(f"Tipo de producto: {respuesta['commodity']}")
        print(f"Unidad de medición: {respuesta['unit_measurement']}")
        print(f"Valor de la medición: {respuesta['value']}")
    else:
        print(f"No se encontraron registros para el departamento {departamento}.")


def print_req_3(control, departamento, inicial, final):
    """
        Función que imprime la solución del Requerimiento 3 en consola
    """
    res, census, survey, tiempo_total = logic.req_3(control, departamento, inicial, final)
    headers = ['source','year_collection','load_time','freq_collection','commodity','unit_measurement']
    size = res['size']
    elements = res['elements'][:size]
    print(f"\nTiempo de ejecución: {tiempo_total:.6f} milisegundos")

    if size == 0:
        print('No se encontraron registros para esos parámetros. Intente de nuevo.')
    else:
        if res['size'] > 20:
            head, tail = logic.head_y_tail(res)
            print("\nPrimeros 5 registros:")
            print(format_table(head,headers,max_col_width=12))

            print("\nÚltimos 5 registros:")
            print(format_table(tail,headers, max_col_width=12))
        else:
            print(format_table(elements, headers, max_col_width=12))
        print('Total registros encontrados: ' + str(size))
        print('Total registros encontrados con fuente census: ' + str(census))
        print('Total registros encontrados con fuente survey: ' + str(survey))
        
        
def print_req_4(control):
    """
        Función que imprime la solución del Requerimiento 4 en consola
    """
    # TODO: Imprimir el resultado del requerimiento 4
    producto = input("Ingrese el tipo de producto a filtrar (ej. 'HOGS', 'SHEEP'): ")
    anio_inicial = int(input("Ingrese el año inicial de búsqueda: "))
    anio_final = int(input("Ingrese el año final de búsqueda: "))

    execution_time, resultado = logic.req_4(control, producto, anio_inicial, anio_final)

    registros, total_registros, survey_count, census_count = resultado
    headers = ['source', 'year_collection', 'load_time', 'freq_collection', 'state_name', 'unit_measurement']

    print(f"\nTiempo de ejecución: {execution_time:.6f} milisegundos")
    print(f"Total registros encontrados: {total_registros}")
    print(f"Total registros encontrados con fuente CENSUS: {census_count}")
    print(f"Total registros encontrados con fuente SURVEY: {survey_count}")

    if total_registros == 0:
        print("No se encontraron registros para esos parámetros.")
    else:
        if total_registros > 20:
            head, tail = logic.head_y_tail({'elements': registros, 'size': total_registros})
            print("\nPrimeros 5 registros:")
            print(format_table(head, headers, max_col_width=12))

            print("\nÚltimos 5 registros:")
            print(format_table(tail, headers, max_col_width=12))
        else:
            print(format_table(registros, headers, max_col_width=12))

    

def print_req_5(control):
    """
        Función que imprime la solución del Requerimiento 5 en consola
    """
    
    categoria = input('Ingrese la categoría estadística a filtrar (ej. "INVENTORY", "SALES"): ')
    anio_inicial = int(input('Ingrese el año inicial de búsqueda: '))
    anio_final = int(input('Ingrese el año final de búsqueda: '))

    respuestas, census_contador, survey_contador, tiempo_total = logic.req_5(control, categoria, anio_inicial, anio_final)
    encabezados = ['source', 'year_collection', 'load_time', 'freq_collection', 'state_name', 'unit_measurement', 'commodity']
    size = respuestas['size']
    elements = respuestas['elements'][:size]

    print(f"\nTiempo de ejecución: {tiempo_total:.6f} milisegundos")
    print(f"Total registros encontrados: {size}")
    print(f"Total registros encontrados con fuente CENSUS: {census_contador}")
    print(f"Total registros encontrados con fuente SURVEY: {survey_contador}")

    if size == 0:
        print('No se encontraron registros para esos parámetros.')
    else:
        if size > 20:
            head, tail = logic.head_y_tail(respuestas)
            print("\nPrimeros 5 registros:")
            print(format_table(head, encabezados, max_col_width=12))

            print("\nÚltimos 5 registros:")
            print(format_table(tail, encabezados, max_col_width=12))
        else:
            print(format_table(elements, encabezados, max_col_width=12))


def print_req_6(control, departamento, inicial, final):
    """
        Función que imprime la solución del Requerimiento 6 en consola
    """
    respuestas, census, survey, tiempo_total = logic.req_6(control, departamento, inicial, final)
    size = respuestas['size']
    elements = respuestas['elements'][:size]
    encabezados = ['source', 'year_collection', 'load_time', 'freq_collection','state_name', 'unit_measurement', 'commodity']

    print(f"\nTiempo de ejecución: {tiempo_total:.6f} milisegundos")
    print(f"Total registros encontrados: {size}")
    print(f"Total registros encontrados con fuente CENSUS: {census}")
    print(f"Total registros encontrados con fuente SURVEY: {survey}")

    if size == 0:
        print('No se encontraron registros para esos parámetros.')
    else:
        if size > 20:
            head, tail = logic.head_y_tail(respuestas)
            print("\nPrimeros 5 registros:")
            print(format_table(head, encabezados, max_col_width=12))

            print("\nÚltimos 5 registros:")
            print(format_table(tail, encabezados, max_col_width=12))
        else:
            print(format_table(elements, encabezados, max_col_width=12))

def print_req_7(control, departamento, inicial, final):
    """
        Función que imprime la solución del Requerimiento 7 en consola
    """
    
    registros_total, min_anio, min_valor, min_regtotal, min_regval, min_reginval, minsur, mincen, max_anio, max_valor, max_regtotal, max_regval, max_reginval, maxsur, maxcen, tiempo_total = logic.req_7(control, departamento, inicial, final)
    if min_anio == max_anio:
        print('El menor y el mayor periodo de tiempo son el mismo.')
    
    print(f"\nTiempo de ejecución: {tiempo_total:.6f} milisegundos")
    print('Número total de registros  que cumplieron el filtro: ' + str(registros_total))
    
    min_data = [
    ["Año", min_anio],
    ["Valor ingresos", "{:,.0f}".format(min_valor)],
    ["Registros en periodo", min_regtotal],
    ["Registros válidos", min_regval],
    ["Registros inválidos", min_reginval],
    ["# Census", mincen],
    ["# Survey", minsur]
    ]
    
    max_data = [
    ["Año", max_anio],
    ["Valor ingresos", "{:,.0f}".format(max_valor)],
    ["Registros en periodo", max_regtotal],
    ["Registros válidos", max_regval],
    ["Registros inválidos", max_reginval],
    ["# Census", maxcen],
    ["# Survey", maxsur]
]

    print("\nPERIODO DE MENOR INGRESO")
    print(tabulate(min_data, tablefmt="grid"))

    print("\n PERIODO DE MAYOR INGRESO")
    print(tabulate(max_data, tablefmt="grid"))
    
    
def print_req_8(control):
    """
        Función que imprime la solución del Requerimiento 8 en consola
    """
    total_departamentos, total_tiempo, total_registros, departamentos, menor_anio_rec, mayor_anio_rec, mayor_estado, mayor_diferencia, tiempo_total = logic.req_8(control)
    print(f"\nTiempo de ejecución: {tiempo_total:.6f} milisegundos")
    general = [
        ['Total departamentos', total_departamentos],
        ['Total registros', total_registros],
        ['Tiempo promedio total', total_tiempo],
        ['Menor año recopilación', menor_anio_rec],
        ['Mayor año recopilación', mayor_anio_rec],
    ]
    
    dep_mayor = [
        ['Nombre', mayor_estado],
        ['Tiempo promedio', mayor_diferencia],
        ['Menor año recopilación', departamentos[mayor_estado]['anio_menor']],
        ['Mayor año recopilación', departamentos[mayor_estado]['anio_mayor']],
        ['Tiempo dif menor', departamentos[mayor_estado]['tiempo_menor']],
        ['Tiempo dif mayor', departamentos[mayor_estado]['tiempo_mayor']],
        ['Survey', departamentos[mayor_estado]['survey']],
        ['Census', departamentos[mayor_estado]['census']]
    ]
    
    data = [
        [state, data["tiempo_promedio"], data["registros"], data["anio_menor"], data["anio_mayor"], 
        data["tiempo_menor"], data["tiempo_mayor"], data["survey"], data["census"]] 
        for state, data in departamentos.items()
    ]
    headers = ["Departamento", "Tiempo Promedio", "# Registros", "Año Menor", "Año Mayor", "Tiempo Menor", "Tiempo Mayor", "# Survey", "# Census"]
    max_col_width = 10

    formateado = [
        [str(row[col])[:max_col_width] + ("..." if len(str(row[col])) > max_col_width else "") for col in range(len(headers))]
        for row in data
    ]
    print("\nDATOS GENERALES")
    print(tabulate(general, tablefmt="grid"))
    
    print("\nDATOS DEPARTAMENTO MAYOR TIEMPO")
    print(tabulate(dep_mayor, tablefmt="grid"))
    
    print("\nPROMEDIO DE CADA DEPARTAMENTO")
    print(tabulate(formateado, headers=headers, tablefmt="grid"))

# Se crea la lógica asociado a la vista
control = new_logic()

# main del ejercicio
def main():
    """
    Menu principal
    """
    working = True
    #ciclo del menu
    while working:
        print_menu()
        inputs = input('Seleccione una opción para continuar\n')
        if int(inputs) == 1:
            print("Cargando información de los archivos ....\n")
            
            registros, size, menor, mayor, primeros, ultimos, headers, tiempo_total = load_data(control)
            
            print(f"\nTiempo de ejecución: {tiempo_total:.6f} milisegundos")
            
            print(f"Total registros cargados: {size}")
            
            print(f"Menor año de recolección de registro: {menor}")
            print(f"Mayor año de recolección de registro: {mayor}")
            
            print("\nPrimeros 5 registros:")
            print(format_table(primeros,headers,max_col_width=12))

            print("\nÚltimos 5 registros:")
            print(format_table(ultimos,headers, max_col_width=12))
            
        elif int(inputs) == 2:
            print_req_1(control)

        elif int(inputs) == 3:
            print_req_2()

        elif int(inputs) == 4:
            departamento = input('Ingrese el departamento que quiere consultar: ')
            inicial = int(input('Ingrese el año inicial de búsqueda: '))
            final = int(input('Ingrese el año final de búsqueda: '))
            print_req_3(control, departamento, inicial, final)

        elif int(inputs) == 5:
            print_req_4(control)

        elif int(inputs) == 6:
            print_req_5(control)

        elif int(inputs) == 7:
            departamento = input('Ingrese el departamento que quiere consultar: ')
            inicial = input('Ingrese la fecha inicial de búsqueda (%Y-%m-%d)": ')
            final = input('Ingrese la fecha final de búsqueda (%Y-%m-%d): ')
            print_req_6(control, departamento, inicial, final)

        elif int(inputs) == 8:
            departamento = input('Ingrese el departamento que quiere consultar: ')
            inicial = int(input('Ingrese el año inicial de búsqueda: '))
            final = int(input('Ingrese el año final de búsqueda: '))
            print_req_7(control, departamento, inicial, final)
            

        elif int(inputs) == 9:
            print_req_8(control)

        elif int(inputs) == 0:
            working = False
            print("\nGracias por utilizar el programa") 
        else:
            print("Opción errónea, vuelva a elegir.\n")
    sys.exit(0)
