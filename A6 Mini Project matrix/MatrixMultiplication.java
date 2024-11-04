import java.util.Arrays;

class MatrixMultiplication {

    // Normal matrix multiplication
    public static int[][] matrixMultiply(int[][] A, int[][] B) {
        int rowsA = A.length;
        int colsA = A[0].length;
        int colsB = B[0].length;

        int[][] C = new int[rowsA][colsB];

        for (int i = 0; i < rowsA; i++) {
            for (int j = 0; j < colsB; j++) {
                for (int k = 0; k < colsA; k++) {
                    C[i][j] += A[i][k] * B[k][j];
                }
            }
        }

        return C;
    }

    // Multithreaded matrix multiplication (thread per row)
    public static int[][] matrixMultiplyThreadRow(int[][] A, int[][] B) throws InterruptedException {
        int rowsA = A.length;
        int colsB = B[0].length;

        int[][] C = new int[rowsA][colsB];

        Thread[] threads = new Thread[rowsA];

        for (int i = 0; i < rowsA; i++) {
            final int row = i;
            threads[i] = new Thread(() -> {
                for (int j = 0; j < colsB; j++) {
                    for (int k = 0; k < A[0].length; k++) {
                        C[row][j] += A[row][k] * B[k][j];
                    }
                }
            });
            threads[i].start();
        }

        for (Thread thread : threads) {
            thread.join();
        }

        return C;
    }

    // Multithreaded matrix multiplication (thread per element)
    public static int[][] matrixMultiplyThreadElement(int[][] A, int[][] B) throws InterruptedException {
        int rowsA = A.length;
        int colsB = B[0].length;

        int[][] C = new int[rowsA][colsB];

        Thread[][] threads = new Thread[rowsA][colsB];

        for (int i = 0; i < rowsA; i++) {
            for (int j = 0; j < colsB; j++) {
                final int row = i;
                final int col = j;
                threads[i][j] = new Thread(() -> {
                    for (int k = 0; k < A[0].length; k++) {
                        C[row][col] += A[row][k] * B[k][col];
                    }
                });
                threads[i][j].start();
            }
        }

        for (int i = 0; i < rowsA; i++) {
            for (int j = 0; j < colsB; j++) {
                threads[i][j].join();
            }
        }

        return C;
    }

    // Helper function to print matrix
    public static void printMatrix(int[][] matrix) {
        for (int[] row : matrix) {
            System.out.println(Arrays.toString(row));
        }
    }

    // Performance analysis
    public static void main(String[] args) throws InterruptedException {
        int[][] A = {
            {1, 2, 3},
            {4, 5, 6},
            {7, 8, 9}
        };

        int[][] B = {
            {9, 8, 7},
            {6, 5, 4},
            {3, 2, 1}
        };

        // Normal matrix multiplication
        long startTime = System.currentTimeMillis();
        int[][] C_normal = matrixMultiply(A, B);
        long endTime = System.currentTimeMillis();
        System.out.println("Normal multiplication time: " + (endTime - startTime) + " ms");
        System.out.println("Resultant matrix (Normal):");
        printMatrix(C_normal);

        // Multithreaded matrix multiplication (thread per row)
        startTime = System.currentTimeMillis();
        int[][] C_threadRow = matrixMultiplyThreadRow(A, B);
        endTime = System.currentTimeMillis();
        System.out.println("\nThread-per-row multiplication time: " + (endTime - startTime) + " ms");
        System.out.println("Resultant matrix (Thread-per-row):");
        printMatrix(C_threadRow);

        // Multithreaded matrix multiplication (thread per element)
        startTime = System.currentTimeMillis();
        int[][] C_threadElement = matrixMultiplyThreadElement(A, B);
        endTime = System.currentTimeMillis();
        System.out.println("\nThread-per-element multiplication time: " + (endTime - startTime) + " ms");
        System.out.println("Resultant matrix (Thread-per-element):");
        printMatrix(C_threadElement);
    }
}
