#import sys
from ctypes import sizeof
import colorama
import random
text = "Buddha"
try:

    with open("/home/ashwin/gits/banner/buddha.txt","r") as ashwin:
        aline = ashwin.read().splitlines()
        started=0
        num=random.randrange(1,len(aline))
    #  print(len(aline))
    #  print(num)
        for i in range(num,num+100):
            if "buddha" in aline[i]:
                if started == 1:
                    break
                started=1
                continue
            elif started:
                text = text + "\n" + aline[i]
        ashwin.close()

except:
    text = text+"\n"+"""

_      `-._     `-.     `.   \      :      /   .'     .-'     _.-'      _
 `--._     `-._    `-.    `.  `.    :    .'  .'    .-'    _.-'     _.--'
      `--._    `-._   `-.   `.  \   :   /  .'   .-'   _.-'    _.--'
`--.__     `--._   `-._  `-.  `. `. : .' .'  .-'  _.-'   _.--'     __.--'
__    `--.__    `--._  `-._ `-. `. \:/ .' .-' _.-'  _.--'    __.--'    __
  `--..__   `--.__   `--._ `-._`-.`_=_'.-'_.-' _.--'   __.--'   __..--'
--..__   `--..__  `--.__  `--._`-q(-_-)p-'_.--'  __.--'  __..--'   __..--
      ``--..__  `--..__ `--.__ `-'_) (_`-' __.--' __..--'  __..--''
...___        ``--..__ `--..__`--/__/  \--'__..--' __..--''        ___...
      ```---...___    ``--..__`_(<_   _/)_'__..--''    ___...---'''
```-----....._____```---...___(__\_\_|_/__)___...---'''_____.....-----'''
 ___   __  ________   _______   _       _   _______    ___   __   _______
|| \\  ||     ||     ||_____))  \\     //  ||_____||  || \\  ||  ||_____||
||  \\_||  ___||___  ||     \\   \\___//   ||     ||  ||  \\_||  ||     ||

    """



bad_colors = ['BLACK', 'WHITE', 'LIGHTBLACK_EX', 'RESET']
codes = vars(colorama.Fore)
colors = [codes[color] for color in codes if color not in bad_colors]

colored_lines = [random.choice(colors) + line for line in text.split('\n')]
print('\n'.join(colored_lines))

#colored_chars = [random.choice(colors) + char for char in text]
#print(''.join(colored_chars))