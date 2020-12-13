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
import config
from App import controller
from DISClib.ADT import stack
import timeit
assert config

"""
La vista se encarga de la interacción con el usuario.
Presenta el menu de opciones  y  por cada seleccion
hace la solicitud al controlador para ejecutar la
operación seleccionada.
"""

# ___________________________________________________
#  Variables
# ___________________________________________________

Archivo="taxi-trips-wrvz-psew-subset-small.csv"

# ___________________________________________________
#  Menu principal
# ___________________________________________________

def printMenu():
    print("\n")
    print("*******************************************")
    print("Bienvenido.")
    print("1- Inicializar Analizador.")
    print("2- Cargar información de Taxis.")
    print("3- Top taxis y Top sevicios.")
    print("4- Puntos.")
    print("0- Salir")
    print("*******************************************")

"""
Menu principal
"""

while True:
    printMenu()
    inputs = input('Seleccione una opción para continuar\n>')

    if int(inputs[0]) == 1:
        print("\nInicializando....")
        rutas = controller.init()

    elif int(inputs[0]) == 2:
        print("\nCargando información de viajes ....")
        controller.loadData(rutas,Archivo)

    elif int(inputs[0]) == 3:
        M=int(input("Digite el numero de resultados(Top taxis): "))
        N=int(input("Digite el numero de resultados(Top servicios): "))
        total=controller.basic_info(rutas,M,N)
        print("Hay ",total["taxis"]," taxis registrados.")
        print("Hay", total["comps"], "compañias con taxi(s).")

        print("Las",M,"compañias con más taxis son: ")
        for res in total["top_tax"]:
            o,n=res
            print("     *",n," con ",o," taxis")
        print("Las",M,"compañias con más servicios son: ")
        for res in total["top_sev"]:
            o,n=res
            print("     *",n," con ",o, "servicios")

    else:
        sys.exit(0)
sys.exit(0)
