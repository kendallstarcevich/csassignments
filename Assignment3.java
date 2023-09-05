//Kendall Starcevich
//Assignment 3- BMI calculator
import java.util.Scanner;
public class Assignment3
{
    public static void main(String[] args)
    {
        Scanner keyboard = new Scanner(System.in);
        String name;
        int weight;
        double height;

        System.out.println("Please enter your name:");
        name = keyboard.nextLine();

        System.out.println("Please enter your weight in pounds:");
        weight = keyboard.nextInt();

        System.out.println("Please enter your height in inches:");
        height = keyboard.nextDouble();

        double bmi = 703*(weight/(height*height));

        System.out.printf("BMI for "+name+ " is %.2f\n", bmi);
        keyboard.close();
    }
}
