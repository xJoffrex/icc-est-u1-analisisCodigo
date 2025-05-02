#Main
import benchmarking as bn
import metodos_ordenamiento as mo


if __name__ == "__main__":
    Bench = bn.Benchmarking() 
    MethodO = mo.MetodosDeOrdenamiento()
    tamanos = [5000, 1000, 15000]
  #  tam = 10000
    

    for tam in tamanos:
        ArregloBase = Bench.build_arreglo(tam)

        MetodosDic = {
            "Burbuja" : MethodO.sort_bubble,
            "Bubble Mejorado": MethodO.sort_bubble_mejorado,
            "Seleccion" : MethodO.sort_seleccion,
            "Shell" : MethodO.shell_sort

        }

        resultados = []

        for nombre, funcionmo in MetodosDic.items():
            TiempoResultado = Bench.medir_tiempo(funcionmo, ArregloBase)
            tuplares = (tam, nombre, TiempoResultado)
            resultados.append(tuplares)

        for tama, nombrec, TiempoResultadof in resultados:
            print(f"Tamaño: {tama}, Nombre: {nombrec}, Tiempo: {TiempoResultadof:.6f} segundos")
    

