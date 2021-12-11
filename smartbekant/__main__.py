import keybow

from SmartBekant import SmartBekant
from smartbekant.keyboard.KeybowController import KeybowController

keybow_controller = KeybowController()
smart_bekant = SmartBekant()


@keybow.on()
def handle_key(index, state):
    keybow_controller.handle_key(index, state)


smart_bekant.start()
