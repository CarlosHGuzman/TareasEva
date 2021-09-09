import java.util.Scanner;

public class Ejercicio3 {
    public static void main(String[] args) {
   Scanner scanner = new Scanner(System.in);

        System.out.print("Por favor ingrese el numero de filas: ");
        int cantidadFilas = scanner.nextInt();
        System.out.print("Por favor ingrese el numero de columnas: ");
        int cantidadColumnas = scanner.nextInt();
        int sumaColumnas[] = new int[cantidadColumnas];
        int sumaFilas[] = new int[cantidadFilas];
        int suma;
        /*
        3. Hacer un programa que llene una matriz de 7 * 7. Calcular la suma de cada renglón y almacenarla en un vector, la suma de cada columna y almacenarla en otro vector.
        pero cambia 7 *7 po lo que la persona ingrese el imite
         */
        int matriz[][] = new int[cantidadFilas][cantidadColumnas];

        for (int i = 0; i < cantidadFilas; i++) {
            suma = 0;
            for (int j = 0; j < cantidadColumnas; j++) {
                System.out.print("Por favor ingrese un numero: ");
                matriz[i][j] = scanner.nextInt();
                suma += matriz[i][j];
            }
            sumaFilas[i] = suma;
        }

        for (int i = 0, aux = 1; i < cantidadColumnas; i++, aux++) {
            suma = 0;
                for (int j = 0; j < cantidadFilas; j++) {
                    suma += matriz[j][i];
            }
            sumaColumnas[i] = suma;
        }

        for (int i = 0; i < cantidadFilas; i++) {
            System.out.println("Suma fila #" + (i + 1) + ": " + sumaFilas[i]);
        }

        for (int i = 0; i < cantidadColumnas; i++) {
            System.out.println("Suma columna #" + (i + 1) + ": " + sumaColumnas[i]);
        }
    }
}
