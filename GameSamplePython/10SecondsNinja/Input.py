import time
def press_key(command):
    print(f"Pressing key {command}")
def release_key(command):
    print(f"Release key {command}")
    
command = "left 2000 LEFT  l 2000 L jump 80 shuriken 80 sword"
def execute_macro(command):
    items = command.split(' ')
    for item in items:
        if item.isdigit():
            milliseconds = int(item)
            time.sleep(milliseconds/1000)
        elif (item == 'left')or (item =='l'):
            press_key(1)
        elif item == 'LEFT'or item =='L':
            release_key(1)
        elif item == 'jump':
            press_key(2)
        elif item == 'shuriken':
            press_key(3)
        elif item == 'sword':
            press_key(4)
            
execute_macro(command)