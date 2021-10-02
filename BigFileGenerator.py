import time
import os
import webbrowser
import threading
from colorama import Fore, Style

GB= 1024*1024*1024

def typeAnim(text, speed, newLine = True):
        for i in text:
            print(i, end = "", flush = True)
            time.sleep(speed)
        if newLine:
            print()

def writeFile(file, lol):
    for x in range(lol):
        file.write(os.urandom(GB))

def progressBar(current, total, barLength = 50):
        percent = float(current) * 100 / total
        arrow   = '-' * int(percent/100 * barLength - 1) + '>'
        spaces  = ' ' * (barLength - len(arrow))
        print(Fore.LIGHTGREEN_EX + 'Progress: [%s%s] %d %%' % (arrow, spaces, percent), end='\r')

def threadfunc(choice):
    global file
    global progress
    progress = 0
    file = open("BigFile.txt", "wb")
    for i in range(int(choice)):
        writeFile(file, 1)
        progress += 1
        progressBar(progress, int(choice))
    time.sleep(1)
    os.system('cls')
    file.close()
        

os.system("title " + 'Big TXT File Generator by EinsKatze#0546')
typeAnim(Fore.CYAN + "Wanna generate a Big File? How big should the file be? (in GB)", 0.05)
choice = input('Gigabytes > ' + Style.RESET_ALL)
if int(choice) == 0:
    for i in range(3):
        print(Fore.RED + "YOU CANT GENERATE A FILE THATS 0 GIGABYTES BIG\n" + Style.RESET_ALL)
        webbrowser.open('https://youtu.be/g8vUPIx5gD8?t=1', new=2, autoraise=True)
        time.sleep(0.5)
    exit(0)
x = threading.Thread(target=threadfunc, args=(choice,))
x.start()
typeAnim(Fore.YELLOW + "Generating file . . .", 0.025)
print('\n')
