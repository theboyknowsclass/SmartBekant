from keyboard.KeybowProxy import KeybowProxy
from SmartBekant import SmartBekant
import keybow

keybow_proxy = KeybowProxy()
keybow.setup(keybow.MINI)
r, g, b = keybow_proxy.background
keybow.set_led(0, r, g, b)
keybow.set_led(1, r, g, b)
keybow.set_led(2, r, g, b)
keybow.show()

smart_bekant = SmartBekant()

@keybow.on(index=0)
def handle_key(index, state):
    keybow_proxy.handle_key(index, state)
    if state:
        r, g, b = keybow_proxy.up_colour
        keybow.set_led(index, r, g, b)
        keybow.show()
    else:
        r, g, b = keybow_proxy.background
        keybow.set_led(index, r, g, b)
        keybow.show()

@keybow.on(index=1)
def handle_key(index, state):
    global keybow_proxy
    keybow_proxy.handle_key(index, state)
    if state:
        r, g, b = keybow_proxy.down_colour
        keybow.set_led(index, r, g, b)
        keybow.show()
    else:
        r, g, b = keybow_proxy.background
        keybow.set_led(index, r, g, b)
        keybow.show()

@keybow.on(index=2)
def handle_key(index, state):
    global keybow_proxy
    keybow_proxy.handle_key(index, state)
    if state:
        r, g, b = keybow_proxy.memory_colour
        keybow.set_led(index, r, g, b)
        keybow.show()
    else:
        r, g, b = keybow_proxy.background
        keybow.set_led(index, r, g, b)
        keybow.show()

smart_bekant.start()