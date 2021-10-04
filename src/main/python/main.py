# import sys
# import fake_rpi

from app.App import App

# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    # TODO move to special main
    # sys.modules['RPi'] = fake_rpi.RPi  # Fake RPi
    # sys.modules['RPi.GPIO'] = fake_rpi.RPi.GPIO  # Fake GPIO
    # sys.modules['smbus'] = fake_rpi.smbus  # Fake smbus (I2C)
    App().start()

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
