package paquete;

import java.util.Scanner;

public class Ejercicio2 {

    public static void main(String[] args) {
        /*Hacer un programa que llena una matriz de 10*10 y determine la posicion
        [renglon, columnas] del numero mayor almacenado en la matriz. Los números son diferentes.
         */
        Scanner scanner = new Scanner(System.in);
        int posicionColumnasMayor = 0, posicionFilaMayor = 0, cantidadFilas, cantidadColumnas;
        System.out.print("Ingrese el numero de filas: ");
        cantidadFilas = scanner.nextInt();
        System.out.print("Ingrese el numero de columnas: ");
        cantidadColumnas = scanner.nextInt();
        float[][] matriz = new float[cantidadFilas][cantidadColumnas];
        double primerNumero = 1.4E-45;
        for (int i = 0; i < matriz.length; i++) {
            for (int j = 0; j < matriz[i].length; j++) {
                System.out.print("Ingrese un numero para la posicion: (" + (i + 1)
                        + "-" + (j + 1) + "): ");
                matriz[i][j] = scanner.nextFloat();
                if (primerNumero < matriz[i][j]) {
                    primerNumero = matriz[i][j];
                    posicionColumnasMayor = j;
                    posicionFilaMayor = i;
                }
            }
        }
        System.out.println("El numero mayor se encuentra en la posicion: "
                + (posicionFilaMayor + 1) + "-" + (posicionColumnasMayor + 1));
        System.out.println("Numero: " + matriz[posicionFilaMayor][posicionColumnasMayor]);
    }
}
