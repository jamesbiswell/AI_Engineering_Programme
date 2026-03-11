using Microsoft.VisualBasic;
using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;

namespace Greetings
{
    /// <summary>
    /// This class represents a person who can be part of a family
    /// </summary>
    public class Person
    {
        /// <summary>
        /// Name is the name of the person
        /// </summary>
        public string? Name { get; set; }

        /// <summary>
        /// This is the age of the person
        /// </summary>
        public int Age { get; set; }


        /// <summary>
        /// 
        /// </summary>
        /// <param name="name"></param>
        /// <param name="age"></param>
        public Person(string name, int age)
        {
            Name = name;
            Age = age;
        }

        /// <summary>
        /// Method to display a greeting of the name and age of the person
        /// </summary>
        public void DisplayDetails()
        {
            Console.WriteLine("Hello" + Name);
            Console.WriteLine("You are " + Age + "years old.");
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
            foreach (Car familyVehicles in displayFamily.Vehicles)
            {
                Console.WriteLine(familyVehicles.Make);
                Console.WriteLine(familyVehicles.Model);
            }
        }

        /// <summary>
        /// Method will build up a string with the name and age of the person
        /// </summary>
        /// <returns>a string with the na,e</returns>
        public string GetDetailsToDisplay()
        {
            string returnValue = string.Empty;

            returnValue = "Hello" + Name + Environment.NewLine;
            returnValue = "You are " + Age + "years old.";

            return returnValue;
        }

        /// <summary>
        /// This method will calculate how old a person will be in X years
        /// </summary>
        /// <param name="yearsToAdd">How many years to add</param>
        /// <returns>New value with the number of years added</returns>
        public int AgeXYearsFromNow(int yearsToAdd)
        {
            int newAge = Age + yearsToAdd;
            return newAge;
        }

        /// <summary>
        /// This method will calculate double the person's age
        /// </summary>
        /// <returns>The new value that is double the person's current age</returns>
        public decimal TwiceAge()
        {

            return Age * 2;

        }

        /// <summary>
        /// This method will calculate when the person was born and then display their age at intervals of each year that they lived,
        /// along with a short message commenting on the person's age at that stage
        /// </summary>
        public void YearsHistory()
        {
            int year = DateAndTime.Now.AddYears(Age * -1).Year;

            Console.WriteLine();
            Console.WriteLine();

            Console.WriteLine(" You were born in the year: " + year);
            Console.WriteLine("Here are the years of your life so far.");

            Console.WriteLine();

            if (Age < 17)
                Console.WriteLine("You are too young to own a car");
            else
                Console.WriteLine("You are of legal driving age");


            for (int i = 0; i < Age; i++)
            {
                year++;

                Console.WriteLine("In " + year + " you turned " + (i + 1));

                switch (i)
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

        /// <summary>
        /// This method will prompt the user for a name and age of a new person to be added
        /// </summary>
        /// <returns>a new Person class with the new values that was collected from the user</returns>
        public Person InputPerson()
        {
            string? name = string.Empty;
            int newAge = 0;


            Console.WriteLine("What is the name?");
            name = Console.ReadLine();
            Console.WriteLine("What is the age?");
            while (!int.TryParse(Console.ReadLine(), out newAge))
            {
                Console.WriteLine("Please enter a valid number for your age:");
            }

            return new Person(name, newAge);            
        }

    }
}
