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


                Console.WriteLine(" -------------------------------------------------------");
                Console.WriteLine("|           Welcome to the Greetings APP!!              |");
                Console.WriteLine("|                                                       |");
                Console.WriteLine("|                                                       |");
                Console.WriteLine("| Save families by adding family members and vehicles   |");
                Console.WriteLine(" -------------------------------------------------------");


                lastMessage = "Press <Control> + C at any time to clear the console.";
                Console.WriteLine(lastMessage);
                
                do
                {
                    lastMessage = string.Concat(
                        $"What would you like to do next?{Environment.NewLine}",
                        "1. Add a family member.", Environment.NewLine,
                        "2. Add a family vehicle.", Environment.NewLine,
                        "3. Database operations.", Environment.NewLine,
                        "4. View fun info Details.", Environment.NewLine,                        
                        "5. Exit"
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
                        lastMessage = "Display fun details.";
                        ViewFunDetails();
                        result = true;
                        break;
                    case "5":
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


        /// <summary>
        /// This method will simply call the database manager to display the menu for database operations
        /// </summary>
        private static void ViewDBFamilies()
        {   
            DbManager dbManager = new DbManager(family);

            // Call the method to display the db menu
            dbManager.DisplayDbMenu(out lastMessage);

        }

        /// <summary>
        /// This method will simply let the user select a specific person for the 
        /// </summary>
        private static void ViewFunDetails()
        {
            // Declarations
            string strSelected = string.Empty;
            int intSelected = 0;
            lastMessage = string.Empty;
            PersonManager personManager = new PersonManager(new Person(string.Empty,0));

            do
            {
                // First check if there are perople to display yet
                if (family.Members.Count < 1)
                {
                    Console.WriteLine("No family members to display yet, add family members...");
                    Console.WriteLine("Press enter key to return...");
                    Console.ReadLine();
                    return;
                }

                lastMessage += string.Concat("Which family member do you want to view fun facts for?",Environment.NewLine);

                for (int counter = 0; counter < family.Members.Count; counter++)
                {
                    lastMessage += string.Concat((counter + 1).ToString(), ".", family.Members[counter].Name, Environment.NewLine);
                }


                Console.WriteLine(lastMessage);
                strSelected = Console.ReadLine();

                if ((!int.TryParse(strSelected, out intSelected))||
                     intSelected < 0 || 
                     intSelected > family.Members.Count)
                {
                    Console.WriteLine("That selection was not valid. Please try again...");
                }
                else 
                {
                       personManager = new PersonManager(family.Members[intSelected -1]);
                }
            } while (intSelected == 0);


            // Display age details for the person
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


            // Display Years History for the person
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
        }
    }
}
