

``` python
import struct
import time
import socket

key_tab_press = 1009
key_power1_press = 1049
player_index= 2


def send_index_integer(index: int, actionKey: int):
    # Pack the integers into bytes
    byte = struct.pack("<ii", index, actionKey)
    
    # Define the server address and port
    address = "127.0.0.1"  # or use "apint.ddns.net"
    port = 7073
    
    s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM) 
    try:
        # Send the packed data
        s.sendto(byte, (address, port))
        print(f"Sent data to {address}:{port}")
    
    except Exception as e:
        print(f"Error sending data: {e}")
    
    finally:
        s.close()  # Make sure to close the socket when done

def press_and_release(actionKey:int, seconds:float):
    send_index_integer(player_index,actionKey )
    time.sleep(seconds)
    send_index_integer(player_index,actionKey+1000 )



while True:
    press_and_release(key_tab_press, 0.1)
    for i in range(4):
        press_and_release(key_power1_press,0.1)
        time.sleep(1.9)
```


``` cs
using System;
using System.Net.Sockets;
using System.Threading;  // Added for Thread.Sleep

public class HelloWorld
{

    // Méthode pour envoyer un index et une clé d'action
    public static void SendIndexInteger(int index, int actionKey)
    {
        // Pack les entiers dans un tableau de bytes (Little Endian)
        byte[] byteArray = new byte[8];
        byteArray[0] = (byte)(index & 0xFF);
        byteArray[1] = (byte)((index >> 8) & 0xFF);
        byteArray[2] = (byte)((index >> 16) & 0xFF);
        byteArray[3] = (byte)((index >> 24) & 0xFF);
        byteArray[4] = (byte)(actionKey & 0xFF);
        byteArray[5] = (byte)((actionKey >> 8) & 0xFF);
        byteArray[6] = (byte)((actionKey >> 16) & 0xFF);
        byteArray[7] = (byte)((actionKey >> 24) & 0xFF);

        // Définir l'adresse et le port du serveur
        string address = "127.0.0.1";  // Ou utiliser "apint.ddns.net"
        int port = 7073;

        // Créer le socket UDP
        using (UdpClient s = new UdpClient())
        {
            try
            {
                // Envoyer les données empaquetées
                s.Send(byteArray, byteArray.Length, address, port);
                Console.WriteLine($"Sent data to {address}:{port}");
            }
            catch (Exception e)
            {
                Console.WriteLine($"Error sending data: {e.Message}");
            }
        }
    }

    // Méthode pour simuler l'appui et la relâche d'une touche avec un délai
    public static void PressAndRelease(int indexPlayer, int actionKey, float seconds)
    {
        SendIndexInteger(indexPlayer, actionKey);
        Thread.Sleep((int)(seconds * 1000));  // Convertir les secondes en millisecondes
        SendIndexInteger(indexPlayer, actionKey + 1000);
    }
    public static void Press(int indexPlayer, int actionKey)
    {
        SendIndexInteger(indexPlayer, actionKey);
     
    }
    public static void Release(int indexPlayer, int actionKey)
    {
        SendIndexInteger(indexPlayer, actionKey + 1000);
    }
    public static void Main(string[] args)
    {
        Console.WriteLine("Hello World");
        int keyTab = 1009;
        int keyPower = 1049;
        int keyJump = 1032;
        int keyLeft = 1037;
        int playerIndex = 0;
        string name = "Eloi";
        Console.WriteLine(name);
        while (true)
        {
            Console.WriteLine("Next ?");
            string command = Console.ReadLine();
            Console.WriteLine(command);
            string[] items = command.Split(" ");
            Console.WriteLine("Items Count: " + items.Length);

            foreach (string item in items)
            {
                Console.WriteLine("Item: " + item);
                if (int.TryParse(item, out int milliseconds))
                {
                    Thread.Sleep(milliseconds);  // Sleep for the specified milliseconds
                }
                else if (item == "L")
                {
                    Console.WriteLine("Start Turn Left");
                    Press(playerIndex, keyLeft);
                }
                else if (item == "l")
                {
                    Console.WriteLine("Stop Turn Left");
                    Release(playerIndex, keyLeft);
                }
                else 
                {
                    switch (item)
                    {
                        case "tab":
                        case "t":
                            PressAndRelease(playerIndex,keyTab, 0.1f);
                            break;
                        case "jump":
                        case "j":
                            PressAndRelease(playerIndex, keyJump, 0.1f);
                            break;
                        case "attack":
                        case "a":
                            PressAndRelease(playerIndex, keyPower, 0.1f);
                            break;
                    }
                }
            }
        }
    }
}

```

