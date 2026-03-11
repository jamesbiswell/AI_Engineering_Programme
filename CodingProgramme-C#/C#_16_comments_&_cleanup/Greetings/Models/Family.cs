using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;

namespace Greetings
{
    /// <summary>
    /// This class represents a family consisting of Family Members(person class) as well as family vehicles(car class)
    /// </summary>
    public class Family
    {
        public Person[] Members { get; set; }
        public List<Car> Vehicles { get; set; }

        /// <summary>
        /// Constructor initializing new empty lists for family members and cars
        /// </summary>
        public Family()
        {
            Members = new Person[0];
            Vehicles = new List<Car>();
        }

        /// <summary>
        /// This method is used to add a new family member
        /// </summary>
        /// <param name="person">The person to be added to the family</param>
        /// <returns>True if successfull and false if not</returns>
        public bool AddFamilyMember(Person person)
        {
            Person[] newMembers = new Person[Members.Count() + 1];
            int personCount = 0;

            foreach (Person member in Members)
            {
                newMembers[personCount] = member;
                personCount++;
            }

            newMembers[personCount] = person;

            Members = newMembers;

            return true;

        }

        /// <summary>
        /// This will add a new car as a family vehicle
        /// </summary>
        /// <param name="car">The car to be added to the family</param>
        /// <returns>True if successfull and false if not</returns>
        public bool AddFamilyCar(Car car)
        {
            Vehicles.Add(car);
            return true;
        }

    }
}
