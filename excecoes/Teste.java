public class Teste {

    public double divide(double a, double b) throws Exception {
        if (b == 0)
            throw new Exception("Dividindo por 0");
        return a / b;
    }

    public static void main(String[] args) {
        Teste t = new Teste();
        try {
            double resultado = t.divide(10, 0);
            System.out.println("Resultado " + resultado);
        }
        catch(Exception e) {
            //e.printStackTrace();
            System.out.println("Erro no programa, verifique o log");
        }
    }
}