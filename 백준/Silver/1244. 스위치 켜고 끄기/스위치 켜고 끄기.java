import java.util.Scanner;

public class Main {
    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);
        int num = scanner.nextInt();
        int[] l = new int[num];

        for (int i = 0; i < num; i++) {
            l[i] = scanner.nextInt();
        }

        int a = scanner.nextInt();
        for (int j = 0; j < a; j++) {
            int x = scanner.nextInt();
            int y = scanner.nextInt();

            if (x == 1) {
                for (int i = y - 1; i < num; i += y) {
                    l[i] = l[i] == 1 ? 0 : 1;
                }
            } else {
                l[y - 1] = l[y - 1] == 1 ? 0 : 1;
                int k = 1;
                while (y - 1 + k <= num - 1 && y - 1 - k >= 0) {
                    if (l[y - 1 + k] == l[y - 1 - k]) {
                        l[y - 1 + k] = l[y - 1 + k] == 1 ? 0 : 1;
                        l[y - 1 - k] = l[y - 1 - k] == 1 ? 0 : 1;
                        k++;
                    } else {
                        break;
                    }
                }
            }
        }

        for (int i = 0; i < l.length; i++) {
            System.out.print(l[i] + " ");
            if ((i + 1) % 20 == 0) {
                System.out.println();
            }
        }

        scanner.close();
    }
}