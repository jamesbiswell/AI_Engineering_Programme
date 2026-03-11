using Greetings.Models;
using ITOLTaskManager.Business.Utils;

namespace Greetings.Services
{
    public class PersonManager
    {
        private readonly Person _person;

        /// <summary>
        /// Constructor to instantiate a new PersonManager class
        /// </summary>
        /// <param name="person">The person to work with in this class</param>
        public PersonManager(Person person)
        {
            _person = person;
        }

        /// <summary>
        /// Method to display a greeting of the name and age of the person
        /// </summary>
        public void DisplayDetails()
        {
            try
            {
                Console.WriteLine("Hello, " + _person.Name);
                Console.WriteLine("You are " + _person.Age + " years old.");
            }
            catch (Exception ex)
            {
                Console.WriteLine("Error displaying person details: " + ex.Message);
                ErrorLogger.LogError(ex);
            }
        }

        /// <summary>
        /// This will display the details of the family sent through, showing all members and all vehicles in the family
        /// </summary>
        /// <param name="displayFamily">The Family to display</param>
        public void DisplayDetails(Family displayFamily)
        {
            Console.WriteLine("Your Family:");
            foreach (Person familyMember in displayFamily.Members)
            {
                Console.WriteLine(familyMember.Name);
                Console.WriteLine(familyMember.Age);
            }

            Console.WriteLine("Family Vehicles:");
            foreach (Car familyVehicle in displayFamily.Vehicles)
            {
                Console.WriteLine(familyVehicle.Make);
                Console.WriteLine(familyVehicle.Model);
            }
        }

        /// <summary>
        /// This method will build up a string with the name and age of the person
        /// </summary>
        /// <returns>a string with the name</returns>
        public string GetDetailsToDisplay()
        {
            return "Hello " + _person.Name + Environment.NewLine + "You are " + _person.Age + " years old.";
        }

        /// <summary>
        /// This method will calculate how old a person will be in X years
        /// </summary>
        /// <param name="yearsToAdd">How many years to add</param>
        /// <returns>New value with the number of years added</returns>
        public int AgeXYearsFromNow(int yearsToAdd)
        {
            try
            {
                return checked(_person.Age + yearsToAdd);
            }
            catch (OverflowException ex)
            {
                Console.WriteLine("Age calculation overflowed.");
                ErrorLogger.LogError(ex);
                return -1;
            }
        }

        /// <summary>
        /// This method will calculate double the person's age
        /// </summary>
        /// <returns>The new value that is double the person's current age</returns>
        public decimal TwiceAge()
        {
            try
            {
                return checked(_person.Age * 2);
            }
            catch (OverflowException ex)
            {
                Console.WriteLine("Error calculating twice the age.");
                ErrorLogger.LogError(ex);
                return -1;
            }
        }

        /// <summary>
        /// This method will calculate when the person was born and then display their age at intervals of each year that they lived,
        /// along with a short message commenting on the person's age at that stage
        /// </summary>
        public string YearsHistory()
        {
            string lastMessage = string.Empty;
            try
            {
                int year = DateTime.Now.AddYears(-_person.Age).Year;

                lastMessage += Environment.NewLine;
                lastMessage += "You were born in the year: " + year + Environment.NewLine;
                lastMessage += "Here are the years of your life so far:" + Environment.NewLine;
                Console.WriteLine();

                if (_person.Age < 17)
                {
                    lastMessage += "You are too young to own a car." + Environment.NewLine;
                }
                else
                {
                    lastMessage += "You are of legal driving age." + Environment.NewLine;
                }

                for (int i = 0; i < _person.Age; i++)
                {
                    year++;
                    lastMessage += "In " + year + ", you turned " + (i + 1) + "." + Environment.NewLine;

                    switch (i)
                    {
                        case < 10:
                            lastMessage += "You were a child." + Environment.NewLine;
                            break;
                        case < 20:
                            lastMessage += "You were a teenager." + Environment.NewLine;
                            break;
                        case < 60:
                            lastMessage += "You were an adult." + Environment.NewLine;
                            break;
                        case >= 60:
                            lastMessage += "You are elderly." + Environment.NewLine;
                            break;
                    }
                }
            }
            catch (Exception ex)
            {
                Console.WriteLine("An error occurred while generating years history: " + ex.Message);
                ErrorLogger.LogError(ex);
            }

            return lastMessage;
        }

        /// <summary>
        /// This method will prompt the user for a name and age of a new person to be added
        /// </summary>
        /// <returns>A new Person class with the new values that were collected from the user</returns>
        public Person InputPerson()
        {
            string? name;
            int newAge = 0;

            Console.WriteLine("What is the name?");
            name = Console.ReadLine();

            Console.WriteLine("What is the age?");
            while (!int.TryParse(Console.ReadLine(), out newAge) || newAge < 0 || newAge > 120)
            {
                Console.WriteLine("Please enter a valid number for the age (between 0 and 120):");                
            }

            return new Person(name, newAge);
        }
    }
}
