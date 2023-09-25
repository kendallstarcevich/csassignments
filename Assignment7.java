//kendall starcevich
//assignment 7-methods

import java.io.*;
import java.util.Scanner;
import java.io.IOException;

public class Assignment7
{
    
    public static String promptName()
    {
        Scanner keyboard = new Scanner(System.in);
        System.out.println("What is the file name?"); //prompts the user for the name of the file
        String name = keyboard.nextLine();
        keyboard.close();
        return name; //returns the file as the variable "name"
    }

    public static char[][] readFile(String fileName) throws IOException 
    {
        File myFile = new File(fileName); //reads the file that is returned from promptName()
        Scanner inputFile = new Scanner(myFile);

        int numRows = inputFile.nextInt(); //read in number of rows
        int numCols = inputFile.nextInt(); //read in number of columns
        inputFile.nextLine(); //"gooble up" new line character
        char[][] grid = new char[numRows][numCols]; //makes a 2D array out of the file
        int row = 0;
        
        while (inputFile.hasNext()) //reads each line of the file until it does not have a next line
        {
            String myStr = inputFile.nextLine(); 
            grid[row] = myStr.toCharArray();
            row++;
        }

    inputFile.close();
    return grid;
    }
    public static int findLongestSequence(char[][] grid)
    {
        int max1 = 0;
        int max2 = 0;
    
        // Check rows for longest sequence
        for (int r = 0; r < grid.length; r++)//I found this .length method of a 2D array from Coding Rooms. link: https://www.codingrooms.com/blog/2d-array-length-java#:~:text=Learn%20how%20to%20get%20the%20length%20of%20a%202D%20array%20in%20Java&text=We%20use%20arrayname.,length%20of%20the%202D%20array.
        //used to find number of rows
        {
            int count1 = 0; // Reset count1 for each new row
            for (int c = 0; c < grid[0].length; c++)//found this .length method from the same link, used to find number of columns
            {
                if (grid[r][c] == 'X') 
                {
                    count1++;
                    if (count1 > max1) 
                    {
                        max1 = count1;
                    }
                } 
                else 
                {
                    count1 = 0; //resets the count if the char is not an X
                }
            }
        }
    
        // Check columns for longest sequence
        for (int c = 0; c < grid[0].length; c++)
        {
            int count2 = 0;
            for (int r = 0; r < grid.length; r++) 
            {
                if (grid[r][c] == 'X') 
                {
                    count2++;
                    if (count2 > max2) 
                    {
                        max2 = count2;
                    }
                } 
                else
                {
                    count2 = 0; 
                }
            }
        }  
    if (max1 > max2) //since it is the longest # of X's in rows or columns, return the higher value
    {
        return max1;
    }
    else
    {
        return max2;
    }
    }
    public static void main(String[] args) throws IOException
    {
        String fileName = promptName(); //main class
        char[][] grid = readFile(fileName);
        int maxSequence = findLongestSequence(grid);
        System.out.println("The longest sequence is " + maxSequence + " long.");
    }

}

