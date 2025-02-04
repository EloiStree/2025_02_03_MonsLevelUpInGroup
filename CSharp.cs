
using System;
public class Etudiant
{
    public string m_nom;
    public int m_age;

}


public class HelloWorld
{
    public static void Main(string[] args)
    {
        //print("Hello World")
        Console.WriteLine("Hello Word");
        //name = "Eloi Stree"
        string name = "Eloi Stree";
        // var à pas utiliser
        var age = 35;
        age = age + 1;
        age += 1;
        age++;
        age++;

        object boiteA="1";
        object boiteB ="5";
        object boiteC = boiteA;
        boiteA = boiteB;
        boiteB = boiteC;


        try
        {
            age = age / 0;

        }catch(Exception e)
        {
            Console.WriteLine("YOU CAN4T DIVIED BY ZERO YOU DUMB FUCKER");
        }

        string[] listeEtudiant = new string[7];
        listeEtudiant[0] = "Gregory";
        listeEtudiant[0] = "Yannis";
        listeEtudiant[6] ="Daniel";
        //for i in range(7):
        for (int i = 0; i < 7; i+=2)
        {
            Console.WriteLine("Bonjour "+i+":" + listeEtudiant[i]);
        }
        listeEtudiant = new string[9];
        //listeEtudiant = null;
        //for (int i = 0; i < 9; i += 2)
        //{
        //    Console.WriteLine("Bonjour " + i + ":" + listeEtudiant[i]);
        //}

        List<int> ageInClassRoom = new List<int>();
        ageInClassRoom.Add(35);
        ageInClassRoom.Add(30);
        for (int i =0; i < 12; i+=3)
        {
            ageInClassRoom.Add(80+i);
        }
        for (int i = 0; i < 12; i += 1)
        {
            ageInClassRoom.Add(80 + i*3);
        }


        foreach (int ageInClass in ageInClassRoom)
        {
            Console.WriteLine("Age in class room: " + ageInClass);
        }

        Etudiant etudiant1 = new Etudiant();
        Console.WriteLine("Nom: " + etudiant1.m_nom.ToString());
        Console.WriteLine("Age: " + etudiant1.m_age);


        //Console.WriteLine("Bonjour " + listeEtudiant[0]);
        //Console.WriteLine("Bonjour " + listeEtudiant[6]);



        /*
        Console.WriteLine ("Age "+ age);
        
        // command =input("Next? ")
        Console.WriteLine ("Age to add ?");
        string command = Console.ReadLine();
        Console.WriteLine (command);
    
        int ageToAdd = int.Parse(command);
        Console.WriteLine ("Age to add:"+ageToAdd);
        */

        float earthAge = 5.90054f;
        Console.WriteLine(earthAge);
        int earthAgeAsInteger = (int)earthAge;
        Console.WriteLine(earthAgeAsInteger);

        int earthAgeAsIntegerRound = (int)Math.Round(earthAge);
        Console.WriteLine(earthAgeAsIntegerRound);

    }
}
