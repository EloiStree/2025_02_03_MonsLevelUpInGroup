# https://youtu.be/lQHoowgRapY
# download: https://github.com/EloiStree/2025_01_28_BubbleTankAfterJam/releases/tag/2025.1.310733
import time

# pip install iid42
import iid42

from iid42 import SendUdpIID
import threading
import socket


bool_use_print = False

print("Hello World")

game_port_sent:int = 2504
game_port_listen_info:int = 8001

##CMD:  ipconfig
ipv4_address:str = "192.168.1.118"
ipv4_address:str = "127.0.0.1"


## MANETTE: 1899887766 18 99 88 77 66  rx ry lx ly
## KEYBOARD: 

key_left:int = 1037
key_up:int = 1038
key_right:int = 1039
key_down:int = 1040
key_space:int = 1019
key_fire:int = 1032




player : SendUdpIID = SendUdpIID(ipv4_address, game_port_sent, True, True)

player_index= 456654




class PlayerInfoOnServer:
    def __init__(self,player_index:int, player_team_id:int
                 , position_x:float, position_y:float, position_z:float
                 , rotation_x:float, rotation_y:float, rotation_z:float
                 , size:float
                 , flat_x2z_angle:float):
        self.player_index = player_index
        self.player_team_id = player_team_id
        self.position_x = position_x
        self.position_y = position_y
        self.position_z = position_z
        self.rotation_x = rotation_x
        self.rotation_y = rotation_y
        self.rotation_z = rotation_z
        self.size = size
        self.flat_x2z_angle = flat_x2z_angle
        self.timestamp = time.time()
        
        
dico_player_info = {}
dico_player_info[1] = PlayerInfoOnServer(player_index, 0, 0, 0, 0, 0, 0, 0, 0, 0)   
        


def press_key_start(key_to_press:int):
    player.push_index_integer_date_ntp_in_milliseconds(player_index, key_to_press, 0)

def press_key_end(key_to_press:int):
    player.push_index_integer_date_ntp_in_milliseconds(player_index, key_to_press+1000, 0)


def rotate_left_start():
    press_key_start(key_left)
    
def rotate_left_end():
    press_key_end(key_left)
    
def rotate_right_start():
    press_key_start(key_right)

def rotate_right_end():
    press_key_end(key_right)

def move_up_start():
    press_key_start(key_up)

def move_up_end():
    press_key_end(key_up)
    
def move_down_start():
    press_key_start(key_down)

def move_down_end():
    press_key_end(key_down)
    
def fire_start():
    press_key_start(key_fire)

def fire_end():
    press_key_end(key_fire)
    
def fire():
    fire_start()
    fire_end()

def fire_with_delay(delay_in_seconds:float):
    fire_start()
    time.sleep(delay_in_seconds)
    fire_end()
    


def listen_to_port(port):
    global dico_player_info
    
    
    sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    sock.bind(("0.0.0.0", port))
    while True:
        data = sock.recvfrom(65507)[0]
        text = data.decode("utf-8")
        #print(f"Received message: {text} from {addr}")
        lines = text.split("\n")
        for line in lines:
            if line.startswith("ID"):
                continue
            # if line.startswith(str(player_index)):
            #     print("ME:",line)
            
            items = line.split(':')
            if len(items)==10 and items[0].isdigit():
                player_index = int(items[0])
                player_team_id = int(items[1])
                position_x = int(items[2])/1000
                position_y = int(items[3])/1000
                position_z = int(items[4])/1000
                rotation_x = int(items[5])/1000
                rotation_y = int(items[6])/1000
                rotation_z = int(items[7])/1000
                size = int(items[8])/1000
                flat_x2z_angle = int(items[9])/1000
                
                
                player_referce = None
                player_index_str_id = str(player_index)
                if not ( player_index_str_id in dico_player_info):
                    dico_player_info[player_index_str_id] = PlayerInfoOnServer(player_index, player_team_id
                     , position_x, position_y, position_z
                     , rotation_x, rotation_y, rotation_z
                     , size
                     , flat_x2z_angle)
                    if bool_use_print:
                        print ("New player:",player_index_str_id)
                else: 
                    player_referce = dico_player_info[player_index_str_id]
                    player_referce.player_team_id = player_team_id
                    player_referce.position_x = position_x
                    player_referce.position_y = position_y
                    player_referce.position_z = position_z
                    player_referce.rotation_x = rotation_x
                    player_referce.rotation_y = rotation_y
                    player_referce.rotation_z = rotation_z
                    player_referce.size = size
                    player_referce.flat_x2z_angle = flat_x2z_angle
                    player_referce.timestamp = time.time()
        
        
        # Remove death player
        keys_to_remove = []
        for key, value in dico_player_info.items():
            if value is None or time.time() - value.timestamp > 5:
                print("Player is dead:", key)
                keys_to_remove.append(key)
                
        for key in keys_to_remove:
            del dico_player_info[key]
        if bool_use_print:
            print("Player Count Dico: ", len(dico_player_info))
            print(f"Player Count in server : {len(lines)-1}")
        



