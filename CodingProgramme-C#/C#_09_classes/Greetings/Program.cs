
using System.ComponentModel;
using System.ComponentModel.DataAnnotations;
using System.Dynamic;

class Program
{
    static void Main(string[] args)
    {
        Person person = new Person(string.Empty, 0);
        Car car = new Car();

        Console.WriteLine("Please enter your name:");
        person.Name = Console.ReadLine();


        Console.WriteLine("Please enter your age:");
        person.Age = int.Parse(Console.ReadLine());


        Console.WriteLine("What is the make of your car?");
        car.Make = Console.ReadLine();

        Console.WriteLine("What model is your car?");
        car.Model = Console.ReadLine();

        Console.WriteLine("Hello " + person.Name);
        Console.Write("You are " + (person.Age) + " years old,");
        Console.WriteLine("let's hope your " + car.Make + " " + car.Model + " will keep going strong for another 5 years.");
    }
}

// Define the Person class
class Person
{
    // Public property for Name
    public string Name { get; set; }

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

        returnValue  = "Hello" + Name + Environment.NewLine;
        returnValue = "You are " + Age + "years old.";

        return returnValue;
    }

}

// Define the Car class
public class Car
{
    // Public properties for Car's Make and Model
    public string Make { get; set; }
    public string Model { get; set; }

    // Method to display car information
    public void DisplayCarInfo()
    {
        Console.WriteLine($"Car: {Make} {Model}");
    }
}

