public class IterativeFibonacci {

    // Iterative method to calculate Fibonacci number
    public static int iterativeFibonacci(int n) {
        if (n <= 1) {
            return n;
        }
        int a = 0, b = 1;
        for (int i = 2; i <= n; i++) {
            int temp = a + b;
            a = b;
            b = temp;
        }
        return b;
    }

    public static void main(String[] args) {
        int n = 10; // Calculate Fibonacci numbers up to 'n'
        System.out.println("Iterative Fibonacci:");
        for (int i = 0; i < n; i++) {
            System.out.print(iterativeFibonacci(i) + " ");
        }
    }
}