print ("Start thread udp listener ")
listener_thread = threading.Thread(target=listen_to_port, args=(game_port_listen_info,))
listener_thread.daemon = True
listener_thread.start()


class MyVector3:
    def __init__(self, x:float, y:float, z:float):
        self.x = x
        self.y = y
        self.z = z
    def __str__(self):
        return f"x:{self.x} y:{self.y} z:{self.z}"
    
    def __add__(self, other):
        return MyVector3(self.x+other.x, self.y+other.y, self.z+other.z)
    
    def __sub__(self, other):
        return MyVector3(self)

def handle_ai_logic (): 
    print ("Start AI logic")
    

    
    while True:
        print("AI logic")
        time.sleep(1)
            
        me : PlayerInfoOnServer = dico_player_info[str(player_index)]
        
        where_am_i = MyVector3(me.position_x, me.position_y, me.position_z)
        where_to_go = MyVector3(0, 0, 0)
        my_direction = me.flat_x2z_angle
        
        print ("Current Direction:", my_direction)
        print("Move up")
        fire()
        move_up_start()
        time.sleep(3)
        move_up_end()
        
        print("Move down")
        fire()
        move_down_start()
        time.sleep(3)
        move_down_end()
        
        print("Rotate left")
        fire()
        rotate_left_start()
        time.sleep(3)
        rotate_left_end()
        
        print("Rotate right")
        fire()
        rotate_right_start()
        time.sleep(3)
        rotate_right_end()
        
        



print ("Start our code logic")
while True:
    
    bool_use_mini_old_type_ai=True
    if bool_use_mini_old_type_ai:
        handle_ai_logic()
        
    
    bool_use_console =False
    if bool_use_console:
        input_player = input("Enter a key: ")
        print("You entered: ", input_player)
        if input_player=="Test Input":
                print("Move up")
                fire()
                move_up_start()
                time.sleep(3)
                move_up_end()
                
                print("Move down")
                fire()
                move_down_start()
                time.sleep(3)
                move_down_end()
                
                print("Rotate left")
                fire()
                rotate_left_start()
                time.sleep(3)
                rotate_left_end()
                
                print("Rotate right")
                fire()
                rotate_right_start()
                time.sleep(3)
                rotate_right_end()
                
                
                print("Fire")
                fire()
                time.sleep(3)
                
                
                print("Fire with delay")
                fire_with_delay(1)
                
                print("End Reach")

                player.push_index_integer_date_ntp_in_milliseconds(player_index, key_up, 0)
                time.sleep(0.1)
                player.push_index_integer_date_ntp_in_milliseconds(player_index, key_up+1000, 0)
                time.sleep(0.5)
                
        elif input_player=="q":
            rotate_left_start()
        elif input_player=="d":
            rotate_right_start()
        elif input_player=="z":
            move_up_start()
        elif input_player=="s":
            move_down_start()
        elif input_player=="x":
            player.push_index_integer_date_ntp_in_milliseconds(player_index, 1800000000, 0)
        elif input_player==" " or input_player=="f":
            fire()
        elif input_player=="F":
            for i in range(1000):
                fire_with_delay(0.01)
 












