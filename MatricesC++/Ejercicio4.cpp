#include<iostream>
#include<conio.h>

using namespace std;

int main(){
	/*Hacer un programa que llene una matriz de 20*20. Sumar las columnas e imprimir que columna tuvo la maxima suma y la suma de esa columna*/
	int matriz[10][10];
	int cantidadFilas  = 0, cantidadColumnas = 0,  sumaMayorColumnas = 0;
	int sumaColumna = 0, posicionColumnaMayorSuma = 0; 
	cout<<"Por favor ingrese la cantiadd de filas: "; cin >> cantidadFilas; 
	cout<<"Por favor ingrese la cantidad de columnas: "; cin >> cantidadColumnas;
	for(int i = 0; i < cantidadFilas; i++){
		for(int j = 0; j < cantidadColumnas; j++){
			cout<<"Por favor ingrese un numero para la posicion: ("<<i+1<<"-"<<j+1<<"): "; cin >> matriz[i][j];
		}
	}	
	for(int i = 0; i < cantidadColumnas; i++){
		sumaColumna = 0;
		for(int j = 0; j < cantidadFilas; j++){
			sumaColumna += matriz[j][i];
		}
		if(sumaColumna > sumaMayorColumnas){
			sumaMayorColumnas = sumaColumna; 
			posicionColumnaMayorSuma = i;
		}
	}

	cout<<"La posicion de la columna con mayor suma es: "<<posicionColumnaMayorSuma+1;
	cout<<endl<<"La suma de su columna es: "<<sumaMayorColumnas;
	getch();
	return 0; 
}
