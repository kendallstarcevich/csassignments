//Kendall Starcevich
//Assignment 6-word find

import java.io.*;
import java.util.Scanner;

public class Assignment6
{
    public static void main(String[] args) throws IOException
    {
        File myGridFile = new File("Grid.txt");
        char[][] grid = new char[6][6];
        Scanner inputGridFile = new Scanner(myGridFile);
        int row = 0;

        // Import grid.txt
        while (inputGridFile.hasNext())
        
        {
            String myStr = inputGridFile.nextLine();
            grid[row] = myStr.toCharArray();
            row++;
        }
        inputGridFile.close();

        // Import dictionary.txt
        File myDictFile = new File("dictionary.txt");
        Scanner inputDictFile = new Scanner(myDictFile);
    
        while (inputDictFile.hasNext())
        {
            // Check rows
            String word = inputDictFile.nextLine();
            String str = "";
            for (int r = 0; r < 6; r++)
            {
                str="";
                for (int c = 0; c < 6; c++)
                {
                    str += grid[r][c];
                }
                if (str.contains(word))
                {
                    System.out.println(word);
                }
            }
            // Check columns
            for (int c = 0; c < 6; c++)
            {
                str="";
                for (int r = 0; r < 6; r++)
                {
                    str += grid[r][c];
                }
                if (str.contains(word))
                {
                    System.out.println(word);
                }
            }  
        }
        inputDictFile.close();

    }
}
