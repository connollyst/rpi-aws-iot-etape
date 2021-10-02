# Simple demo of reading each analog input from the ADS1x15 and printing it to
# the screen.
# Author: Tony DiCola
# License: Public Domain

# Choose a gain of 1 for reading voltages from 0 to 4.09V.
# Or pick a different gain to change the range of voltages that are read:
#  - 2/3 = +/-6.144V
#  -   1 = +/-4.096V
#  -   2 = +/-2.048V
#  -   4 = +/-1.024V
#  -   8 = +/-0.512V
#  -  16 = +/-0.256V
# See table 3 in the ADS1015/ADS1115 datasheet for more info on gain.
from app.App import App

# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    App().start()

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
