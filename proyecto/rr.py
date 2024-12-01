# rr.py
from actividad import Actividad
from collections import deque

def calcular_rr(actividades, quantum):
    cola = deque(actividades)  
    tiempo = 0
    resultado = []
    
    while cola:
        act = cola.popleft()  
        if act.ti > tiempo:  
            tiempo = act.ti
        
        if act.t > quantum:  
            tiempo += quantum  
            act.t -= quantum  
            cola.append(act)  
        else:
            tiempo += act.t  
            act.tf = tiempo  
            act.T = act.tf - act.ti  
            act.E = act.T - act.t  
            act.I = act.t / act.T  
            resultado.append(act)  
    
    actividades[:] = resultado  






