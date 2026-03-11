using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;

namespace Greetings.Models
{
    /// <summary>
    /// This class represents a car entity that can be part of a family
    /// </summary>
    public class Car
    {
        /// <summary>
        /// Defines the make of the Car
        /// </summary>
        public enum MakesOfCars
        {
            Mercedes,
            BMW,
            LandRover,
            Toyota,
            Ford
        }

        /// <summary>
        /// The make of the car to be selected
        /// </summary>
        public MakesOfCars Make { get; set; }

        /// <summary>
        /// The Model of the car to be selected
        /// </summary>
        public string? Model { get; set; }
    }
}
