using Greetings.Models;
using Greetings.Services;
using ITOLTaskManager.Business.Utils;

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
        /// <param name="args">Arguments sent to the application main method</param>
        static void Main(string[] args)
        {
            try
            {
                PersonManager personManager;
                CarManager carManager;
                FamilyManager familyManager = new FamilyManager(family);
                Console.CancelKeyPress += (sender, e) => { Bob(); };
                                
                Console.WriteLine("Please enter your name:");                
                person.Name = Console.ReadLine();

                Console.WriteLine("Please enter your age:");
                
                while (!int.TryParse(Console.ReadLine(), out newAge) || newAge < 0 || newAge > 120)
                {
                    Console.WriteLine("Please enter a valid number for your age (0-120):");
                    
                }
                person.Age = newAge;

                personManager = new PersonManager(person);

                try
                {
                    newAge = personManager.AgeXYearsFromNow(5);
                    Console.WriteLine("Hello " + person.Name);
                    Console.WriteLine("You are " + person.Age + " years old.");
                    Console.WriteLine("In five years, you will be " + newAge + ".");
                    Console.WriteLine("In ten years, you will be " + personManager.AgeXYearsFromNow(10) + ".");
                    Console.WriteLine("Someone double your age is " + personManager.TwiceAge() + " years old.");
                    
                }
                catch (Exception ex)
                {
                    Console.WriteLine("An error occurred while calculating future age: " + ex.Message);
                    
                    ErrorLogger.LogError(ex);
                }

                carManager = new CarManager();

                try
                {
                    familyManager.AddFamilyMember(person);
                    familyManager.AddFamilyCar(carManager.InputCar());
                    Console.WriteLine("Let's hope your " + car.Make + " " + car.Model + " is still going strong when you are " + (person.Age + 7) + " years old.");
                    
                }
                catch (Exception ex)
                {
                    Console.WriteLine("An error occurred while adding the family car or member: " + ex.Message);
                    
                    ErrorLogger.LogError(ex);
                }

                try
                {
                    personManager.YearsHistory();
                    
                }
                catch (Exception ex)
                {
                    Console.WriteLine("An error occurred while generating years history: " + ex.Message);
                    
                    ErrorLogger.LogError(ex);
                }

                do
                {
                    Console.WriteLine("What would you like to do next?");
                    Console.WriteLine("1. Add a family member.");
                    Console.WriteLine("2. Add a family vehicle.");
                    Console.WriteLine("3. Exit");
                    

                    optionSelected = ProcessMenu(Console.ReadLine());

                } while (optionSelected);
            }
            catch (Exception ex)
            {
                Console.WriteLine("An unexpected error occurred: " + ex.Message);
                
                ErrorLogger.LogError(ex);
            }
        }
        static private void Bob()
        {
            Console.WriteLine();
        }

        /// <summary>
        /// Static method that will process the menu when it gets inputted
        /// </summary>
        /// <param name="selected">The option selected by the user</param>
        /// <returns>True if the selection was valid and the program will not yet exit; false if user wants to exit</returns>
        static private bool ProcessMenu(string selected)
        {
            PersonManager personManager = new PersonManager(person);
            CarManager carManager = new CarManager(car);
            FamilyManager familyManager = new FamilyManager(family);

            bool result = false;

            try
            {
                switch (selected)
                {
                    case "1":
                        Console.WriteLine("Adding a family member.");
                        familyManager.AddFamilyMember(personManager.InputPerson());
                        result = true;
                        break;
                    case "2":
                        Console.WriteLine("Adding a family vehicle.");
                        familyManager.AddFamilyCar(carManager.InputCar());
                        result = true;
                        break;
                    case "3":
                        result = false;
                        break;
                    default:
                        Console.WriteLine("Your selection was invalid, please try again:");
                        
                        result = true;
                        break;
                }

                personManager.DisplayDetails(family);
            }
            catch (Exception ex)
            {
                Console.WriteLine("An error occurred while processing your selection: " + ex.Message);
                
                ErrorLogger.LogError(ex);
            }

            return result;
        }
    }
}
