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
import config
from DISClib.ADT.graph import gr
from DISClib.ADT import map as m
from DISClib.ADT import list as lt
from DISClib.ADT import minpq as mpq
from DISClib.DataStructures import listiterator as it
from DISClib.Algorithms.Graphs import scc
from DISClib.Algorithms.Graphs import dijsktra as djk
from DISClib.Utils import error as error
assert config

"""
En este archivo definimos los TADs que vamos a usar y las operaciones
de creacion y consulta sobre las estructuras de datos.
"""

# -----------------------------------------------------
#                       API
# -----------------------------------------------------

# Funciones para agregar informacion al grafo

def New_list():

    lista={"Compañias":None,"Servicios":None, "Puntos":None,"Info":None}
    lista['Compañias'] = mpq.newMinPQ(comparar_taxis)
    lista['Servicios'] = mpq.newMinPQ(comparar_taxis)
    lista['Puntos'] = mpq.newMinPQ(comparar_taxis)
    lista["Info"]={}
    return lista


def añadirdato(lista,viaje):
    if viaje["company"] in lista["Info"]:
        lista["Info"][viaje["company"]]["servs"] += 1

    elif viaje["company"] == None:
        if "Independent Owner" in lista["Info"]:
            lista["Info"]["Independent Owner"]["servs"] += 1
        else:
            lista["Info"]["Independent Owner"]={}
            lista["Info"]["Independent Owner"]["servs"] = 1
            lista["Info"]["Independent Owner"]["taxis"] = []
            lista["Info"]["Independent Owner"]["mills"] = 0
            lista["Info"]["Independent Owner"]["money"] = 0
            lista["Info"]["Independent Owner"]["taxis_num"] = 0

    else:
        lista["Info"][viaje["company"]]={}
        lista["Info"][viaje["company"]]["servs"] = 1
        lista["Info"][viaje["company"]]["taxis"] = []
        lista["Info"][viaje["company"]]["taxis_num"] = 0

    if viaje["taxi_id"] not in lista["Info"][viaje["company"]]["taxis"]:
        lista["Info"][viaje["company"]]["taxis"].append(viaje["taxi_id"])
        valor = lista["Info"][viaje["company"]]["taxis"]
        lista["Info"][viaje["company"]]["taxis_num"] = len(valor)

    return lista


def AñadirCompañias (lista):
    for cp in lista["Info"]:
        dato=(lista["Info"][cp]["taxis_num"],cp)
        mpq.insert(lista["Compañias"],dato)
    return lista["Compañias"]


def Añadirservicios (lista):
    for cp in lista["Info"]:
        dato=(lista["Info"][cp]["servs"],cp)
        mpq.insert(lista["Servicios"],dato)
    return lista["Servicios"]


# ==============================
# Funciones de consulta
# ==============================

def total_taxis (lista):
    total=0
    for cp in lista["Info"]:
        total += lista["Info"][cp]["taxis_num"]
    return total


def companyunit (lista):
    return len(lista["Info"])


def M_compañias(lista,M):
    Min=[]
    for n in range(0,M):
        Min.append(mpq.delMin(lista["Compañias"]))
    return Min


def M_servicios(lista,M):
    Min=[]
    for n in range(0,M):
        Min.append(mpq.delMin(lista["Servicios"]))
    return Min


# ==============================
# Funciones de Comparacion
# ==============================

def comparar_taxis(taxi1,taxi2):
    tax1,o=taxi1
    tax2,m=taxi2
    if tax1 <= tax2:
        return 1
    else:
        return -1
