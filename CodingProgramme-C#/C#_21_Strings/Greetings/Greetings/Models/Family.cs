using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;

namespace Greetings.Models
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

    }
}
