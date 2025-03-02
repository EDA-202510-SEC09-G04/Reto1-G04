import sys
import App.logic as logic
from tabulate import tabulate


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
    registros, size, menor, mayor, primeros, ultimos, headers = logic.load_data(control)
    return registros, size, menor, mayor, primeros, ultimos, headers

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
    pass


def print_req_2(control):
    """
        Función que imprime la solución del Requerimiento 2 en consola
    """
    # TODO: Imprimir el resultado del requerimiento 2
    pass


def print_req_3(control, departamento, inicial, final):
    """
        Función que imprime la solución del Requerimiento 3 en consola
    """
    res, census, survey = logic.req_3(control, departamento, inicial, final)
    headers = ['source','year_collection','load_time','freq_collection','commodity','unit_measurement']
    size = res['size']
    elements = res['elements'][:size]
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
    categoria = input('Ingrese la categoría que quiere consultar: ')
    anio_inicial = int(input('Ingrese el año inicial de búsqueda: '))
    anio_final = int(input('Ingrese el año final de búsqueda: '))
    
    respuestas,census_contador, survey_contador, tiempo_total = logic.req_4(control, categoria, anio_inicial, anio_final)
    encabezados = ['source', 'year_collection', 'load_time', 'freq_collection', 'state_name', 'unit_measurement', 'commodity']
    size = respuestas['size']
    elementos = respuestas['elements'][:size]
    print(f"\nTiempo de ejecución: {tiempo_total:.6f} milisegundos")
    print(f"Total registros encontrados: {size}")
    print(f"Total registros encontrados con fuente CENSUS: {census_contador}")
    print(f"Total registros encontrados con fuente SURVEY: {survey_contador}")
    
    if size == 0:
        print('No se encontraron registros para esos parámetros. Intente de nuevo.')
    else:
        if size > 20:
            head, tail = logic.head_y_tail(respuestas)
            print("\nPrimeros 5 registros:")
            print(format_table(head, encabezados, max_col_width=12))

            print("\nÚltimos 5 registros:")
            print(format_table(tail, encabezados, max_col_width=12))
        else:
            print(format_table(elementos, encabezados, max_col_width=12))

def print_req_5(control):
    """
        Función que imprime la solución del Requerimiento 5 en consola
    """
    # TODO: Imprimir el resultado del requerimiento 5
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


def print_req_6(control):
    """
        Función que imprime la solución del Requerimiento 6 en consola
    """
    # TODO: Imprimir el resultado del requerimiento 6
    pass


def print_req_7(control, departamento, inicial, final):
    """
        Función que imprime la solución del Requerimiento 7 en consola
    """
    
    registros_total, min_anio, min_valor, min_regtotal, min_regval, min_reginval, minsur, mincen, max_anio, max_valor, max_regtotal, max_regval, max_reginval, maxsur, maxcen = logic.req_7(control, departamento, inicial, final)
    if min_anio == max_anio:
        print('El menor y el mayor periodo de tiempo son el mismo.')
    
    print('Tiempo de ejecución: \n')
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
    total_departamentos, total_tiempo, total_registros, departamentos, menor_anio_rec, mayor_anio_rec, mayor_estado, mayor_diferencia = logic.req_8(control)
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
            registros, size, menor, mayor, primeros, ultimos, headers = load_data(control)
            
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
            print_req_6(control)

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
