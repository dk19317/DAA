public class RecursiveFibonacci {

    // Recursive method to calculate Fibonacci number
    public static int recursiveFibonacci(int n) {
        if (n <= 1) {
            return n;
        }
        return recursiveFibonacci(n - 1) + recursiveFibonacci(n - 2);
    }

    public static void main(String[] args) {
        int n = 10; // Calculate Fibonacci numbers up to 'n'
        System.out.println("Recursive Fibonacci:");
        for (int i = 0; i < n; i++) {
            System.out.print(recursiveFibonacci(i) + " ");
        }
    }
}
