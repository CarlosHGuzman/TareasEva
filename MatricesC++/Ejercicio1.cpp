#include<iostream>
#include<conio.h>

using namespace std;

int main(){
	/*Hacer un programa que almacene números en una matriz de 5*6. Imprimir la suma de los números almacenados en la matriz*/
	int matriz[10][10];
	int cantidadFilas  = 0, cantidadColumnas = 0, sumaElementosMatriz = 0; 
	cout<<"Por favor ingrese la cantiadd de filas: "; cin >> cantidadFilas; 
	cout<<"Por favor ingrese la cantidad de columnas: "; cin >> cantidadColumnas;
	for(int i = 0; i < cantidadFilas; i++){
		for(int j = 0; j < cantidadColumnas; j++){
			cout<<"Por favor ingrese un numero para la posicion: ("<<i+1<<"-"<<j+1<<"): "; cin >> matriz[i][j];
			sumaElementosMatriz += matriz[i][j];
		}
	}	
	cout<<"La suma de los elementos de la  matriz es: "<< sumaElementosMatriz;
	getch();
	return 0; 
}
