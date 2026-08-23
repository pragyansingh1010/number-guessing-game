import java.util.Random;
import java.util.Scanner;

public class NumberGuessingGame {
    public static void main(String[] args) {

        Scanner sc = new Scanner(System.in);
        Random r = new Random();

        int number = r.nextInt(100) + 1;
        int attempts = 0;
        int guess;

        System.out.println("===== NUMBER GUESSING GAME =====");
        System.out.println("Guess a number between 1 and 100");

        while (true) {

            System.out.print("Enter your guess: ");
            guess = sc.nextInt();
            attempts++;

            if (guess > number) {
                System.out.println("Lower!");
            }
            else if (guess < number) {
                System.out.println("Higher!");
            }
            else {
                System.out.println("Congratulations! You guessed the number.");
                System.out.println("Number was: " + number);
                System.out.println("Total attempts: " + attempts);
                break;
            }
        }
    }
}