/**
 * assignment 9-object oriented programming
 * athlete class will take in information about an athlete and create an object of type Athlete.
 * can be extended by different sports players, I made baseball only
 * 
 * @author kendall starcevich
*/

public class Athlete 
{
    private String name;
    private String team;
    private int weight;
    private String height;
    private String position;
    private String hometown;

    /**
     * Constructor for an Athlete
     * @param n, String for the name of the athlete
     * @param t, String for their professional team
     * @param w, int for their weight in lbs
     * @param h, String for their height in feet and inches
     * @param p, String for their position
     * @param ht, String for their hometown
     */

    public Athlete(String n, String t, int w, String h, String p, String ht) //initializes the "facts"
    {
        name = n;
        team = t;
        weight = w;
        height = h;
        position = p;
        hometown = ht;
    }

    public String getName()
    {
        return name;
    }

    public String getTeam()
    {
        return team;
    }

    public int getWeight()
    {
        return weight;
    }

    public String getHeight()
    {
        return height;
    }
    public String getHometown()
    {
        return hometown;
    }
    public String getPosition()
    {
        return position;
    }

    /**
     * @return String representation of an Athlete
     */

    public String toString()
    {
        String returnString = "";
        returnString+= "ATHLETE\n";
        returnString += "name: " + name+"\n";
        returnString += "team: " + team+"\n"; 
        returnString += "weight: " + weight+" lbs\n";
        returnString += "height: " + height+ "\" \n"; 
        returnString += "position: " + position+"\n"; 
        returnString += "hometown: " + hometown+"\n";
        return returnString;
    } 
}
