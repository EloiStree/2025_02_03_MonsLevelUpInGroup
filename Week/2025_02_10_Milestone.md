> **Jeu : 10 Second Ninja**  

Git: https://github.com/EloiStree/2025_02_08_Ex_10SecondNinjaPythonAndCSharp.git  

**Jour 1 : C'est quoi du code ?**       
- Jeu : 10 Second Ninja     
- Matin : Apprendre ce qu'est une variable et une méthode, et ce qu'il y a autour en Python  
- Après-midi : Même exercice en C# (int, float, Thread.Sleep, méthode statique, using...)  


> **Jeu : World of Warcraft**   

Git: https://github.com/EloiStree/2025_02_05_WarcraftClientQA  

**Jour 2 : C'est quoi une console ?**    
- Matin : Apprendre à utiliser Console.WriteLine et ReadLine    
- Après-midi : Apprendre à utiliser if, switch avec string.Split()  

**Jour 3 : Nettoyons un peu Main()**  
- Matin : Créer une boîte à outils avec une classe statique  
- Après-midi : Du switch au dictionnaire  

**Jour 4 :  Des classes et du mapping**  
- Matin: Créé des classes 
  - créé des classes contenants des macro de déplacement.
  - Estimation de déplacement.
- Après-midi: Pratiquer les classes
  - Le premier à Booty Bay

**Jour 5 : Allons tuer Van Cleef**  
- Matin : Une dernière révision des bases C# non vues  
- Après-midi : Faire les Mortemines à 4 (x2)  


**Mon objectif est d'avoir avec eux au minimum :**  
- Variables, classes statiques et méthodes statiques, surcharge et polymorphisme  
- Leur faire faire des macros de ce type : "LEFT 1000 left POWER1 80 power1 Q Z 500 qz"  
- Utiliser un dictionnaire et, au minimum, utiliser des listes  
- Essayer de faire pratiquer *class vs object* aux débutants  
- Donner de la matière selon le cas pour les plus experts  

Je n’aborde pas les classes abstraites, sauf quand un élève en fait la demande ou est prêt à comprendre ce que c’est.  
La classe est composée de débutants pour qui c’est la première ligne de code. :wink:

Sur le plan technique, je les fais jouer à des jeux via des messages UDP envoyés à l’ordinateur du formateur.  
Ils disposent de code facade  pour éviter d’avoir à apprendre ce qu’est un message UDP.

Les messages sont composés de 8 octets : un **int** pour l'index et un **int** pour la valeur.

```python
index = 5  # Fenêtre de jeu ciblée
value = 1027  # Appui sur la touche "espace"
value = 2027  # Relâchement de la touche "espace"
packed_data = struct.pack('>ii', index, value)  # Big-endian
```

Le mapping des touches est disponible ici :  
https://github.com/EloiStree/2024_08_29_ScratchToWarcraft
