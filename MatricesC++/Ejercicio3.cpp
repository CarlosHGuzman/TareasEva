#include<iostream>
#include<conio.h>

using namespace std;

int main(){
	/*Hacer un programa que llene una matriz de 7*7. Calcular la suma de cada renglón y almacenarla en un vector, la suma de cada columna y almacenarla en otro vector*/
	int matriz[10][10];
	int cantidadFilas  = 0, cantidadColumnas = 0, sumasFilas[cantidadFilas], sumasColumnas[cantidadColumnas];
	int sumaFila = 0, sumaColumna = 0; 
	cout<<"Por favor ingrese la cantiadd de filas: "; cin >> cantidadFilas; 
	cout<<"Por favor ingrese la cantidad de columnas: "; cin >> cantidadColumnas;
	for(int i = 0; i < cantidadFilas; i++){
		sumaFila = 0;
		for(int j = 0; j < cantidadColumnas; j++){
			cout<<"Por favor ingrese un numero para la posicion: ("<<i+1<<"-"<<j+1<<"): "; cin >> matriz[i][j];
			sumaFila += matriz[i][j];
		}
		sumasFilas[i] = sumaFila; 
	}	
	for(int i = 0; i < cantidadColumnas; i++){
		sumaColumna = 0;
		for(int j = 0; j < cantidadFilas; j++){
			sumaColumna += matriz[j][i];
		}
		sumasColumnas[i] = sumaColumna;
	}
	for(int i = 0; i < cantidadFilas; i++){
		cout<<"La suma de la fila : "<<i+1<<" es: "<<sumasFilas[i]<<endl;
	}
	
	for(int i = 0; i < cantidadColumnas; i++){
		cout<<"La suma de la Columna : "<<i+1<<" es: "<<sumasColumnas[i]<<endl;
	}
	getch();
	return 0; 
}
