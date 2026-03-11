using System;
using System.Collections.Generic;
using System.Linq;
using Microsoft.EntityFrameworkCore;
using Greetings.Models;
using Greetings.Data;
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
                _family.Members = newMembers;
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

        /// <summary>
        /// Adds the current family (_family) to the database.
        /// </summary>
        /// <returns>True if the family was successfully saved; otherwise, false.</returns>
        public bool SaveFamily()
        {
            try
            {
                using (var db = new AppDbContext())
                {
                    db.Families.Add(_family);
                    db.SaveChanges();
                }
                return true;
            }
            catch (Exception ex)
            {
                Console.WriteLine("Error saving family: " + ex.Message);
                ErrorLogger.LogError(ex);
                return false;
            }
        }

        /// <summary>
        /// Retrieves all families saved in the database, including their members and vehicles.
        /// </summary>
        /// <returns>A list of families.</returns>
        public static List<Family> GetAllFamilies()
        {
            using (var db = new AppDbContext())
            {
                return db.Families
                         .Include(f => f.Members)
                         .Include(f => f.Vehicles)
                         .ToList();
            }
        }

        /// <summary>
        /// Deletes a family from the database by its unique identifier.
        /// </summary>
        /// <param name="familyId">The identifier of the family to delete.</param>
        /// <returns>True if deletion was successful; otherwise, false.</returns>
        public static bool DeleteFamily(int familyId)
        {
            try
            {
                using (var db = new AppDbContext())
                {
                    var familyToDelete = db.Families.FirstOrDefault(f => f.Id == familyId);
                    if (familyToDelete != null)
                    {
                        db.Families.Remove(familyToDelete);
                        db.SaveChanges();
                        return true;
                    }
                    return false;
                }
            }
            catch (Exception ex)
            {
                Console.WriteLine("Error deleting family: " + ex.Message);
                ErrorLogger.LogError(ex);
                return false;
            }
        }

    }
}
