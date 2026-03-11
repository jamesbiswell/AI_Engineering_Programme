using Greetings.Models;
using ITOLTaskManager.Business.Utils;

namespace Greetings.Services
{
    public class CarManager
    {
        private readonly Car _car;

        /// <summary>
        /// Constructor not sending through a car but starting with a blank one
        /// </summary>
        public CarManager()
        {
            _car = new Car();
        }

        /// <summary>
        /// Constructor receiving the car to work with
        /// </summary>
        /// <param name="car"></param>
        public CarManager(Car car)
        {
            _car = car;
        }

        /// <summary>
        /// This will display the make and model of the car to the console
        /// </summary>
        public void DisplayCarInfo()
        {
            try
            {
                Console.WriteLine($"Car: {_car.Make}, {_car.Model}");
            }
            catch (Exception ex)
            {
                Console.WriteLine(string.Concat("Error displaying car info: ", ex.Message));
                ErrorLogger.LogError(ex);
            }
        }

        /// <summary>
        /// This method will prompt the user to enter make and model for a new car entity
        /// </summary>
        /// <returns>The car class populated with the new values</returns>
        public Car InputCar(out string lastMessage)
        {
            Car newCar = new Car();
            bool optionSelected = false;

            lastMessage = string.Concat(
                "What is the make of your car?", Environment.NewLine,
                "Please enter one of the options below:", Environment.NewLine,
                "1 for Mercedes", Environment.NewLine,
                "2 for BMW", Environment.NewLine,
                "3 for LandRover", Environment.NewLine,
                "4 for Toyota", Environment.NewLine,
                "5 for Ford"
            );

            Console.WriteLine(lastMessage);

            do
            {
                try
                {
                    string input = Console.ReadLine();
                    switch (input)
                    {
                        case "1":
                            newCar.Make = Car.MakesOfCars.Mercedes;
                            optionSelected = true;
                            break;
                        case "2":
                            newCar.Make = Car.MakesOfCars.BMW;
                            optionSelected = true;
                            break;
                        case "3":
                            newCar.Make = Car.MakesOfCars.LandRover;
                            optionSelected = true;
                            break;
                        case "4":
                            newCar.Make = Car.MakesOfCars.Toyota;
                            optionSelected = true;
                            break;
                        case "5":
                            newCar.Make = Car.MakesOfCars.Ford;
                            optionSelected = true;
                            break;
                        default:
                            Console.WriteLine("Invalid selection, please try again.");
                            break;
                    }
                }
                catch (Exception ex)
                {
                    Console.WriteLine(string.Concat("Error setting car make: ", ex.Message));
                    ErrorLogger.LogError(ex);
                }
            } while (!optionSelected);

            lastMessage = "What model is your car?";
            Console.WriteLine(lastMessage);
            try
            {
                newCar.Model = Console.ReadLine();
            }
            catch (ArgumentException ex)
            {
                Console.WriteLine(string.Concat("Error: ", ex.Message));
                ErrorLogger.LogError(ex);
            }

            return newCar;
        }
    }
}