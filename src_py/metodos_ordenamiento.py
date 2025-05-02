class MetodosDeOrdenamiento:

    def sort_bubble(self, array):
        arreglo = array.copy()
        n = len(arreglo)

        for i in range(n):
            for j in range(i+1, n):
                if arreglo[i] > arreglo[j]:
            

                    arreglo[i], arreglo[j] = arreglo[j], arreglo[i]
                   

        return arreglo
    

    def sort_bubble_mejorado(self, array):
        arreglo = array.copy()
        n = len(arreglo)

        for i in range(n):
            boolea = False
            for j in range(i+1, n - i - 1):
                if arreglo[j] > arreglo[j+1]:
            
                    boolea = True
                    arreglo[j], arreglo[j+1] = arreglo[j+1], arreglo[j]

            if not boolea:
                break
        return arreglo
    
    def sort_seleccion(self, array):
        arreglo = array.copy()
        n = len(arreglo)

        for i in range(n):
            indice_minimo = i
            for j in range(i+1, n):
                if arreglo[j] < arreglo[indice_minimo]:
                    indice_minimo = j
       
            arreglo[i], arreglo[indice_minimo] = arreglo[indice_minimo], arreglo[i]

        return arreglo
        
    def shell_sort(self, array):
        n = len(array)
        gap = n // 2
        sorted_arr = array.copy()  

        while gap > 0:
            for i in range(gap, n):
                temp = sorted_arr[i]
                j = i
                while j >= gap and sorted_arr[j - gap] > temp:
                    sorted_arr[j] = sorted_arr[j - gap]
                    j -= gap
                sorted_arr[j] = temp
            gap //= 2

        return sorted_arr
    

    

    