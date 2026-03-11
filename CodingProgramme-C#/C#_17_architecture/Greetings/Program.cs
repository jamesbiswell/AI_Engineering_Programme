
using Microsoft.VisualBasic;
using System.ComponentModel;
using System.ComponentModel.DataAnnotations;
using System.ComponentModel.Design;
using System.Dynamic;
using Greetings.Models;
using Greetings.Services;

namespace Greetings
{
    class Program
    {
        static Person person = new Person(string.Empty, 0);
        static Car car = new Car();
        static Family family = new Family();
        static int newAge;
        static bool optionSelected = false;        

        /// <summary>
        /// Main entry point for the application
        /// </summary>
        /// <param name="args">arguments sent to the application main method</param>
        static void Main(string[] args)
        {
            PersonManager personManager;
            CarManager carManager;
            FamilyManager familyManager = new FamilyManager(family);

            Console.WriteLine("Please enter your name:");
            person.Name = Console.ReadLine();

            Console.WriteLine("Please enter your age:");
            while (!int.TryParse(Console.ReadLine(), out newAge))
            {
                Console.WriteLine("Please enter a valid number for your age:");
            }

            person.Age = newAge;

            personManager = new PersonManager(person);

            newAge = personManager.AgeXYearsFromNow(5);

            Console.WriteLine("Hello " + person.Name);
            Console.WriteLine("You are " + person.Age + " years old,");
            Console.WriteLine("In five years you will be " + newAge);
            Console.WriteLine("In ten years you will be " + personManager.AgeXYearsFromNow(10));
            Console.WriteLine("Someone double your age is " + personManager.TwiceAge() + " years old");

            carManager = new CarManager();

            familyManager.AddFamilyMember(person);
            familyManager.AddFamilyCar(carManager.InputCar());


            Console.WriteLine("let's hope your " + car.Make + " " + car.Model + " is still going strong when you are " + (person.Age + 7) + " years old.");


            personManager.YearsHistory();


            Console.WriteLine();
            Console.WriteLine();

            optionSelected = true;

            do
            {
                Console.WriteLine();
                Console.WriteLine();
                Console.WriteLine("What would you like to do next?");
                Console.WriteLine("1. Add a family member.");
                Console.WriteLine("2. Add a family vehicle.");
                Console.WriteLine("3. Exit");

                optionSelected = ProcessMenu(Console.ReadLine());

                Console.WriteLine();
                Console.WriteLine();

            } while (optionSelected);
        }

        /// <summary>
        /// Static method that will process the menu when it gets inputted
        /// </summary>
        /// <param name="selected">The option selected by the user</param>
        /// <returns>True if the the selection was valid and the program will not yet exit and false if user wants to exit</returns>
        static private bool ProcessMenu(string selected)
        {
            PersonManager personManager = new PersonManager(person);
            CarManager carManager = new CarManager(car);
            FamilyManager familyManager = new FamilyManager(family);

            bool result = false;

            switch (selected)
            {
                case "1":                    
                    familyManager.AddFamilyMember(personManager.InputPerson());
                    result = true;
                    break;
                case "2":
                    familyManager.AddFamilyCar(carManager.InputCar());
                    result = true;
                    break;
                case "3":
                    result = false;
                    break;
                default:
                    Console.WriteLine("Your selection was invalid, Please try again:");
                    result = true;
                    break;
            }

            personManager.DisplayDetails(family);

            return result;
        }

        


    }

}