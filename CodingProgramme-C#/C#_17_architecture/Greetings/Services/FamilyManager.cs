using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;
using Greetings.Models;

namespace Greetings.Services
{
    internal class FamilyManager
    {
        private Family _family;

        /// <summary>
        /// Constructor to initialize a new familyManager object to handle all actions relating to families starting with a blank one
        /// </summary>        
        public FamilyManager()
        {
            _family = new Family();
        }

        /// <summary>
        /// Constructor to initialize a new familyManager object to handle all actions relating to families
        /// </summary>
        /// <param name="family">The new family object to work with</param>
        public FamilyManager(Family family)
        {
            _family = family;
        }

        /// <summary>
        /// This method is used to add a new family member
        /// </summary>
        /// <param name="person">The person to be added to the family</param>
        /// <returns>True if successfull and false if not</returns>
        public bool AddFamilyMember(Person person)
        {
            Person[] newMembers = new Person[_family.Members.Count() + 1];
            int personCount = 0;

            foreach (Person member in _family.Members)
            {
                newMembers[personCount] = member;
                personCount++;
            }

            newMembers[personCount] = person;

            _family.Members = newMembers;

            return true;

        }

        /// <summary>
        /// This will add a new car as a family vehicle
        /// </summary>
        /// <param name="car">The car to be added to the family</param>
        /// <returns>True if successfull and false if not</returns>
        public bool AddFamilyCar(Car car)
        {
            _family.Vehicles.Add(car);
            return true;
        }
    }
}
