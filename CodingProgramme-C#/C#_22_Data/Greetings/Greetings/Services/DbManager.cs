using Greetings.Models;
using ITOLTaskManager.Business.Utils;
using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;
using static System.Runtime.InteropServices.JavaScript.JSType;

namespace Greetings.Services
{
    public class DbManager
    {
        Family currentFamily;
        bool currentFamilyAdded = false;
        string strLastMessage = string.Empty;

        public DbManager(Family parCurrentFamily) 
        {
            currentFamily = parCurrentFamily;
        }

        /// <summary>
        /// This will display a menu to the user to select which database operation they wish to perform.
        /// </summary>
        /// <param name="lastMessage">The last message displayted to the user, in case they clear the screen</param>
        public void DisplayDbMenu(out string lastMessage)
        {
            // Declarations
            lastMessage = string.Empty;
            bool result = true;
            bool corretInput;
            string strOptionSelected = string.Empty;
            bool firstTime = true;

            try
            {
                do
                {
                    switch (strOptionSelected)
                    {
                        case "1":
                            displayCurrentDbFamilies();
                            result = true;
                            break;
                        case "2":
                            AddCurrentFamily();
                            result = true;
                            break;
                        case "3":
                            do
                            {
                                corretInput = displaySpecificDbFamily();
                            }
                            while (!corretInput);
                            result = true;
                            break;
                        case "4":
                            do
                            {
                                corretInput = deleteSpecificDbFamily();
                            }
                            while (!corretInput);
                            result = true;
                            break;
                        case "5":
                            result = false;
                            return;
                            break;
                        default:
                            if (!firstTime)
                            {
                                firstTime = false;
                                lastMessage = "Your selection was invalid, please try again:";
                                Console.WriteLine(lastMessage);
                            }
                            result = true;

                            break;
                    }

                    lastMessage = string.Concat(
                                    $"What would you like to do next?{Environment.NewLine}",
                                    "1. View current saved families.", Environment.NewLine,
                                    "2. Add the current family to the database.", Environment.NewLine,
                                    "3. Display a specific family.", Environment.NewLine,
                                    "4. Delete a specific family.", Environment.NewLine,
                                    "5. Back to Main Menu.");
                    Console.WriteLine(lastMessage);
                    strOptionSelected = Console.ReadLine();
                }
                while (result);
            }
            catch (Exception ex)
            {
                strLastMessage = string.Concat("An error occurred while displaying the database menu: ", ex.Message);
                Console.WriteLine(strLastMessage);
                ErrorLogger.LogError(ex);
            }
            finally
            {
                lastMessage = strLastMessage;
            }
        }

        /// <summary>
        /// This method will display the families currently in the database
        /// </summary>
        private void displayCurrentDbFamilies()
        {
            List<Family> families = new List<Family>();
            string strFamilyDisplay = string.Empty;

            try
            {

                families = FamilyManager.GetAllFamilies();

                foreach (Family family in families)
                {
                    strFamilyDisplay += string.Concat("--------------------------------------",Environment.NewLine,
                                                      "Family ID: ", family.Id, Environment.NewLine,
                                                      "Family of : ", family.Members[0].Name,Environment.NewLine,
                                                      "--------------------------------------", Environment.NewLine);
                }

                Console.WriteLine(strFamilyDisplay);
            }
            catch (Exception ex)
            {
                strLastMessage = string.Concat("An error occurred while displaying all families: ", ex.Message);
                Console.WriteLine(strLastMessage);
                ErrorLogger.LogError(ex);
            }
        }

        private void AddCurrentFamily()
        {
            FamilyManager  familyManager = new FamilyManager(currentFamily);

            try
            {
                if (familyManager.SaveFamily())
                {
                    strLastMessage = string.Concat("The current family was saved to the database.", Environment.NewLine,
                                                    "Press Any key to continue...");
                    Console.Write(strLastMessage);
                    Console.ReadLine();
                    currentFamilyAdded = true;
                }
                else
                {
                    strLastMessage = string.Concat("Something went wrong. The current family was NOT saved to the database.", Environment.NewLine,
                                                   "Press Any key to continue...");
                    Console.ReadLine();
                }
            }
            catch (Exception ex)
            {
                strLastMessage = string.Concat("An error occurred while Adding the current family: ", ex.Message);
                Console.WriteLine(strLastMessage);
                ErrorLogger.LogError(ex);
            }
        }

