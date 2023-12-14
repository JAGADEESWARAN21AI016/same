import java.util.Scanner;
 
public class SumTwoNumbers {
    public static void main(String[] args) {
        int num1, num2, sum;
        Scanner scanner;
 
        scanner = new Scanner(System.in);
 
        // Take two integer input from user and
        // store it in variable num1 and num2
        System.out.println("Enter First Number");
        num1 = scanner.nextInt();
 
        System.out.println("Enter Second Number");
        num2 = scanner.nextInt();
 
        // Add two numbers using + operator
        sum = num1 + num2;
        System.out.println( sum);
    }
}