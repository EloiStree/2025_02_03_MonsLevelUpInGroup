import time

# pip install iid42    in console
import iid42
from iid42 import SendUdpIID

## import wowint
from wowint import *

# print("Hello World")
# time.sleep(2)
# print("Oh yeah")

class NinjaToolBox:
    
    
    key_c= 1067
    key_escape = 1027
    key_arrow_up= 1038
    key_arrow_left= 1037
    key_arrow_right= 1039
    key_x_sword=  1088
    key_z_shurikens = 1090
    key_r_restart = 1082
    
    key_continue = key_c
    key_jump = key_arrow_up
    key_go_left = key_arrow_left
    key_go_right = key_arrow_right
    key_sword=  key_x_sword
    key_shuriken = key_z_shurikens
    key_restart = key_r_restart
    
    
    
    def bonjour():
        print("Bonjour")
    def help():
        print(f"""
              jump={NinjaToolBox.key_jump}
              left={NinjaToolBox.key_go_left}
              right={NinjaToolBox.key_go_right}
              sword={NinjaToolBox.key_sword}
              shuriken={NinjaToolBox.key_shuriken}
              restart={NinjaToolBox.key_restart}
              escape={NinjaToolBox.key_escape}
              next_level={NinjaToolBox.key_continue}
              """)
         
jump =1038
restart = IntMapping_10SecondsNinja.key_restart

ipv4_target="81.240.94.97"
ipv4_target="169.254.160.23"

player: SendUdpIID = SendUdpIID(ipv4_target, 7073, True, True)
player_index= 1
## wait to hide window.
# time.sleep(3)



player.push_index_integer(player_index, NinjaToolBox.restart)
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

def click_escape():
    press_for_delay(NinjaToolBox.escape,0.1,0.1)
    
def click_next_level():
    press_for_delay(NinjaToolBox.next_level,0.1,0.1)
    


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
        
NinjaToolBox.bonjour()
NinjaToolBox.help()



NinjaToolBox.help()
NinjaToolBox.click_espace()
while True:
    user_text = input("Next ?")
    print(f"Enter:{user_text}")
    if user_text == "level1":
        process_level_one()
    
    
