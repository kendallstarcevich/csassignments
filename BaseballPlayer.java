/**
 * assignment 9-object oriented programming
 * extends Athlete
 * BaseballPlayer class will take in information about an athlete but also add specific information about only baseball players
 * 
 * @author kendall starcevich
*/


public class BaseballPlayer extends Athlete
{
    private double battingAverage;
    private int homeruns;
    private String battingHand;
    private String throwingHand;

    /**
     * same as athlete class
     * @param n, String for the name of the athlete
     * @param t, String for their professional team
     * @param w, int for their weight in lbs
     * @param h, String for their height in feet and inches
     * @param p, String for their position
     * @param ht, String for their hometown
     * 
     * specific for baseball players
     * @param ba, double for career batting average
     * @param hr, int for number of career homeruns
     * @param b, String for batting hand
     * @param th, String for throwing hand
     */

    public BaseballPlayer(String n, String t, int w, String h, String p, String ht, double ba, int hr, String b, String th)
    {
        super(n,t,w,h,p,ht);
        battingAverage=ba;
        homeruns=hr;
        battingHand=b;
        throwingHand=th;

    }

    public double getBattingAverage()
    {
        return battingAverage;
    }

    public int getHomeruns()
    {
        return homeruns;
    }

    public String getBattingHand()
    {
        return battingHand;
    }

    public String getThrowingHand()
    {
        return throwingHand;
    }


     /**
     * @return String representation of a baseball player
     */

    public String toString()
    {
        String returnString = "";
        returnString+= "BASEBALL PLAYER\n";
        returnString += "name: " + getName()+"\n";
        returnString += "team: " + getTeam()+"\n"; 
        returnString += "weight: " + getWeight()+" lbs\n";
        returnString += "height: " + getHeight()+ "\" \n"; 
        returnString += "position: " + getPosition()+ "\n"; 
        returnString += "hometown: " + getHometown()+"\n";
        returnString+="--------------------------\n";
        returnString += "batting average: " + battingAverage +"\n";
        returnString += "homeruns: " + homeruns+"\n";  
        returnString += "bats: " + battingHand+"\n";  
        returnString += "throws: " + throwingHand+"\n";

        return returnString;
    }
}