        /// <summary>
        /// Displays the current failies and then asks user to select which family to display in detail
        /// </summary>
        /// <returns>True if a family was selected and displayed, or false for an invalid input. </returns>
        private bool displaySpecificDbFamily()
        {
            string strFamilyDisplay = string.Empty;
            string strFamilySelected = "0";
            bool blnFamilySelected = false;


            displayCurrentDbFamilies();

            try
            {

                strFamilyDisplay = "Which family details do you want to view? Please enter the id:";
                Console.WriteLine(strFamilyDisplay);

                strFamilySelected = Console.ReadLine();

                foreach (Family family in FamilyManager.GetAllFamilies())
                {
                    if (family.Id.ToString() == strFamilySelected)
                    {
                        blnFamilySelected = true;
                        // Family Members
                        // --------------
                        strFamilyDisplay += string.Concat("Family ID: ", family.Id, Environment.NewLine,
                                                          "Members: ", Environment.NewLine,
                                                          "--------", Environment.NewLine);
                        foreach (Person person in family.Members)
                        {
                            strFamilyDisplay += string.Concat("Name: ", person.Name, Environment.NewLine,
                                                               "Age: ", person.Age, Environment.NewLine,
                                                               "------------------", Environment.NewLine);
                        }

                        // Vehicles
                        // --------
                        strFamilyDisplay += string.Concat("Vehicles: ", Environment.NewLine,
                                                          "--------", Environment.NewLine);
                        foreach (Car car in family.Vehicles)
                        {
                            strFamilyDisplay += string.Concat("Make: ", car.Make, Environment.NewLine,
                                                               "Model: ", car.Model, Environment.NewLine,
                                                               "-----------------", Environment.NewLine);
                        }
                    }
                }
            }
            catch (Exception ex)
            {
                strLastMessage = string.Concat("An error occurred while displaying a specific family: ", ex.Message);
                Console.WriteLine(strLastMessage);
                ErrorLogger.LogError(ex);
            }

            // Display the family
            if (blnFamilySelected)
            {
                Console.WriteLine(strFamilyDisplay);
                return true;
            }
            else
            {
                Console.WriteLine("The family id selected was not valid. Please try again:");
                return false;
            }


        }

        private bool deleteSpecificDbFamily()
        {            
            string strFamilySelected = "0";
            string strFamilyDisplay = string.Empty;
            bool blnFamilySelected = false;


            displayCurrentDbFamilies();

            try
            {

                strFamilyDisplay = "Which family do you want to delete? Please enter the id:";
                Console.WriteLine(strFamilyDisplay);
                strFamilySelected = Console.ReadLine();

                foreach (Family family in FamilyManager.GetAllFamilies())
                {
                    if (family.Id.ToString() == strFamilySelected)
                    {
                        blnFamilySelected = true;
                    }
                }

                // Display the family
                if (blnFamilySelected)
                {
                    string confirmDelete = "0";
                    Console.WriteLine(string.Concat("Are you sure you wish to DELETE this family with ID: ", strFamilySelected, " Confirm by entering 'Y'"));
                    confirmDelete = Console.ReadLine();

                    if (confirmDelete.ToLower() == "y")
                    {
                        int intFamilyID = 0;

                        if (int.TryParse(strFamilySelected, out intFamilyID))
                        {
                            if (FamilyManager.DeleteFamily(intFamilyID))
                            {
                                strFamilyDisplay = string.Concat("The Famliy with ID: ", strFamilySelected, " was deleted");
                            }
                            else
                            {
                                strFamilyDisplay = string.Concat("Something went wrong and the Famliy with ID: ", strFamilySelected, " was NOT deleted");
                            }
                        }
                    }
                    else
                    {
                        strFamilyDisplay = string.Concat("Famliy with ID: ", strFamilySelected, " was NOT deleted");
                    }

                    Console.WriteLine(strFamilyDisplay);

                    return true;
                }
                else
                {
                    Console.WriteLine("The family id selected was not valid. Please try again:");
                    return false;
                }
            }
            catch (Exception ex)
            {
                strLastMessage = string.Concat("An error occurred while deleting a family: ", ex.Message);
                Console.WriteLine(strLastMessage);
                ErrorLogger.LogError(ex);
                return false;
            }
        }
    }
}