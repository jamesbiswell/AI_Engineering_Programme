using Greetings.Models;
using ITOLTaskManager.Business.Utils;

namespace Greetings.Services
{
    internal class FamilyManager
    {
        private readonly Family _family;

        /// <summary>
        /// Constructor to initialize a new FamilyManager object to handle all actions relating to families starting with a blank one
        /// </summary>
        public FamilyManager()
        {
            _family = new Family();
        }

        /// <summary>
        /// Constructor to initialize a new FamilyManager object to handle all actions relating to families
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
        /// <returns>True if successful and false if not</returns>
        public bool AddFamilyMember(Person person)
        {
            try
            {
                List<Person> newMembers = _family.Members.ToList();
                newMembers.Add(person);
                _family.Members = newMembers.ToArray();
                return true;
            }
            catch (Exception ex)
            {
                Console.WriteLine(string.Concat("Error adding family member: ", ex.Message));
                ErrorLogger.LogError(ex);
                return false;
            }
        }

        /// <summary>
        /// This will add a new car as a family vehicle
        /// </summary>
        /// <param name="car">The car to be added to the family</param>
        /// <returns>True if successful and false if not</returns>
        public bool AddFamilyCar(Car car)
        {
            try
            {
                _family.Vehicles.Add(car);
                return true;
            }
            catch (Exception ex)
            {
                Console.WriteLine(string.Concat("Error adding family car: ", ex.Message));
                ErrorLogger.LogError(ex);
                return false;
            }
        }
    }
}
