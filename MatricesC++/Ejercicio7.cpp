#include<iostream>
#include<conio.h>

using namespace std;

int main(){
	/*Hacer un programa que llene una matriz de 10*10 y que almacene en la diagonal principal unos y en las demas posiciones ceros.*/
	int cantidadFilas  = 0, cantidadColumnas = 0, contadorVector = 0;
	int matriz[10][10],  vector[cantidadFilas * cantidadColumnas];
	cout<<"Por favor ingrese la cantiadd de filas: "; cin >> cantidadFilas; 
	cout<<"Por favor ingrese la cantidad de columnas: "; cin >> cantidadColumnas;
	for(int i = 0; i < cantidadFilas; i++){
		for(int j = 0; j < cantidadColumnas; j++){
			cout<<"Por favor ingrese un numero para la posicion: ("<<i+1<<"-"<<j+1<<"): "; cin >> matriz[i][j];
			vector[contadorVector] = matriz[i][j];
			contadorVector++;
		}
	}	
	for(int i = 0; i < cantidadColumnas * cantidadFilas; i++){
		cout<<"Elemento: ("<<i+1<<"): "<< vector[i] <<endl;
	}

	getch();
	return 0; 
}
