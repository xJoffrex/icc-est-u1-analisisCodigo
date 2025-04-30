import java.util.Random;


public class Benchmarking {

    private MetodosOrdenamiento mOrdenamiento;
    
    public Benchmarking(){
        long CurrentMillis = System.currentTimeMillis();
        long currentNano = System.nanoTime();

        System.out.println(CurrentMillis);
        System.out.println(currentNano);

        mOrdenamiento = new MetodosOrdenamiento();

        int[] arreglo = arregloaleatorio(10000);
        Runnable tarea = () -> mOrdenamiento.burbujaTradicional(arreglo);
        double medirConcurrenmiles =  medirConcurrenmiles(tarea);
        double medirconnano =  medirconnano(tarea);

        System.out.println("Tiempo en milisegundos: " + medirConcurrenmiles + "ms");
        System.out.println("Tiempo en nanosegundos: " + medirconnano + "ns");
    }

    private int[] arregloaleatorio(int tamano){
        Random aleatorio = new Random();
        int[] array = new int[tamano];
        for (int i = 0 ; i<tamano ; i++){
            array[i] = aleatorio.nextInt(100000);
        }
        return array;
    }

    public double medirConcurrenmiles(Runnable tarea){
        long inicio = System.currentTimeMillis();
        tarea.run();
        long fin = System.currentTimeMillis();
        double tiempseg = (fin - inicio) * 1000.0;
        return tiempseg;
    }

    public double medirconnano(Runnable tarea){
        long inicio = System.nanoTime();
        tarea.run();
        long fin = System.nanoTime();
        return (fin - inicio) * 100_000_000.0;
    }


}
