import sys
sys.path.append('./proyecto')

from util import leer_actividades, mostrar_resultados
from fifo import calcular_fifo
from lifo import calcular_lifo
from rr import calcular_rr
import time
import copy

def calcular_promedios(actividades):
    total_t = total_e = total_i = 0
    for act in actividades:
        total_t += act.T
        total_e += act.E
        total_i += act.I
    
    n = len(actividades)
    return total_t / n, total_e / n, total_i / n

def comparar_resultados(fifo_actividades, lifo_actividades, rr_actividades, fifo_time, lifo_time, rr_time):
    # Calcular promedios de T, E, I para cada método
    promedio_fifo_t, promedio_fifo_e, promedio_fifo_i = calcular_promedios(fifo_actividades)
    promedio_lifo_t, promedio_lifo_e, promedio_lifo_i = calcular_promedios(lifo_actividades)
    promedio_rr_t, promedio_rr_e, promedio_rr_i = calcular_promedios(rr_actividades)
    
    # Mostrar los promedios de cada método
    print("\nPromedios de cada método:")
    print(f"FIFO: T = {promedio_fifo_t:.2f}, E = {promedio_fifo_e:.2f}, I = {promedio_fifo_i:.2f}")
    print(f"LIFO: T = {promedio_lifo_t:.2f}, E = {promedio_lifo_e:.2f}, I = {promedio_lifo_i:.2f}")
    print(f"RR: T = {promedio_rr_t:.2f}, E = {promedio_rr_e:.2f}, I = {promedio_rr_i:.2f}")
    
    # Inicializar el mejor método con el tiempo más bajo
    mejor_metodo = None
    mejor_tiempo = min(fifo_time, lifo_time, rr_time)  
    mejor_promedio = float('inf')  

    # Ahora comparamos los tres algoritmos basados en los tiempos y los promedios
    if fifo_time == mejor_tiempo: 
        if promedio_fifo_t + promedio_fifo_e + promedio_fifo_i < mejor_promedio:  
            mejor_metodo = "FIFO"
            mejor_promedio = promedio_fifo_t + promedio_fifo_e + promedio_fifo_i
    
    if lifo_time == mejor_tiempo:  # Si LIFO tiene el menor tiempo
        if promedio_lifo_t + promedio_lifo_e + promedio_lifo_i < mejor_promedio:
            mejor_metodo = "LIFO"
            mejor_promedio = promedio_lifo_t + promedio_lifo_e + promedio_lifo_i

    if rr_time == mejor_tiempo:  # Si Round Robin tiene el menor tiempo
        if promedio_rr_t + promedio_rr_e + promedio_rr_i < mejor_promedio:
            mejor_metodo = "Round Robin"
            mejor_promedio = promedio_rr_t + promedio_rr_e + promedio_rr_i
    
    print(f"\nEl mejor método es: {mejor_metodo}")
    
def main():
    # Cargar actividades desde el archivo CSV
    actividades = leer_actividades('datos.csv')

    if not actividades:
        print("No se pudieron cargar actividades desde el archivo.")
        return

    # Preguntar al usuario por el quantum para el algoritmo RR
    quantum = int(input("Ingrese el quantum para Round Robin: "))

    
    fifo_actividades = copy.deepcopy(actividades)
    lifo_actividades = copy.deepcopy(actividades)
    rr_actividades = copy.deepcopy(actividades)

    # Calcular resultados para FIFO
    start_time = time.perf_counter()
    calcular_fifo(fifo_actividades)
    fifo_duration = time.perf_counter() - start_time
    mostrar_resultados("FIFO", fifo_actividades)
    print(f"Tiempo de cálculo FIFO: {fifo_duration:.6f} segundos\n")

    # Calcular resultados para LIFO
    start_time = time.perf_counter()
    calcular_lifo(lifo_actividades)
    lifo_duration = time.perf_counter() - start_time
    mostrar_resultados("LIFO", lifo_actividades)
    print(f"Tiempo de cálculo LIFO: {lifo_duration:.6f} segundos\n")

    # Calcular resultados para Round Robin
    start_time = time.perf_counter()
    calcular_rr(rr_actividades, quantum)
    rr_duration = time.perf_counter() - start_time
    mostrar_resultados("Round Robin", rr_actividades)
    print(f"Tiempo de cálculo Round Robin: {rr_duration:.6f} segundos\n")

    # Comparar los resultados de los tres métodos
    comparar_resultados(fifo_actividades, lifo_actividades, rr_actividades, fifo_duration, lifo_duration, rr_duration)

if __name__ == "__main__":
    main()















