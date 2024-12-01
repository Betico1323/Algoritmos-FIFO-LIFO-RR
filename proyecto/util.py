import csv
from actividad import Actividad
import pandas as pd

# Función para leer el archivo CSV y cargar las actividades
def leer_actividades(archivo):
    actividades = []
    with open(archivo, newline='') as f:
        reader = csv.reader(f)
        next(reader)  # Saltar la primera línea (encabezado)
        for row in reader:
            id = row[0]
            ti = int(row[1])
            t = int(row[2])
            actividades.append(Actividad(id, ti, t))
    return actividades

# Función para mostrar los resultados de las actividades
def mostrar_resultados(metodo, actividades):
    print(f"Resultados para {metodo}:")
    print(f"{'Actividad':<12}{'tf':<10}{'T':<10}{'E':<10}{'I':<10}")
    print("-" * 42)
    
    totalT = totalE = totalI = 0
    for act in actividades:
        print(f"{act.id:<12}{act.tf:<10}{act.T:<10}{act.E:<10}{act.I:<10.4f}")
        totalT += act.T
        totalE += act.E
        totalI += act.I
    
    n = len(actividades)
    print("-" * 42)
    print(f"Promedio T: {totalT/n:.4f}")
    print(f"Promedio E: {totalE/n:.4f}")
    print(f"Promedio I: {totalI/n:.4f}")







