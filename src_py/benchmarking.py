
from metodos_ordenamiento import MetodosDeOrdenamiento
import random
import time
class Benchmarking:
    
    def __init__(self):
        print("Benchmarking Instanciado")
        self.mO = MetodosDeOrdenamiento()

        arreglo = self.build_arreglo(1000)

        tarea_bubble = lambda: self.mO.sort_bubble(arreglo)
        TiempoN_Bubble = self.contar_con_nano_time(tarea_bubble)
        TiempoM_Bubble = self.build_con_current_time_miles(tarea_bubble)
        print(f"Tiempo en NanoSegundos: {TiempoN_Bubble:} \nTiempo en Milisegundos: {TiempoM_Bubble:.5f}\n")

    
        tarea_bubble_mejorado = lambda: self.mO.sort_bubble_mejorado(arreglo)
        TiempoN_BubbleM = self.contar_con_nano_time(tarea_bubble_mejorado)
        TiempoM_BubbleM = self.build_con_current_time_miles(tarea_bubble_mejorado)
        print(f"Tiempo en NanoSegundos: {TiempoN_BubbleM:} \nTiempo en Milisegundos: {TiempoM_BubbleM:.5f}\n")

     
        tarea_seleccion = lambda: self.mO.sort_seleccion(arreglo)
        TiempoN_Seleccion = self.contar_con_nano_time(tarea_seleccion)
        TiempoM_Seleccion = self.build_con_current_time_miles(tarea_seleccion)
        print(f"Tiempo en NanoSegundos: {TiempoN_Seleccion} \nTiempo en Milisegundos: {TiempoM_Seleccion:.5f}")

        

    def build_arreglo(self, tamaño):

        arreglo = []

        for _ in range(tamaño):
            numero_aleatorio = random.randint(0, 99999)
            arreglo.append(numero_aleatorio)
        return arreglo

    def build_con_current_time_miles(self, tarea):
        tims = time.time()
        tarea()
        tfin = time.time()
        return tfin - tims
        

    def contar_con_nano_time(self, tarea):
        tins = time.time_ns()
        tarea()
        fins = time.time_ns()
        return (fins - tins) / 100_000_000.0
