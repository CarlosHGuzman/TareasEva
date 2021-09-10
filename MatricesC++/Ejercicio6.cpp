#include<iostream>
#include<conio.h>

using namespace std;

int main(){
	/*Hacer un programa que llene una matriz de 10*10 y que almacene en la diagonal principal unos y en las demas posiciones ceros.*/
	int matriz[10][10];
	int cantidadFilas  = 0, cantidadColumnas = 0;
	cout<<"Por favor ingrese la cantiadd de filas: "; cin >> cantidadFilas; 
	cout<<"Por favor ingrese la cantidad de columnas: "; cin >> cantidadColumnas;
	for(int i = 0; i < cantidadFilas; i++){
		for(int j = 0; j < cantidadColumnas; j++){
			if(i == j){
				matriz[i][j] = 1;
			}else{
				matriz[i][j] = 0;
			}
		}
	}	
	for(int i = 0; i < cantidadFilas; i++){
		for(int j = 0; j < cantidadColumnas; j++){
			cout<<matriz[i][j]<<" - ";
		}
		cout<<endl;
	}	

	getch();
	return 0; 
}
