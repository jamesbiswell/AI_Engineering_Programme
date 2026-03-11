using Microsoft.VisualBasic;
using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;

namespace Greetings.Models
{
    /// <summary>
    /// This class represents a person who can be part of a family
    /// </summary>
    public class Person
    {

        /// <summary>
        /// Primary key for EF
        /// </summary>
        public int Id { get; set; }

        /// <summary>
        /// Name is the name of the person
        /// </summary>
        public string? Name { get; set; }

        /// <summary>
        /// This is the age of the person
        /// </summary>
        public int Age { get; set; }

        /// <summary>
        /// Foreign Key for Family (One-to-Many)
        /// </summary>
        public int FamilyId { get; set; }
        public Family? Family { get; set; }


        /// <summary>
        /// Constructor to instantiate a new person with values
        /// </summary>
        /// <param name="name">The name of the new person</param>
        /// <param name="age">The Age of the new person</param>
        public Person(string? name, int age)
        {
            Name = name;
            Age = age;
        }
    }
}
