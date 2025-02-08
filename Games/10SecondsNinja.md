[![image](https://github.com/user-attachments/assets/96f33151-2b24-4871-a303-20c1252c37b0)
![image](https://github.com/user-attachments/assets/cdff7682-2e01-4c7d-92f3-47445279946a)](https://store.steampowered.com/app/271670/10_Second_Ninja/)  
https://store.steampowered.com/app/271670/10_Second_Ninja/



``` python

# https://github.com/EloiStree/2024_08_29_ScratchToWarcraft/tree/main


"""
LeftArrow	37	0x25	1037	2037
UpArrow	38	0x26	1038	2038
RightArrow	39	0x27	1039	2039
DownArrow	40	0x28	1040	2040
C	67	0x43	1067	2067
X	88	0x58	1088	2088
R	82	0x52	1082	2082
Z	90	0x5A	1090	2090
Escape	27	0x1B	1027	2027
Enter	13	0x0D	1013	2013

"""


class Ninja:
    left_arrow = 1037
    up_arrow = 1038
    right_arrow = 1039
    down_arrow = 1040
    c = 1067
    x = 1088
    r = 1082
    z = 1090
    enter= 1013
    escape= 1027
    
    
    def press_sword(): 
        return Ninja.x
    def release_sword():
        return Ninja.x+1000
    
    
    def press_jump():
        return Ninja.up_arrow
    def release_jump():
        return Ninja.up_arrow+1000
    
    def press_right():
        return Ninja.right_arrow
    def release_right():
        return Ninja.right_arrow+1000
    
    def press_left():
        return Ninja.left_arrow
    def release_left():
        return Ninja.left_arrow+1000
    
    def press_down():
        return Ninja.down_arrow
    def release_down():    
        return Ninja.down_arrow+1000
    
    def press_shuriken():
        return Ninja.z
    def release_shuriken():
        return Ninja.z+1000
    
    def press_restart():
        return Ninja.r
    def release_restart():
        return Ninja.r+1000
    
    
    def press_enter():
        return Ninja.enter
    def release_enter():
        return Ninja.enter+1000
    
    def press_escape():
        return Ninja.escape
    def release_escape():
        return Ninja.escape+1000
    
        


    
import socket
import struct
import time
def i(integer, ip, port):
    
    bytes = struct.pack("<i", integer)
    sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    sock.sendto(bytes, (ip, port))
    sock.close()
    
   

def ii(index, integer):
    bytes = struct.pack("<ii", index, integer)
    sock= socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    sock.sendto(bytes, (target_ip, target_port))
    sock.close()
    
    

if __name__ == "__main__":
    integer_to_send = 10  # Replace with the integer you want to send
    target_ip = "193.150.14.47"
    target_port = 3615
    
    while True:
        
        ii(0, Ninja.x)
        time.sleep(5)
        ii(0, Ninja.x+1000)
        time.sleep(1)
        
        ii(0, Ninja.press_right())
        time.sleep(1)
        ii(0, Ninja.release_right())
        
        ii(0, Ninja.press_jump())
        time.sleep(1)
        ii(0, Ninja.release_jump())
        
        ii(0, Ninja.press_left())
        time.sleep(1)
        ii(0, Ninja.release_left())
        
        ii(0, Ninja.press_down())
        time.sleep(1)
        ii(0, Ninja.release_down())

            
        ii(0, Ninja.press_shuriken())
        time.sleep(1)
        ii(0, Ninja.release_shuriken())
        time.sleep(1)
        
        
        ii(0, Ninja.press_restart())
        time.sleep(1)
        ii(0, Ninja.release_restart())
        
        ii(0, Ninja.press_enter())
        time.sleep(1)
        ii(0, Ninja.release_enter())
        
       
```


-----------------------------------
----------------------------------------

Introduction: https://youtu.be/gLs49QntNyM
Video:  https://youtu.be/4r52NHEQLxo

-------

[![Image](https://github.com/user-attachments/assets/dcc65d49-3959-4c50-b1f7-e961f6271bbf)](#3)
Voir 
- #3 
- https://github.com/EloiStree/HelloSharpForUnity3D/issues/171

----------------

- **10 Seconds Ninja** : ([Game](https://github.com/EloiStree/2025_02_03_MonsLevelUpInGroup/issues/3) [Workshop](https://github.com/EloiStree/2025_02_03_MonsLevelUpInGroup/issues/10))  
  - Vous permet d'apprendre ce qu'est une fonction, des paramètres, un thread et la gestion du temps.  
  - **Plan** :  
    - Apprendre la programmation avec Python  
    - Poser votre code sur GitHub  
    - Passer de Python à C# avec Visual Studio  

-------------------------------


Ce jeu *10 Second Ninja* est pour moi l'un des meilleurs moyens d'apprendre les bases de ce qu'est une boucle, une fonction, des paramètres, le temps et les threads.

Python est un langage qui, après Scratch, est fortement conseillé pour les débutants, mais toujours utilisé par les experts grâce à la puissance de PyPi. Il permet d'installer tout et n'importe quoi en un simple `pip install faireLeCafe`.

Comme le jeu n'est pas gratuit, et qu'il est plus amusant d'organiser des petits tournois pour le fun, nous avons 12 instances du jeu qui tournent sur un ordinateur en ligne, diffusant son écran sur Discord (et sur le projecteur quand je ne donne pas un cours).

Pour interagir avec ce jeu, un serveur reçoit vos messages sur un Raspberry Pi en République tchèque et envoie vos messages via un tunnel vers le PC de chez Shadow en France. Vous avez donc de 15 à 40 ms de latence à prendre en compte dans vos codes.

Le code pour faire cela ressemble à ceci :

```python
# Ceci est un commentaire, un code non exécuté 
"""
Ceci est un commentaire 
Sur plusieurs lignes
Non exécuté donc.
"""

# On importe du code pour faire du réseau
import socket

"""
On importe un code qui joue avec des 1 et des 0 pour faire du code binaire.
Exemple : 101010 = 42
"""
import struct

# Ce code vous permet de faire attendre votre programme 
import time

# On crée une petite variable où l'on stocke l'adresse de l'ordinateur à contacter
server_address = "apint.ddns.net"
# On stocke un numéro de port où une application devrait être appelée.
server_port = 3615

# Comme mes boîtes à outils ne fonctionnent qu'avec des entiers, on prépare un entier.
presser_touche_restart = 1038	  
relacher_touche_restart = presser_touche_restart + 1000


"""

Pour jouer à ce jeu, vous pouvez aller lire la documentation de mon outil :
https://github.com/EloiStree/2024_08_29_ScratchToWarcraft

Voici une liste des touches du jeu *10 Second Ninja* :
LeftArrow 37 0x25 1037 2037
UpArrow 38 0x26 1038 2038
RightArrow 39 0x27 1039 2039
DownArrow 40 0x28 1040 2040
C 67 0x43 1067 2067
X 88 0x58 1088 2088
R 82 0x52 1082 2082
Z 90 0x5A 1090 2090
Escape 27 0x1B 1027 2027
Enter 13 0x0D 1013 2013

"""

# Il faut choisir quelle fenêtre vous voulez jouer
# Attention 0 veut dire tout. Merci de ne pas faire de sabotage 
# Sinon, je sors des mots de passe et une authentification cryptographique ^^
# Je compte sur votre fair-play de groupe
player_index = 1  # de 1 à 12 

# Sujet un peu compliqué, mais il faut que vous m'envoyiez deux entiers sous format binaire
# dans un format que l'on appelle "little endian".

little_endian_data = struct.pack('<ii', player_index, 42)

# On initialise un code qui nous permettra d'envoyer des messages à un ordinateur
udp_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

# On dit au code de faire une chose à l'infini
while True:
    # On envoie à l'ordinateur distant sans attendre de réponse un message de deux fois 4 bytes ( 8 bytes)
    #  8 bytes ça ressemble à ceci : 
    # 11111111 11111111 11111111 11111111  |  11111111 11111111 11111111 11111111
    # Pour    
    # 1 et 1038
    # 1 et 10000111010
    # https://www.rapidtables.com/convert/number/decimal-to-binary.html?x=1
    udp_socket.sendto(little_endian_data, (server_address, server_port))
  
    # On attend un peu, 100 millisecondes
    time.sleep(0.1)

    # On relâche la touche
    # 1 et 100000100010
    udp_socket.sendto(little_endian_data, (server_address, server_port))

    # On attend 5 secondes pour recommencer la boucle 
    time.sleep(5)

"""
Voyez la simplicité du code Python :)
C'est magique.     
"""

```

De ce fait, nous allons, durant ces trois jours, apprendre les bases de la programmation en Python pour ensuite publier notre code en ligne sur GitHub et transitionner lentement vers du C# dans Visual Studio.

Le deuxième jour, nous allons apprendre les commandes : `add commit pull push`.  
Un cours sans Git chez moi, c'est comme une soupe au chou sans poivre. 
Un peu fade ^^.
Comme dirait mes anciens élèves : `Git good`.

Git est utilisé mondialement par les développeurs de tous les continents. 
Il existe d'autres systèmes, mais celui-ci vous ne pourrez pas y échapper 😉.

Le défi du deuxième jour, c'est moi qui exécute votre code sur mon ordinateur via le code que vous publiez sur Git.
Le but du jeu : 
- Pour le fun : faire un code publié sur GitHub qui, exécuté sur l'ordinateur d'un inconnu avec Python, arrive à passer le niveau.
- Pour Git : pratiquer Git sur GitHub.
- Pour C# : apprendre ce qu'est une classe avant que l'on passe à C# le troisième jour.

Les classes vont vous permettre de créer ce que l'on appelle des boîtes à outils.
Ces boîtes à outils, utilisées l'une après l'autre, vous permettent de faire un code spécifique à un niveau et donc de passer les niveaux du jeu.

Une fois que nous aurons pratiqué Python et Git, nous passerons progressivement à C# en utilisant le même exercice. Prenez votre code écrit en Python et entraînez-vous à le convertir en code C# dans Visual Studio. N'oubliez pas de sauvegarder votre code une fois stabilisé sur GitHub si vous souhaitez approfondir vos compétences en Git.

L'idée du troisième jour est simple : 
> Nous avons fait du Python.
> Comment on le fait en C# ?

Ce que vous avez appris durant ces trois jours vous sera bien utile... pour les deux jours à venir.  
La suite de l'atelier consiste à aller *"éliminer"* une personne de notoriété publique:
![Image](https://github.com/user-attachments/assets/997b1340-cd07-47df-bbcc-8c76925cde24)  
Les détails sont [ici](https://github.com/EloiStree/2025_02_03_MonsLevelUpInGroup/issues/14).

 



-----------------------------------
-----------------------------------


Une autre version utilisant mes libraries:

``` python
# pip install iid42 wowint
import iid42
import wowint
import time

# https://github.com/EloiStree?tab=repositories&q=pypi_&type=&language=&sort=
# https://github.com/EloiStree/pypi_iid
# https://github.com/EloiStree/pypi_wowint


from iid42 import *
from wowint import *

player : SendUdpIID = SendUdpIID("192.168.1.115",7073, True, True )

## WARNING 0 means all the games # Don't use it.
player_index : int = 0 # it allows to select the target game 0-4-12





def push_integer(int_value :int):
    player.push_index_integer_date_ntp_in_milliseconds(player_index, int_value,0)
    
    
    
def press_key_slow( key : int):
    time.sleep(0.1)
    push_integer(key)
    time.sleep(0.1)
    push_integer(key)

def press_enter():
    press_key_slow(IntMapping_10SecondsNinja.key_enter)
    

def press_escape():
    press_key_slow(IntMapping_10SecondsNinja.key_escape)
    
def press_restart():
    press_key_slow(IntMapping_10SecondsNinja.key_restart)

    
    
if __name__ == "__main__":
    
    press_restart()
    while True:
        time.sleep(1)
        push_integer(IntMapping_10SecondsNinja.key_right)
        time.sleep(1)
        push_integer(IntMapping_10SecondsNinja.key_right+1000)
        time.sleep(1)
        push_integer(IntMapping_10SecondsNinja.key_left)
        time.sleep(1)
        push_integer(IntMapping_10SecondsNinja.key_left+1000)
```



--------------------
----------------------

Trouvez ici une checklist de mots à apprendre en jouant à *10 Seconds Ninja* via du Python.  
Nous regarderons demain comment les transformer en C#.  

Hormis le fait que, pour débuter, il est plus simple d'apprendre le concept en Scratch et Python,  

il y a de très nombreuses possibilités offertes en Python, qui sont codables en 10-40 minutes contre 3-8 heures en C#, en raison de sa facilité d'utilisation et de sa grande communauté sur PyPI.  

Exemple : envoyer un mail avec [Mailchimp](https://mailchimp.com/) :  
🔗 [GitHub code](https://github.com/mailchimp/mailchimp-marketing-python)

Cela se fait en 30 lignes de code en Python.  

Essayer de jour à 10 Second Ninja avec du python et déposer votre code ici.
https://github.com/EloiStree/2025_02_03_MonsLevelUpInGroup/tree/main/PythonDrop

**Checklist :**  
- [ ] print("Hello World")
- [ ] variable
- [ ] variable type
- [ ] int, string float 
- [ ] print("Bonjour", name)
- [ ] # vs // one line comment
- [ ] """ vs /* */ multiline comment
- [ ] while True:
- [ ] True False
- [ ] def function()
- [ ] def function(with_params)
- [ ] PascaleCase vs camelCase vs snake_case
- [ ] import time
- [ ] time.sleep()
- [ ] import socker
- [ ] import iid42
- [ ] from iid42 import SendUdpIID
- [ ] pypi
- [ ] pip install iid42
- [ ] pip install wowint
- [ ] if condion:
- [ ] elif condition:
- [ ] else:
- [ ] for i in range(10):

Si vous vous sentez d'attaque:
- [ ] class Ninja
- [ ] __init__
- [ ] self
- [ ] constructor
- [ ] static variable
- [ ] static method
- [ ] object vs class 
- [ ] member variable
- [ ] member method


Si vous voulez vous amuser:
- Faire tourner le code sur un Raspberry Pi via SSH
- Faire tourner le code sur un Raspberry Pi Pico


Où en est on ?
https://docs.google.com/spreadsheets/d/15BQ1OqLn9omeHH6yPuqSO0Ip6XeQ0CktMDebbJCkarU/edit?usp=sharing



---------------------
------------------------

Pour le fun, d'en pense 🤖🐟:

En python:

``` python

# Print "Hello World"
print("Hello World")

# Variable declaration and types
integer_variable = 10  # Equivalent to 'int integerVariable;'
string_variable = "Hello"  # Equivalent to 'string stringVariable;'
float_variable = 3.14  # Equivalent to 'float floatVariable;'

# Print with variable (equivalent to 'Console.WriteLine($"Bonjour {name}");')
name = "John"
print("Bonjour", name)

# Single-line comment (equivalent to '//')
# This is a single-line comment in Python

# Multi-line comment (equivalent to '/* ... */')
"""
This is a multi-line comment in Python
"""

# Infinite loop (equivalent to 'while (true)')
while True:
    # Boolean values (equivalent to 'bool isTrue = true;')
    is_true = True
    is_false = False

    # Break the loop to avoid infinite execution
    break

# Function without parameters (equivalent to 'void Function()')
def function():
    print("Function without parameters")

# Function with parameters (equivalent to 'void FunctionWithParams(string param)')
def function_with_params(param):
    print(f"Function with parameter: {param}")

# Naming conventions
# PascalCase for class names (e.g., 'Ninja')
# snake_case for variables and function names (e.g., 'integer_variable', 'function_with_params')

# Sleep (equivalent to 'Thread.Sleep(1000);')
import time
time.sleep(1)  # Sleep for 1 second

# Conditional statements (equivalent to 'if', 'else if', 'else')
condition = 10
if condition > 10:
    print("Condition is greater than 10")
elif condition == 10:
    print("Condition is equal to 10")
else:
    print("Condition is less than 10")

# For loop (equivalent to 'for (int i = 0; i < 10; i++)')
for i in range(10):
    print(f"Iteration: {i}")

# Class definition (equivalent to 'class Ninja')
class Ninja:
    # Static variable (equivalent to 'public static int Count = 0;')
    count = 0

    # Constructor (equivalent to 'public Ninja(string name)')
    def __init__(self, name):
        # Member variable (equivalent to 'private string _name;')
        self.name = name
        Ninja.count += 1  # Increment static variable

    # Static method (equivalent to 'public static void DisplayCount()')
    @staticmethod
    def display_count():
        print(f"Ninja count: {Ninja.count}")

    # Member method (equivalent to 'public void DisplayName()')
    def display_name(self):
        print(f"Ninja name: {self.name}")

# Create an object of the Ninja class (equivalent to 'Ninja ninja = new Ninja("Shadow");')
ninja = Ninja("Shadow")
ninja.display_name()

# Access static variable and method (equivalent to 'Ninja.Count = 1;' and 'Ninja.DisplayCount();')
Ninja.count = 1
Ninja.display_count()
```

En C#:
``` cs
using System;
using System.Threading; // Equivalent to 'import time' and 'time.sleep()'
// using System.Net.Sockets; // Equivalent to 'import socket' (if needed)
// using iid42; // Equivalent to 'import iid42' (if needed)

namespace HelloWorld
{
    class Program
    {
        // Variable declaration and types
        int integerVariable;
        string stringVariable;
        float floatVariable;

        // Main method (entry point of the program)
        static void Main(string[] args)
        {
            // Print "Hello World"
            Console.WriteLine("Hello World");

            // Print with variable (equivalent to 'print("Bonjour", name)')
            string name = "John";
            Console.WriteLine($"Bonjour {name}");

            // Single-line comment (equivalent to '#')
            // This is a single-line comment in C#

            // Multi-line comment (equivalent to '""" ... """' or '/* ... */')
            /*
            This is a multi-line comment in C#
            */

            // Infinite loop (equivalent to 'while True:')
            while (true)
            {
                // Boolean values (equivalent to 'True' and 'False')
                bool isTrue = true;
                bool isFalse = false;

                // Break the loop to avoid infinite execution
                break;
            }

            // Function without parameters (equivalent to 'def function():')
            void Function()
            {
                Console.WriteLine("Function without parameters");
            }

            // Function with parameters (equivalent to 'def function(with_params):')
            void FunctionWithParams(string param)
            {
                Console.WriteLine($"Function with parameter: {param}");
            }

            // Naming conventions
            // PascalCase for class and method names (e.g., 'Ninja', 'FunctionWithParams')
            // camelCase for local variables and parameters (e.g., 'integerVariable', 'stringVariable')
            // snake_case is not commonly used in C#

            // Sleep (equivalent to 'time.sleep()')
            Thread.Sleep(1000); // Sleep for 1 second

            // Conditional statements (equivalent to 'if', 'elif', 'else')
            int condition = 10;
            if (condition > 10)
            {
                Console.WriteLine("Condition is greater than 10");
            }
            else if (condition == 10)
            {
                Console.WriteLine("Condition is equal to 10");
            }
            else
            {
                Console.WriteLine("Condition is less than 10");
            }

            // For loop (equivalent to 'for i in range(10):')
            for (int i = 0; i < 10; i++)
            {
                Console.WriteLine($"Iteration: {i}");
            }

            // Class definition (equivalent to 'class Ninja:')
            class Ninja
            {
                // Member variable (equivalent to 'member variable')
                private string _name;

                // Constructor (equivalent to '__init__' and 'self')
                public Ninja(string name)
                {
                    this._name = name;
                }

                // Static variable (equivalent to 'static variable')
                public static int Count = 0;

                // Static method (equivalent to 'static method')
                public static void DisplayCount()
                {
                    Console.WriteLine($"Ninja count: {Count}");
                }

                // Member method (equivalent to 'member method')
                public void DisplayName()
                {
                    Console.WriteLine($"Ninja name: {this._name}");
                }
            }

            // Create an object of the Ninja class
            Ninja ninja = new Ninja("Shadow");
            ninja.DisplayName();

            // Access static variable and method
            Ninja.Count = 1;
            Ninja.DisplayCount();
        }
    }
}
```









