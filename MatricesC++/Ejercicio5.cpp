#include<iostream>
#include<conio.h>

using namespace std;

int main(){
	/*Hacer un programa que llene una matriz de 5*5 y que almacene la diagonal principal en un vector. Imprimir el vector resutante*/
	int matriz[10][10];
	int cantidadFilas  = 0, cantidadColumnas = 0, diagonalPrincipal[cantidadFilas];
	cout<<"Por favor ingrese la cantiadd de filas: "; cin >> cantidadFilas; 
	cout<<"Por favor ingrese la cantidad de columnas: "; cin >> cantidadColumnas;
	for(int i = 0; i < cantidadFilas; i++){
		for(int j = 0; j < cantidadColumnas; j++){
			cout<<"Por favor ingrese un numero para la posicion: ("<<i+1<<"-"<<j+1<<"): "; cin >> matriz[i][j];
			if(i == j){
				diagonalPrincipal[i] = matriz[i][j];
			}
		}
	}	
	cout<<"Diagonal principal: ";
	for(int i = 0; i < cantidadFilas; i++){
		cout<<diagonalPrincipal[i]<<"  ";
	}
	getch();
	return 0; 
}
