package Ejercicos29;

import javax.swing.JOptionPane;

public class CalculadoraProcesos {
        private float numero1; 
        private float numero2; 
	
        public CalculadoraProcesos(float numero1, float numero2){
            this.numero1 = numero1;
            this.numero2 = numero2;
        }
        
	public void Suma() {
		double sumaTotal = this.numero1 + this.numero2; 
		JOptionPane.showMessageDialog(null, "La suma es: "+ sumaTotal, "Resultado", 1);
	}	
	public void Restar() {
		double restaTotal = this.numero2 - this.numero1;
		JOptionPane.showMessageDialog(null, "La resta es: "+restaTotal, "Resultado", 1);
	}
	public void Multiplicar() {
		double multiplicacionTotal = this.numero1 * this.numero2;
		JOptionPane.showMessageDialog(null, "La multiplicacion: " + multiplicacionTotal, "Resultado", 1);
	}
	public void divicion() {
		double divicionTotal = this.numero1 / numero2;
                JOptionPane.showMessageDialog(null, "La division es: " + divicionTotal, "Resultado", 1);
	}
        public void setNumero1(float numero1){
            this.numero1 = numero1;
        }
        
        public void setNumero2(float numero2){
            this.numero2 = numero2;
        }

    public float getNumero1() {
        return this.numero1;
    }

    public float getNumero2() {
        return this.numero2;
    }
        
}