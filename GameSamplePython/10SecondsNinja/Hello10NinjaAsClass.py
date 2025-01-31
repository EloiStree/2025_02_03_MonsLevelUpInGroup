import time


## https://github.com/EloiStree/2025_02_03_MonsLevelUpInGroup/tree/main/GameSamplePython/10SecondsNinja

# pip install iid42    in console
import iid42
from iid42 import SendUdpIID

## import wowint
from wowint import *

# print("Hello World")
# time.sleep(2)
# print("Oh yeah")

jump =1038
restart = IntMapping_10SecondsNinja.key_restart

ipv4_target="81.240.94.97"
ipv4_target="127.0.0.1"

player: SendUdpIID = SendUdpIID(ipv4_target, 7073, True, True)
player_index= 1
## wait to hide window.
# time.sleep(3)



player.push_index_integer(player_index, restart)
time.sleep(0.1)
player.push_index_integer(player_index,restart+1000)

# while True:
#     player.push_integer(jump)
#     time.sleep(0.01)
#     player.push_integer(jump+1000)
#     time.sleep(2)


def press_for_delay(key_to_press:int,
                    seconds_between_press:float,
                    seconds_after_press:float ):
    player.push_index_integer(player_index,key_to_press)
    time.sleep(seconds_between_press)
    player.push_index_integer(player_index,key_to_press+1000)
    time.sleep(seconds_after_press)

def press_key(key_to_press:int):
    player.push_index_integer(player_index,key_to_press)

def release_key(key_to_press:int):
    player.push_index_integer(player_index,key_to_press+1000)



def process_level_one():
    
    # player.push_integer(restart)
    # time.sleep(0.1)
    # player.push_integer(restart+1000)
    # time.sleep(0.2)
    # player.push_integer(jump)
    # time.sleep(0.01)
    # player.push_integer(jump+1000)
    # time.sleep(2)
    press_for_delay(restart,0.2,0.6)
    press_for_delay(IntMapping_10SecondsNinja.key_shuriken,0.03,0.03)
    press_for_delay(IntMapping_10SecondsNinja.key_right,0.35,0.1)

    press_key(IntMapping_10SecondsNinja.key_jump)
    press_key(IntMapping_10SecondsNinja.key_left)
    time.sleep(0.5)
    release_key(IntMapping_10SecondsNinja.key_jump)
    release_key(IntMapping_10SecondsNinja.key_left)
    time.sleep(0.1)
    press_key(IntMapping_10SecondsNinja.key_jump)
    press_key(IntMapping_10SecondsNinja.key_left)
    press_key(IntMapping_10SecondsNinja.key_sword)
    time.sleep(0.5)
    release_key(IntMapping_10SecondsNinja.key_sword)
    release_key(IntMapping_10SecondsNinja.key_jump)
    release_key(IntMapping_10SecondsNinja.key_left)
    
    time.sleep(0.2)
    press_key(IntMapping_10SecondsNinja.key_right)
    press_for_delay(IntMapping_10SecondsNinja.key_jump,0.35,0.1)
    press_for_delay(IntMapping_10SecondsNinja.key_jump,0.35,0.1)
    release_key(IntMapping_10SecondsNinja.key_right)
    press_for_delay(IntMapping_10SecondsNinja.key_shuriken,0.1,0.1)
    time.sleep(3)
    press_for_delay(IntMapping_10SecondsNinja.key_continue,0.1,0.1)

    time.sleep(4)
    
    



#process_level_one()


class Ninja:
    ip_home ="127.0.0.1"
    ip_server= "apint.ddns.net"
    def ninja():
        print("NINJA !!!")

    def __init__(self, ipv4, port, player_index, name_ninja):
        self.ipv4 = ipv4
        self.port = port
        self.player_index = player_index
        self.name_ninja = name_ninja
        self.connection = SendUdpIID(ipv4, port,True, True)
    
    def start_go_right(self):
        print(f"{self.name_ninja}: Start Moving right ->")
        self.connection.push_index_integer(self.player_index, IntMapping_10SecondsNinja.key_right)
    
    
    def stop_go_right(self):
        print(f"{self.name_ninja}: Stop Moving right ->|")
        self.connection.push_index_integer(self.player_index, IntMapping_10SecondsNinja.key_right+1000)

    def press_key(self, key_press : int):
        self.connection.push_index_integer(self.player_index, key_press)

    def release_key(self, key_press: int):
        self.connection.push_index_integer(self.player_index, key_press+1000)

        
    
player_1 : Ninja = Ninja(Ninja.ip_home, 7073, 1, "Ninja Marcel")
player_2 : Ninja = Ninja(Ninja.ip_server, 7073, 1, "Ninja Didier")

team = []
team.append(player_1)
team.append(player_2)

print("\n\n--------------\n\n")

for ninja in team:
    Ninja.ninja()
    ninja.start_go_right()
    time.sleep(1)
    ninja.stop_go_right()

print("\n\n--------------\n\n")

for ninja in team:
    Ninja.ninja()
for ninja in team:
    ninja.start_go_right()

time.sleep(1)

for ninja in team:
    ninja.stop_go_right()

print("\n\n--------------\n\n")

class TeamNinja:

    def __init__(self):
        self.ninja_in_team:Ninja=[]
        pass

    def add_ninja(self, ninja:Ninja):
        print("NINJA add to the village (HUouuu): ", ninja.name_ninja)
        self.ninja_in_team.append(ninja)

    def press_key(self, key_press: int ):
        for ninja_selected in self.ninja_in_team:
            ninja_selected.press_key(key_press)
    
    
    def release_key(self, key_press: int ):
        for ninja_selected in self.ninja_in_team:
            ninja_selected.release_key(key_press)

team_7 : TeamNinja = TeamNinja()
team_7.add_ninja(player_1)
team_7.add_ninja(player_2)


for i in range(2,30,4):
    print(str(i))

print(f">>>> TEAM NUMBER: {str(len(team_7.ninja_in_team))}")


say_hello_to_village="""
I am the coding ninja village.
Be careful of what you do here
Marcel is watching you

"""

print (say_hello_to_village)

print ("CUT: ",say_hello_to_village[20:25])

index= 0
while True:
    action = index % 5
    index+=1

    """
    THe following is a demo code to a module to trigger random action
    It is not the best but it is to show.

    """
    ## I am a comment on a line



    key_to_presss = None
    if action ==0:
        key_to_presss = IntMapping_10SecondsNinja.key_sword
    elif action==1:
        key_to_presss = IntMapping_10SecondsNinja.key_shuriken
    elif action==2:
        key_to_presss = IntMapping_10SecondsNinja.key_jump
    else :
        key_to_presss = IntMapping_10SecondsNinja.key_restart

    team_7.press_key(key_to_presss)
    time.sleep(1)
    team_7.release_key(key_to_presss)
    time.sleep(1)
