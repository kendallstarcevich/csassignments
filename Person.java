//kendall starcevich
//assignment 8
//Person class

public class Person
{
    private String name;
    private Date birthday; //use the Date object from my Date class 

    public Person(String name, Date birthday) 

    //allows you to create a Person object with two lines, like:
    //Date kendallBirthday= new Date("September",03,2003);
    //Person kendall = new Person("Kendall", kendallBirthday);

    {
        this.name = name;
        this.birthday = birthday;
    }

    public Person(String name, String m, int d, int y)

    //allows you to create a Person object like:
    //Person professorU = new Person("Tim", "September", 15,1976);

    {
        this.name = name;
        Date date = new Date (m,d,y);
        this.birthday = date;
    }
    public String getName()
    {
        return name;
    }

    public Date getBirthday() 
    {
        return birthday;
    }

    public void setName(String name) 
    {
        this.name = name;
    }

    public void setBirthday(Date birthday) 
    {
        this.birthday = birthday;
    }

    public String toString() 
    {
        return name + "'s birthday is " + birthday;
    }
}
