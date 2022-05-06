from pynput.keyboard import Key, Controller
import threading
import time
import random

def simulate_key_event(keyboard):
    keyboard.press(Key.space)

def get_rand_key_code():

    keylist = [
        [Key.page_up], 
        [Key.page_down], 
        [Key.up], 
        [Key.down], 
        [Key.right],
        [Key.up], 
        [Key.down], 
        [Key.right],
        [Key.up], 
        [Key.down], 
        [Key.down],
        [Key.down],
        [Key.down],
        [Key.right],
        [Key.ctrl, Key.tab],
        [Key.ctrl, Key.tab],
        [Key.ctrl, Key.tab],
        [Key.ctrl, Key.tab]
    ]   
    code = random.randrange(len(keylist))
    return keylist[code]
    # elif code_type == 2:
    #     return [Key.Alt]
    # elif code_type == 3:
    #     return [Key.Alt, Key.Ctrl]


def simulate_temp_key_event(keyboard):
    cnt = random.randrange(3) + 2
    for i in range(cnt):
        keys = get_rand_key_code()
        if(type(keys) == type([])):
            for keycode in keys:
                keyboard.press(keycode)
            for keycode in keys:
                keyboard.release(keycode)
        else:
            keyboard.type(keys)

def simulate_mouse_event():
    pass


def main_thread():
    global command
    key_controller = Controller()

    while True:
        timeToSleep = random.randrange(2) + 1
        time.sleep(timeToSleep)
        if command == '1':
            simulate_key_event(key_controller)
        elif command == '2':
            simulate_mouse_event()
        elif command == '3':    
            simulate_temp_key_event(key_controller)
        elif command == 'q':
            break
    
    print("stop thread")
    return


if __name__ == '__main__':
    command = None
    t = threading.Thread(target=main_thread)
    t.start()
    print("Input q to quit")
    while True:
        print("Input Command: ")
        command = input()
        if command == 'q':
            break
    t.join()
    print("Host thread exited")
