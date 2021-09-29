package Ejercicos29;

import Ejercicos29.CalculadoraProcesos;
import javax.swing.JOptionPane;

public class Calculadora {

    public static void main(String[] args) {

        float numero1, numero2;
        int opc;
        boolean activo = true;
        try {
            numero1 = Float.parseFloat(JOptionPane.showInputDialog(null, "Ingrese un numero: ", "3.0"));
            numero2 = Float.parseFloat(JOptionPane.showInputDialog(null, "Ingrese un numero: ", "3.0"));
            CalculadoraProcesos calculadora = new CalculadoraProcesos(numero1, numero2);
            while (activo) {
                try {
                    opc = Integer.parseInt(JOptionPane.showInputDialog("""
    -----------------Opciones-----------------
    1) Sumar los dos numeros ingresados 
    2) Restarle al primer numero el segundo
    3) Multiplicar los dos numeros 
    4) Dividir el primer numero dado por el segundo                                                
    5) Cambiar numeros        
    6) Mostrar Numeros utilizados
    7) Salir
    Ingrese la opcion:
						"""));
                    switch (opc) {
                        case 1:
                            calculadora.Suma();
                            break;
                        case 2:
                            calculadora.Restar();
                            break;
                        case 3:
                            calculadora.Multiplicar();
                            break;
                        case 4:
                            calculadora.divicion();
                            break;
                        case 5:
                            calculadora.setNumero1(Float.parseFloat(JOptionPane.showInputDialog(null, "ingrese el primer numero: ", "Cambiar valor")));
                            calculadora.setNumero2(Float.parseFloat(JOptionPane.showInputDialog(null, "ingrese el segundo numero: ", "Cambiar valor")));
                            break;
                        case 6:
                            JOptionPane.showMessageDialog(null, calculadora.getNumero1() + ", " + calculadora.getNumero2(), "Info numeros", 1);
                            break;
                        case 7:
                            activo = false;
                            JOptionPane.showMessageDialog(null, "--------------Fin de el proceso--------------", "Fin", 2);
                            break;
                        default:
                            JOptionPane.showMessageDialog(null, "La opcion ingresada no es valida", "Error", 0);

                    }
                } catch (Exception ex) {
                    JOptionPane.showMessageDialog(null, ex, "Error", 0);
                }
            }
        } catch (Exception ex) {
            JOptionPane.showMessageDialog(null, ex, "Error", 0);
        }

    }
}
