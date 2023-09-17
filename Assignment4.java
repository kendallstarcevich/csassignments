//Kendall Starcevich
//Assignment 4-files

import java.io.*;
import java.util.Scanner;


public class Assignment4 
{
    public static void main(String[] args) throws IOException
    {
        File myFile = new File("Numbers.txt");
        Scanner inputFile = new Scanner(myFile);
        
        double min = 100;
        double max = 0;
        int count = 0;
        double numberCount = 0;
        while (inputFile.hasNext())
        {
            double number = inputFile.nextDouble();
            if (number<min)
            {
                min=number;
            }
            if (number>max)
            {
                max=number;
            }
            count++;
            numberCount = numberCount+number;
        }

        double average = numberCount/count;
        System.out.println("There are a total of " + count+" numbers.");
        System.out.println("The minimum number is: "+ min);
        System.out.println("The maximum number is: "+ max); 
        System.out.printf("The average is: %.2f\n",average);
        inputFile.close();
    }
}