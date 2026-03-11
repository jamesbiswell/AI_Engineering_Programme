
Console.Write("Welcome to the Wonderfull world of ");
Console.WriteLine("C#.");

Console.WriteLine("Please enter your name:");

string? name = Console.ReadLine();

Console.WriteLine("Please enter your name:");

string? age = Console.ReadLine();

int futureAge = int.Parse(age) + 10;


Console.WriteLine("Hello " + name);
Console.WriteLine("in 10 years you will be " + futureAge.ToString());
