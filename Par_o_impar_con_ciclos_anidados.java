/*
 * To change this license header, choose License Headers in Project Properties.
 * To change this template file, choose Tools | Templates
 * and open the template in the editor.
 */

/**
 *
 * @author 52553
 */
  import javax.swing.JOptionPane;
public class Par_o_impar_con_ciclos_anidados{
    public static void main(String[] args) {
        for (int i = 1; i <= 10; i++) {
            int numero = Integer.parseInt(JOptionPane.showInputDialog("Inserta un número (" + i + "/10):"));

            if (numero % 2 == 0) {
                int cociente = numero / 2;

                String resultado = "";
                for (int j = 0; j < cociente; j++) {
                    resultado += "*";
                }

                JOptionPane.showMessageDialog(null, 
                    "Número par. Resultado:\n" + resultado);
            } else {
                JOptionPane.showMessageDialog(null, 
                    "Número impar.");
            }
        }
    }
}


