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
public class DoWhile2 {
    public static void main(String[]AndresM) {
        short num;
        int fact;
        byte opcion;
        do{
            fact = 1;
            num = (Short)Short.parseShort(JOptionPane.showInputDialog("Ingresa un numero"));
            for(int x = num; x>=1 ; x--){
                fact = fact * x ;
            }
            System.out.println("El factorial del numero" + num + " es "+ fact);
            opcion = (Byte)Byte.parseByte(JOptionPane.showInputDialog("Ingresa el numero 1 para calcular otro factorial"));
        }while(opcion==1);
    }
}