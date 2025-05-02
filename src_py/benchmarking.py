
from metodos_ordenamiento import MetodosDeOrdenamiento
import random
import time
class Benchmarking:
   
    def __init__(self):
        print("Benchmarking Instanciado")
        self.mO = MetodosDeOrdenamiento()


    
      

    def build_arreglo(self, tamano):

        arreglo = []

        for i in range(tamano):
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
    
    def medir_tiempo(self, funcions, arreglo):
        tinc = time.perf_counter()
        funcions(arreglo)
        finsc = time.perf_counter()
        return finsc - tinc
