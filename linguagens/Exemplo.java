
import java.util.Scanner;

public class Exemplo {
    public static void main(String[] args) {
        Scanner tec = new Scanner(System.in);
        System.out.println("Olá Mundo!");
        System.out.print("Digite um número: ");
        int num = tec.nextInt();
        System.out.println("O numero digitado foi " + num);
        tec.close();
    }
}