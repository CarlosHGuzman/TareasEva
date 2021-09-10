#include<iostream>
#include<conio.h>

using namespace std;

int main(){
	/*Hacer un programa que llene una matriz de 10*10 y determine la posicion[renglon, columna] del numero mayor almacenado en la matriz. Los numeros son diferentes*/
	int matriz[10][10];
	int cantidadFilas  = 0, cantidadColumnas = 0, mayorElemento = -32768;
	int posicionFilaNumeroMayor = 0, posicionColumnaNumeroMayor = 0; 
	cout<<"Por favor ingrese la cantiadd de filas: "; cin >> cantidadFilas; 
	cout<<"Por favor ingrese la cantidad de columnas: "; cin >> cantidadColumnas;
	for(int i = 0; i < cantidadFilas; i++){
		for(int j = 0; j < cantidadColumnas; j++){
			cout<<"Por favor ingrese un numero para la posicion: ("<<i+1<<"-"<<j+1<<"): "; cin >> matriz[i][j];
			if(mayorElemento < matriz[i][j]){
				mayorElemento = matriz[i][j];
				posicionFilaNumeroMayor = i;
				posicionColumnaNumeroMayor = j;
			}
		}
	}	
	cout<<"La posicion del mayor elemento es: ("<<posicionFilaNumeroMayor+1<<"-"<<posicionColumnaNumeroMayor+1<<")"<<endl;
	cout<<"El mayor elemento es: "<< mayorElemento;
	getch();
	return 0; 
}
