"""
 * Copyright 2020, Departamento de sistemas y Computación
 * Universidad de Los Andes
 *
 *
 * Desarrolado para el curso ISIS1225 - Estructuras de Datos y Algoritmos
 *
 *
 * This program is free software: you can redistribute it and/or modify
 * it under the terms of the GNU General Public License as published by
 * the Free Software Foundation, either version 3 of the License, or
 * (at your option) any later version.
 *
 * This program is distributed in the hope that it will be useful,
 * but WITHOUT ANY WARRANTY; without even the implied warranty of
 * MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
 * GNU General Public License for more details.
 *
 * You should have received a copy of the GNU General Public License
 * along with this program.  If not, see <http://www.gnu.org/licenses/>.
 * Contribución de:
 *
 * Dario Correal
 *
 """


import sys
import threading
from App import logic
from DataStructures.List import array_list as al

"""
La vista se encarga de la interacción con el usuario.
Presenta el menu de opciones  y  por cada seleccion
hace la solicitud al controlador para ejecutar la
operación seleccionada.
"""

# ___________________________________________________
#  Variables
# ___________________________________________________


servicefile = 'bus_routes_14000.csv'
stopsfile = 'bus_stops.csv'
initialStation = None

# ___________________________________________________
#  Menu principal
# ___________________________________________________


def print_menu():
    print("\n")
    print("*******************************************")
    print("Bienvenido")
    print("1- Cargar información de buses de singapur") # Clase 1: Implementar digraph básico
    print("2- Encontrar las paradas más concurridas") # Casa 1: Implementar digraph completo
    print("3- Encontrar una ruta entre dos paradas (DFS)") # Casa 1: Implementar funcionalidad dfs
    print("4- Encontrar una ruta entre dos paradas (BFS)") # Clase 2: Implementar funcionalidad bfs
    print("5- Encontrar la ruta mínima entre dos paradas") # Casa 2: Implementar dijkstra
    print("6- Mostrar en un mapa la ruta mínima entre dos paradas") # Trabajo Complementario: Mostrar ruta con folium
    print("0- Salir")
    print("*******************************************")


def option_one(cont):
    print("\nCargando información de transporte de singapur ....")
    logic.load_services(cont, servicefile, stopsfile)
    numedges = logic.total_connections(cont)
    numvertex = logic.total_stops(cont)
    print('Numero de vertices: ' + str(numvertex))
    print('Numero de arcos: ' + str(numedges))
    print('El limite de recursion actual: ' + str(sys.getrecursionlimit()))

def option_two(cont):
    # TODO: Imprimir los resultados de la opción 2
    paradas = logic.get_most_concurrent_stops(cont)
    print("\n------ OPCIÓN 2 ------")
    print("Las paradas más concurridas son:")
    for i in range(al.size(paradas)):
        parada = al.get_element(paradas, i)
        print(str(i + 1) + ". '" + parada['parada'] + "': " + str(parada['grado']) + " conexiones")

def option_three(cont):
    # TODO: Imprimir los resultados de la opción 3
    stop1 = input("Parada inicial (ej. 66009-100): ")
    stop2 = input("Parada destino (ej. 14151-10): ")
    ruta = logic.get_route_between_stops_dfs(cont, stop1, stop2)
    print("\n----- OPCIÓN 3 (DFS) ----")
    print("Parada inicial: '" + stop1 + "'")
    print("Parada destino: '" + stop2 + "'")
    if ruta is None:
        print("No existe una ruta entre las dos paradas")
    else:
        print_ruta(ruta)


def print_ruta(ruta):
    primera = al.get_element(ruta, 0)
    bus = primera.split('-')[1]
    print("\n--- Tomar bus '" + bus + "' desde '" + primera + "' ---")
    linea = primera.split('-')[0]
    for i in range(1, al.size(ruta)):
        vertice = al.get_element(ruta, i)
        parada = vertice.split('-')[0]
        nuevo_bus = vertice.split('-')[1]
        if nuevo_bus != bus:
            print(linea + " ->")
            print("--- Cambiar a bus '" + nuevo_bus + "' en la parada '" + parada + "' ---")
            bus = nuevo_bus
            linea = parada
        else:
            linea = linea + " -> " + parada
    print(linea)

def option_four(cont):
    # TODO: Imprimir los resultados de la opción 4
    stop1 = input("Parada inicial (ej. 66009-100): ")
    stop2 = input("Parada destino (ej. 14151-10): ")
    ruta = logic.get_route_between_stops_bfs(cont, stop1, stop2)
    print("\n----- OPCIÓN 4 (BFS) ----")
    print("Parada inicial: '" + stop1 + "'")
    print("Parada destino: '" + stop2 + "'")
    if ruta is None:
        print("No existe una ruta entre las dos paradas")
    else:
        print_ruta(ruta)

def option_five(cont):
    # TODO: Imprimir los resultados de la opción 5
    stop1 = input("Parada inicial (ej. 66009-100): ")
    stop2 = input("Parada destino (ej. 14151-10): ")
    respuesta = logic.get_shortest_route_between_stops(cont, stop1, stop2)
    print("\n----- OPCIÓN 5 ----")
    print("Origen: '" + stop1 + "'")
    print("Destino: '" + stop2 + "'")
    if respuesta is None:
        print("No existe una ruta entre las dos paradas")
    else:
        print_ruta(respuesta['ruta'])
        print("Distancia total: " + str(round(respuesta['distancia'], 2)) + " km")

def option_six(cont):
    # (Opcional) TODO: Imprimir los resultados de la opción 6
    destino = input("Parada destino (ej. 14151-10): ")
    archivo = logic.show_calculated_shortest_route(cont, destino)
    print("\n----- OPCIÓN 6 ----")
    if archivo is None:
        print("Primero ejecute la opción 5, o no existe una ruta hasta esa parada")
    else:
        print("El mapa se guardó en el archivo: " + archivo)
        print("Ábralo con el navegador para ver la ruta")


"""
Menu principal
"""


def main():
    working = True
    while working:
        print_menu()
        inputs = input('Seleccione una opción para continuar\n>')

        if int(inputs[0]) == 1:
            print("\nInicializando....")
            cont = logic.new_analyzer()
            option_one(cont)
        elif int(inputs[0]) == 2:
            option_two(cont)
        elif int(inputs[0]) == 3:
            option_three(cont)
        elif int(inputs[0]) == 4:
            option_four(cont)
        elif int(inputs[0]) == 5:
            option_five(cont)
        elif int(inputs[0]) == 6:
            option_six(cont)
        else:
            working = False
            print("Saliendo...")
    sys.exit(0)


if __name__ == "__main__":
    threading.stack_size(67108864)  # 64MB stack
    sys.setrecursionlimit(2 ** 20)
    thread = threading.Thread(target=main)
    thread.start()
