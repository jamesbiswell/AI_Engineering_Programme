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

        public static event EventHandler ConsoleClearRequested;

        static void Main(string[] args)
        {
            try
            {
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
                    lastMessage = string.Concat(
                        $"Hello {person.Name}", Environment.NewLine,
                        $"You are {person.Age} years old.", Environment.NewLine,
                        $"In five years, you will be {newAge}.", Environment.NewLine,
                        $"In ten years, you will be {personManager.AgeXYearsFromNow(10)}.", Environment.NewLine,
                        $"Someone double your age is {personManager.TwiceAge()} years old."
                    );
                    Console.WriteLine(lastMessage);
                }
                catch (Exception ex)
                {
                    lastMessage = string.Concat("An error occurred while calculating future age: ", ex.Message);
                    Console.WriteLine(lastMessage);
                    ErrorLogger.LogError(ex);
                }

                carManager = new CarManager();

                try
                {
                    familyManager.AddFamilyMember(person);
                    familyManager.AddFamilyCar(carManager.InputCar(out lastMessage));
                    lastMessage = string.Concat("Let's hope your ", car.Make, " ", car.Model, " is still going strong when you are ", (person.Age + 7), " years old.");
                    Console.WriteLine(lastMessage);
                }
                catch (Exception ex)
                {
                    lastMessage = string.Concat("An error occurred while adding the family car or member: ", ex.Message);
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
                    lastMessage = string.Concat("An error occurred while generating years history: ", ex.Message);
                    Console.WriteLine(lastMessage);
                    ErrorLogger.LogError(ex);
                }

                do
                {
                    lastMessage = string.Concat(
                        $"What would you like to do next?{Environment.NewLine}",
                        "1. Add a family member.", Environment.NewLine,
                        "2. Add a family vehicle.", Environment.NewLine,
                        "3. Database operations.", Environment.NewLine,
                        "4. Exit"
                    );
                    Console.WriteLine(lastMessage);

                    optionSelected = ProcessMenu(Console.ReadLine());

                } while (optionSelected);
            }
            catch (Exception ex)
            {
                lastMessage = string.Concat("An unexpected error occurred: ", ex.Message);
                Console.WriteLine(lastMessage);
                ErrorLogger.LogError(ex);
            }
        }

        private static void OnCancelKeyPress(object sender, ConsoleCancelEventArgs e)
        {
            e.Cancel = true;
            ConsoleClearRequested?.Invoke(sender, EventArgs.Empty);
        }

        private static void Program_ConsoleClearRequested(object sender, EventArgs e)
        {
            Console.Clear();
            Console.WriteLine("Console cleared. Press <Control> + C at any time to clear the console again.");
            if (!string.IsNullOrEmpty(lastMessage))
            {
                Console.WriteLine(lastMessage);
            }
        }

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
                        lastMessage = "Working with the database.";
                        ViewDBFamilies();
                        result = true;
                        lastMessage = string.Concat(
                            $"What would you like to do next?{Environment.NewLine}",
                            "1. Add a family member.", Environment.NewLine,
                            "2. Add a family vehicle.", Environment.NewLine,
                            "3. Database operations.", Environment.NewLine,
                            "4. Exit"
                        );
                        break;
                    case "4":
                        result = false;
                        break;
                    default:
                        lastMessage = "Your selection was invalid, please try again:";
                        Console.WriteLine(lastMessage);
                        result = true;
                        break;
                }

            }
            catch (Exception ex)
            {
                lastMessage = string.Concat("An error occurred while processing your selection: ", ex.Message);
                Console.WriteLine(lastMessage);
                ErrorLogger.LogError(ex);
            }

            return result;
        }

        private static void ViewDBFamilies()
        {   
            DbManager dbManager = new DbManager(family);

            // Call the method to display the db menu
            dbManager.DisplayDbMenu(out lastMessage);

        }
    }
}
