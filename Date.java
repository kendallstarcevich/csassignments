//kendall starcevich
//assignment 8
//Date class

public class Date
{
    private String month;
    private int day;
    private int year;


    public Date(String m, int d, int y) //creates the Date object and takes in 3 arguments
    {
        month=m;
        day=d;
        year=y;
    }

    public void setMonth(String m)
    {
        month=m;
    }
    public String getMonth()
    {
        return month;
    }

    public void setDay(int d)
    {
        day=d;
    }
    public int getDay()
    {
        return day;
    }

    public void setYear(int y)
    {
        year=y;
    }
    public int getYear()
    {
        return year;
    }

    public String toString() //prints the date in the format that I want the user to see
    {
        return (month+" "+day+", "+year+".");

    }
}



