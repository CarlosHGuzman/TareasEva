package paquete;

import java.util.Scanner;

public class Ejercicio5 {

    public static void main(String[] args) {
        /*
        Hacer un progrma que llena una matriz de 5*5 y que almacene la diagonal
        principal en un vector. Imprimir el vector resultante.
         */
        var scanner = new Scanner(System.in);
        int cantidadFilas, cantidadColumnas;
        System.out.print("Ingrese la cantidad de filas: ");
        cantidadFilas = scanner.nextInt();
        System.out.print("Ingrese la cantidad de columnas: ");
        cantidadColumnas = scanner.nextInt();
        float matriz[][] = new float[cantidadFilas][cantidadColumnas]; float vector[] = new float[cantidadFilas];
        for (int i = 0; i < cantidadFilas; i++) {
            for (int j = 0; j < cantidadColumnas; j++) {
                System.out.print("Ingrese un numero para la posicion: ("
                        + (i + 1) + "-" + (j + 1) + "): ");
                matriz[i][j] = scanner.nextInt();
                if(i == j){
                    vector[i] = matriz[i][j];
                }
            }
        }
        for (int i = 0; i < cantidadFilas; i++) {
            System.out.println("Posicion : " + (i+1) + " numero: " + vector[i]);
        }
    }
}
