import benchmarking as bn
import metodos_ordenamiento as mo
import matplotlib.pylab as plt

if __name__ == "__main__":
    Bench = bn.Benchmarking() 
    MethodO = mo.MetodosDeOrdenamiento()
    tamanos = [500, 1000, 2000]
    resultados = []

    for tam in tamanos:
        ArregloBase = Bench.build_arreglo(tam)

        MetodosDic = {
            "Burbuja": MethodO.sort_bubble,
            "Bubble Mejorado": MethodO.sort_bubble_mejorado,
            "Seleccion": MethodO.sort_seleccion,
            "Shell": MethodO.shell_sort
        }

        for nombre, funcionmo in MetodosDic.items():
            TiempoResultado = Bench.medir_tiempo(funcionmo, ArregloBase)
            tuplares = (tam, nombre, TiempoResultado)
            resultados.append(tuplares)

    for tama, nombrec, TiempoResultadof in resultados:
        print(f"Tamaño: {tama}, Nombre: {nombrec}, Tiempo: {TiempoResultadof:.6f} segundos")

    tiempos_by_metodos = {
        "Burbuja": [],
        "Bubble Mejorado": [],
        "Seleccion": [],
        "Shell": []
    }

    for tama, nombrec, TiempoResultadof in resultados:
        tiempos_by_metodos[nombrec].append(TiempoResultadof)

    plt.figure(figsize=(10, 6))

    for nombrec, tiempos in tiempos_by_metodos.items():
        plt.plot(tamanos, tiempos, label=nombrec, marker="o") 

    plt.title("Comparacion con metodos de ordenamiento")
    plt.xlabel("Tamaño del arreglo")
    plt.ylabel("Tiempo de ejecución (s)")
    plt.legend()
    plt.show()
