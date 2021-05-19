import time
import os
import webbrowser
from colorama import Fore, Style

file = open("BigFile.txt", "wb")
GB= 1024*1024*1024
progress = 0

def typeAnim(text, speed, newLine = True):
        for i in text:
            print(i, end = "", flush = True)
            time.sleep(speed)
        if newLine:
            print()

def writeFile(lol):
    for x in range(lol):
        file.write(os.urandom(GB))

def progressBar(current, total, barLength = 50):
        percent = float(current) * 100 / total
        arrow   = '-' * int(percent/100 * barLength - 1) + '>'
        spaces  = ' ' * (barLength - len(arrow))
        print(Fore.LIGHTGREEN_EX + 'Progress: [%s%s] %d %%' % (arrow, spaces, percent), end='\r')

os.system("title " + 'Big TXT File Generator by EinsKatze#0546')
typeAnim(Fore.CYAN + "Wanna Write a Big File? How many Gigabytes should the File have?", 0.05)
choice = input('Gigabytes > ' + Style.RESET_ALL)
if int(choice) == 0:
    for i in range(3):
        print(Fore.RED + "YOU CANT GENERATE A FILE THATS 0 GIGABYTES BIG\n" + Style.RESET_ALL)
        webbrowser.open('https://youtu.be/g8vUPIx5gD8?t=1', new=2, autoraise=True)
        time.sleep(0.5)
    exit(0)
typeAnim(Fore.YELLOW + "Okay, your file will be written now.", 0.05)
typeAnim("Please wait for the file to be written. It will take some time due to the big file size.", 0.05)
print('\n')
for i in range(int(choice)):
    writeFile(1)
    progress += 1
    progressBar(progress, int(choice))

time.sleep(3)
os.system('cls')
file.close()