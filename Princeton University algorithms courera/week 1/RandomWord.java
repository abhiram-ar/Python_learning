import java.util.Scanner;

public class RandomWord {
    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);
        String champion = "";
        int count = 0;

        while (scanner.hasNext()) {
            String word = scanner.next();
            count++;
            if (Math.random() < 1.0 / count) {
                champion = word;
            }
        }

        System.out.println(champion);
    }
}
