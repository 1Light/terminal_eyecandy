#import sys
from ctypes import sizeof
import colorama
import random
text = """Ashwin"""

with open("/home/ashwin/gits/banner/ashwin.txt","r") as ashwin:
    aline = ashwin.read().splitlines()
    started=0
    num=random.randrange(1,len(aline))
  #  print(len(aline))
  #  print(num)
    for i in range(num,num+100):
        if "Font" in aline[i]:
            if started == 1:
                break
            started=1
            continue
        elif started:
            text = text + "\n" + aline[i]
    ashwin.close()


bad_colors = ['BLACK', 'WHITE', 'LIGHTBLACK_EX', 'RESET']
codes = vars(colorama.Fore)
colors = [codes[color] for color in codes if color not in bad_colors]

colored_lines = [random.choice(colors) + line for line in text.split('\n')]
print('\n'.join(colored_lines))

#colored_chars = [random.choice(colors) + char for char in text]
#print(''.join(colored_chars))