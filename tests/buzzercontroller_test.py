import time
from unittest.mock import Mock


def func(x):
    return x + 1


def test_long_beep():
    mock = Mock()
    buzzer_controller = buzzer(mock)
    buzzer_controller.long_beep()
    time.sleep(0.3)
    mock.on.assert_called_once()
    mock.off.assert_called_once()
