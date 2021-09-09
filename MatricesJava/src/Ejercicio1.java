
package paquete;

import java.util.Scanner;

public class Ejercicio1 {
    public static void main(String[] args){
        /*Hacer un programa que almacene números en una matriz de 5*6. Imprimir la
        suma de los numeros almacenados en la matriz.
        */
        Scanner scanner = new Scanner(System.in);
        float sumaNumerosMatriz = 0;
        System.out.print("Ingrese el numero de filas: "); int cantidadFilas = scanner.nextInt();
        System.out.print("Ingrese el numero de columnas: "); int cantidadColumnas = scanner.nextInt();
        float matriz[][] = new float[cantidadFilas][cantidadColumnas];
        for (int i = 0; i < matriz.length; i++) {
            for (int j = 0; j < matriz[i].length; j++) {
                System.out.print("Ingrese un numero para la posicion: (" + (i+1)
                + "-" + (j+1) + "): "); sumaNumerosMatriz += matriz[i][j] = scanner.nextFloat();
            }
        }
        System.out.println("La suma de los numeros de la matriz es: " + sumaNumerosMatriz);
    }
}
