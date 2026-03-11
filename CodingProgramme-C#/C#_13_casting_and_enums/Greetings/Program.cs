using Microsoft.VisualBasic;
using System.ComponentModel;
using System.ComponentModel.DataAnnotations;
using System.Dynamic;
 
class Program
{
    enum Month
    {
        January = 1,
        February = 2,
        March = 3,
        April = 4,
        May = 5,
        June = 6,
        July = 7,
        August = 8,
        September = 9,
        October = 10,
        November = 11,
        December = 12
    }
 
    enum Season
    {
        Summer,
        Autumn,
        Winter,
        Spring
    }
 
    static void Main(string[] args)
    {   
        Person person = new Person(string.Empty, 0);
        Car car = new Car();
        int newAge;
 
        int MonthOfTheYear = DateAndTime.Month(DateTime.Now);
        Month monthName;
        Season season = Season.Summer;
 
        monthName = (Month)MonthOfTheYear;
 
        if (MonthOfTheYear < 3 || MonthOfTheYear == 12)
        {
            season = Season.Winter;
        }
        else if (MonthOfTheYear >= 3 && MonthOfTheYear <= 5)
        {
            season = Season.Spring;
        }
        else if (MonthOfTheYear >= 6 && MonthOfTheYear <= 8)
        {
            season = Season.Summer;
        }
        else if (MonthOfTheYear >= 9 && MonthOfTheYear <= 11)
        {
            season = Season.Autumn;
        }
 
        Console.WriteLine("The current month of the year is: " + monthName);
        Console.WriteLine("The current season is: " + season);
        Console.ReadLine();
 
        Console.WriteLine("Please enter your name:");
        person.Name = Console.ReadLine();
 
 
        Console.WriteLine("Please enter your age:");
        person.Age = int.Parse(Console.ReadLine());
 
 
        Console.WriteLine("What is the make of your car?");
        car.Make = Console.ReadLine();
 
        Console.WriteLine("What model is your car?");
        car.Model = Console.ReadLine();
 
        newAge = person.AgeXYearsFromNow(5);
 
        Console.WriteLine("Hello " + person.Name);
        Console.WriteLine("You are " + person.Age + " years old,");
        Console.WriteLine("In five years you will be " + newAge);
        Console.WriteLine("In ten years you will be " + person.AgeXYearsFromNow(10));
        Console.WriteLine("Someone double your age is " + person.TwiceAge() + " years old");
 
        Console.WriteLine("let's hope your " + car.Make + " " + car.Model + " is still going strong when you are " + (person.Age + 7) + " years old.");
 
        person.YearsHistory();
    }
}
 
// Define the Person class
public class Person
{
    // Public property for Name
    public string? Name { get; set; }
 
    // Private property for Age
    public int Age { get; set; }    
 
 
    // Constructor to initialize Name and Age
    public Person(string name, int age)
    {
        Name = name;
        Age = age;
    }
 
    public void DisplayDetails()
    {
        Console.WriteLine("Hello" + Name);
        Console.WriteLine("You are " + Age + "years old.");
    }
 
    public string GetDetailsToDisplay()
    {
        string returnValue = string.Empty;
 
        returnValue = "Hello" + Name + Environment.NewLine;
        returnValue = "You are " + Age + "years old.";
 
        return returnValue;
    }
 
    public int AgeXYearsFromNow(int yearsToAdd)
    {
        int newAge = Age + yearsToAdd;
        return newAge;
    }
 
    public decimal TwiceAge()
    {
        return Age * 2;
    }
 
    public void YearsHistory() 
    {
        int year = DateAndTime.Now.AddYears(Age * -1).Year;
 
        Console.WriteLine();
        Console.WriteLine();
 
        Console.WriteLine(" You were born in the year: " + year);
        Console.WriteLine("Here are the years of your life so far.");
 
        Console.WriteLine();
 
        if(Age < 17)
            Console.WriteLine("You are too young to own a car");
        else
            Console.WriteLine("You are of legal driving age");
 
 
        for (int i = 0; i < Age; i++)
        {            
            year++;            
 
            Console.WriteLine("In " + year + " you turned " + (i + 1));
 
            switch(i)
            {
                case < 10:
                    Console.WriteLine("You were a child");
                    break;
                case < 20:
                    Console.WriteLine("You were a teenager");
                    break;
                case < 60:
                    Console.WriteLine("You were a grown up");
                    break;
                case > 59:
                    Console.WriteLine("You are old");
                    break;
            }
        }
 
    }
 
}
 
// Define the Car class
public class Car
{
    // Public properties for Car's Make and Model
    public string? Make { get; set; }
    public string? Model { get; set; }
 
    // Method to display car information
    public void DisplayCarInfo()
    {
        Console.WriteLine($"Car: {Make} {Model}");
    }
}
 
public class Family
{
    public Person[] Members { get; set;}
    public List<Car> Vehicles { get; set;}
 
    public Family()
    {
        Members = new Person[0];
        Vehicles = new List<Car>();
    }
}
 
