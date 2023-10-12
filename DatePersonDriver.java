//kendall starcevich
//assignment 8
//Driver

public class DatePersonDriver
{
    public static void main(String[] args)
    {
        Date kendallBirthday= new Date("September",03,2003); //using my first Person object
        Person kendall = new Person("Kendall", kendallBirthday);

        Date karlieBirthday = new Date("December",29,2005);//using my first Person object;
        Person karlie = new Person("Karlie", karlieBirthday);

        Person professorU = new Person("Tim", "September", 15,1976); //using my second Person object

        System.out.println(kendall);
        System.out.println(karlie);
        System.out.println(professorU);
    }
}