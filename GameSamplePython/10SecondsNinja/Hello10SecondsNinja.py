

import os
## Use by the developer when workin on iid42
## Comment it.
cmd = "pip install iid42 wowint  --force-reinstall" 
os.system(cmd)


# pip install iid42
# Manual: 
# https://github.com/EloiStree/2024_08_29_ScratchToWarcraft
import iid42
from iid42 import SendUdpIID
import socket
import time

import wowint
from wowint import WowIntegerKeyboard
from wowint import IntMapping_10SecondsNinja


print("Hey, I am a python script for 10SecondsNinja. I will send some key to the game.")
server_name ="apint-gaming.ddns.net"

print(iid42.IIDUtility.get_ipv4(server_name))


# Send IID to a UDP Gate Relay
# Replace 127.0.0.1 with the computer you want to target or the game server
# Example: 192.168.1.42  http://apint.ddns.net 
target = SendUdpIID(server_name,3615,True,True)
# Send the action 42 to the target with UDP to 127.0.0.1 computer on the applicaton behind 3615 port.
target.push_integer(42)
# Send the action 42 to the player 2 to the target with UDP to 127.0.0.1 computer on the applicaton behind 3615 port.
target.push_index_integer(2,42)

# Send the action 42 to all the player to the target with UDP to 127.0.0.1 computer on the applicaton behind 3615 port.
target.push_index_integer(0,42)


key_x_escape = IntMapping_10SecondsNinja.key_escape
key_x_validate= IntMapping_10SecondsNinja.key_continue
key_c_back= WowIntegerKeyboard.key_c

key_x_sword=  IntMapping_10SecondsNinja.key_sword
key_z_shurikens =  IntMapping_10SecondsNinja.key_shuriken
key_r_retry= IntMapping_10SecondsNinja.key_restart
key_up_arrow = IntMapping_10SecondsNinja.key_jump
key_left_arrow =IntMapping_10SecondsNinja.key_left
key_right_arrow =IntMapping_10SecondsNinja.key_right

def press_all( press_value):
    
    target.push_index_integer(0, press_value)

def release_all( press_value):
    target.push_index_integer(0, press_value + 1000)


def  press_release_all(press_value):
    press_all(press_value)
    time.sleep(0.2)
    release_all(press_value)
    
press_release_all(key_r_retry)


me_index =1

def press_me( press_value):
    target.push_index_integer(me_index, press_value)

def release_me( press_value):
    target.push_index_integer(me_index, press_value + 1000)
    
def  press_release_me(press_value):
    press_me(press_value)
    time.sleep(0.2)
    release_me(press_value)
    

bool_use_time = False
if bool_use_time:
    press_all(key_r_retry)
    time.sleep(1)
    while True:
        press_release_me(key_x_sword)
        time.sleep(0.5)
        press_release_me(key_z_shurikens)
        time.sleep(0.5)
        press_release_me(key_up_arrow)
        time.sleep(0.5)
        press_release_me(key_left_arrow)
        time.sleep(0.5)
        press_release_me(key_right_arrow)
        time.sleep(0.5)
        press_release_me(key_r_retry)
    

bool_use_time_thread = True
if bool_use_time_thread:
    press_all(key_r_retry)
    while True:
        time.sleep(5)
        
        target.push_index_integer_in_queue(0, key_r_retry,0)
        target.push_index_integer_in_queue(0, key_x_sword,500)
        target.push_index_integer_in_queue(0, key_z_shurikens,1000)
        target.push_index_integer_in_queue(0, key_up_arrow,1500)
        target.push_index_integer_in_queue(0, key_left_arrow,2000)
        target.push_index_integer_in_queue(0, key_right_arrow,2500)
        target.push_index_integer_in_queue(0, key_r_retry,3500)

        delay_ms_press=60
        target.push_index_integer_in_queue(0, key_r_retry+1000,0+delay_ms_press)
        target.push_index_integer_in_queue(0, key_x_sword+1000,500+delay_ms_press)
        target.push_index_integer_in_queue(0, key_z_shurikens+1000,1000+delay_ms_press)
        target.push_index_integer_in_queue(0, key_up_arrow+1000,1500+delay_ms_press)
        target.push_index_integer_in_queue(0, key_left_arrow+1000,2000+delay_ms_press)
        target.push_index_integer_in_queue(0, key_right_arrow+1000,2500+delay_ms_press)
        target.push_index_integer_in_queue(0, key_r_retry+1000,3500+delay_ms_press)

        







