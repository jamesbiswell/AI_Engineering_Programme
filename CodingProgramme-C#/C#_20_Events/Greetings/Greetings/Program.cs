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
        static string lastMessage = string.Empty;

        // Define an event for handling Ctrl+C
        public static event EventHandler ConsoleClearRequested;

        /// <summary>
        /// Main entry point for the application
        /// </summary>
        /// <param name="args">Arguments sent to the application main method</param>
        static void Main(string[] args)
        {
            try
            {
                // Subscribe to the ConsoleCancelKeyPress event
                Console.CancelKeyPress += new ConsoleCancelEventHandler(OnCancelKeyPress);
                ConsoleClearRequested += Program_ConsoleClearRequested;

                PersonManager personManager;
                CarManager carManager;
                FamilyManager familyManager = new FamilyManager(family);

                lastMessage = "Press <Control> + C at any time to clear the console.";
                Console.WriteLine(lastMessage);
                lastMessage = "Please enter your name:";
                Console.WriteLine(lastMessage);
                person.Name = Console.ReadLine();

                lastMessage = "Please enter your age:";
                Console.WriteLine(lastMessage);
                while (!int.TryParse(Console.ReadLine(), out newAge) || newAge < 0 || newAge > 120)
                {
                    lastMessage = "Please enter a valid number for your age (0-120):";
                    Console.WriteLine(lastMessage);
                }
                person.Age = newAge;

                personManager = new PersonManager(person);

                try
                {
                    newAge = personManager.AgeXYearsFromNow(5);
                    lastMessage = "Hello " + person.Name + Environment.NewLine +
                                  "You are " + person.Age + " years old." + Environment.NewLine +
                                  "In five years, you will be " + newAge + "." + Environment.NewLine +
                                  "In ten years, you will be " + personManager.AgeXYearsFromNow(10) + "." + Environment.NewLine +
                                  "Someone double your age is " + personManager.TwiceAge() + " years old.";
                    Console.WriteLine(lastMessage);
                }
                catch (Exception ex)
                {
                    lastMessage = "An error occurred while calculating future age: " + ex.Message;
                    Console.WriteLine(lastMessage);
                    ErrorLogger.LogError(ex);
                }

                carManager = new CarManager();

                try
                {
                    familyManager.AddFamilyMember(person);
                    familyManager.AddFamilyCar(carManager.InputCar(out lastMessage));
                    lastMessage = "Let's hope your " + car.Make + " " + car.Model + " is still going strong when you are " + (person.Age + 7) + " years old.";
                    Console.WriteLine(lastMessage);
                }
                catch (Exception ex)
                {
                    lastMessage = "An error occurred while adding the family car or member: " + ex.Message;
                    Console.WriteLine(lastMessage);
                    ErrorLogger.LogError(ex);
                }

                try
                {
                    lastMessage = personManager.YearsHistory();
                    Console.WriteLine(lastMessage);
                }
                catch (Exception ex)
                {
                    lastMessage = "An error occurred while generating years history: " + ex.Message;
                    Console.WriteLine(lastMessage);
                    ErrorLogger.LogError(ex);
                }

                do
                {
                    lastMessage = "What would you like to do next?" + Environment.NewLine +
                                  "1. Add a family member." + Environment.NewLine +
                                  "2. Add a family vehicle." + Environment.NewLine +
                                  "3. Exit";
                    Console.WriteLine(lastMessage);

                    optionSelected = ProcessMenu(Console.ReadLine());

                } while (optionSelected);
            }
            catch (Exception ex)
            {
                lastMessage = "An unexpected error occurred: " + ex.Message;
                Console.WriteLine(lastMessage);
                ErrorLogger.LogError(ex);
            }
        }

        /// <summary>
        /// Event handler for Ctrl+C
        /// </summary>
        private static void OnCancelKeyPress(object sender, ConsoleCancelEventArgs e)
        {
            // Prevent the application from exiting
            e.Cancel = true;

            // Raise the ConsoleClearRequested event
            ConsoleClearRequested?.Invoke(sender, EventArgs.Empty);
        }

        /// <summary>
        /// Event handler to clear the console
        /// </summary>
        private static void Program_ConsoleClearRequested(object sender, EventArgs e)
        {
            Console.Clear();
            Console.WriteLine("Console cleared. Press <Control> + C at any time to clear the console again.");
            if (!string.IsNullOrEmpty(lastMessage))
            {
                Console.WriteLine(lastMessage);
            }
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
                        lastMessage = "Adding a family member.";
                        familyManager.AddFamilyMember(personManager.InputPerson());
                        result = true;
                        break;
                    case "2":
                        lastMessage = "Adding a family vehicle.";
                        familyManager.AddFamilyCar(carManager.InputCar(out lastMessage));
                        result = true;
                        break;
                    case "3":
                        result = false;
                        break;
                    default:
                        lastMessage = "Your selection was invalid, please try again:";
                        Console.WriteLine(lastMessage);
                        result = true;
                        break;
                }

                personManager.DisplayDetails(family);
            }
            catch (Exception ex)
            {
                lastMessage = "An error occurred while processing your selection: " + ex.Message;
                Console.WriteLine(lastMessage);
                ErrorLogger.LogError(ex);
            }

            return result;
        }
    }
}
