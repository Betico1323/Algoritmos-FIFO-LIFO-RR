from actividad import Actividad

def calcular_lifo(actividades):
    pila = []
    for act in actividades:
        pila.append(act)  
    
    tiempo = 0
    resultado = []
    while pila:
        act = pila.pop()  
        tiempo = max(tiempo, act.ti) + act.t  
        act.tf = tiempo  
        act.T = act.tf - act.ti  
        act.E = act.T - act.t  
        act.I = act.t / act.T  
        resultado.append(act)  # actividad procesada
    
    actividades[:] = resultado  







