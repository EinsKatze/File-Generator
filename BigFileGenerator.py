import os
import threading
import time

from colorama import Fore, Style

MB = 1024 * 1024


def typeAnim(text, speed, newline=True):
    for i in text:
        print(i, end="", flush=True)
        time.sleep(speed)
    if newline:
        print()


def writeFile(file, lol):
    for n in range(lol):
        file.write(os.urandom(MB))


def progressBar(current, total, barlen=50):
    percent = float(current) * 100 / total
    arrow = '-' * int(percent / 100 * barlen - 1) + '>'
    spaces = ' ' * (barlen - len(arrow))
    print(Fore.LIGHTGREEN_EX + 'Progress: [%s%s] %d %%' % (arrow, spaces, percent), end='\r')


def threadfunc(choice):
    global file
    global progress
    progress = 0
    file = open("BigFile.txt", "wb")
    for _ in range(int(choice)):
        writeFile(file, 1)
        progress += 1
        progressBar(progress, int(choice))
    time.sleep(1)
    os.system('cls')
    file.close()


def main():
    os.system("title " + 'Big File Generator by EinsKatze#0546')
    typeAnim(Fore.CYAN + "Enter the file Size! ", 0.05)
    choice = input('Megabytes > ' + Style.RESET_ALL)
    if int(choice) == 0:
        print("Invalid. Try again.")
        main()
    x = threading.Thread(target=threadfunc, args=(choice,))
    x.start()
    typeAnim(Fore.YELLOW + "Generating file . . .", 0.025)
    print('\n')


if __name__ == '__main__':
    main()
