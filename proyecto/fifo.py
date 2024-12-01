from actividad import Actividad

def calcular_fifo(actividades):
    tiempo = 0
    for act in actividades:
        tiempo = max(tiempo, act.ti) + act.t
        act.tf = tiempo
        act.T = act.tf - act.ti
        act.E = act.T - act.t
        act.I = act.t / act.T






