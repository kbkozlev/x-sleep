# created by kbkozlev 23.11.2021
import random
import time
from pynput.keyboard import Key, Controller as KeyController
from pynput.mouse import Controller as MouseController

mouse = MouseController()
key = KeyController()


def toggle(button, state, name, wait=None):

    key.press(button)
    key.release(button)

    if state == 1:
        print('{0} ON'.format(name))

    elif state == 0:
        print('{0} OFF, button was pressed for {1}s.'.format(name, wait))


mouse.position = (0, 0)

print('The pointer starting position is {0}'.format(mouse.position))

while True:
    a = random.randint(1, 10)
    b = 1

    while b <= a:
        time.sleep(random.randint(1, 5))
        mouse.move(random.randint(-500, 500), random.randint(-500, 500))
        print('The pointer was moved to {0}'.format(mouse.position))
        b += 1

    wait = random.randint(1, 5)
    toggle(Key.caps_lock, 1, 'Caps Lock')
    time.sleep(wait)
    toggle(Key.caps_lock, 0, 'Caps Lock', wait)
