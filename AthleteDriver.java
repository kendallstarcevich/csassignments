/**
 * assignment 9-object oriented programming
 * driver for Athlete and BaseballPlayer classes
 * allows you to create objects of type Athlete or BaseballPlayer
 * 
 * @author kendall starcevich
*/

public class AthleteDriver
{
    public static void main(String[] args)
    {
        Athlete a1 = new Athlete("Lionel Messi","Inter Miami FC",159,"5'7","Forward","Rosario, Argentina");
        Athlete a2 = new Athlete("Patrick Mahomes","Kansas City Chiefs",225,"6'2","Quarterback","Tyler, Texas");

        BaseballPlayer bp1 = new BaseballPlayer("Mike Trout","Los Angeles Angels",235,"6'2","Centerfield","Vineland, NJ",.301,368,"Right","Right");
        BaseballPlayer bp2 = new BaseballPlayer("Salvador Perez","Kansas City Royals",255,"6'3","Catcher","Valencia, Venezuela",.267,246,"Right","Right"); 

        System.out.println(a1);
        System.out.println(a2);
        System.out.println(bp1);
        System.out.println(bp2);
        
    }
}
