import os
import threading
import time

MiB = 1024 * 1024


def typeAnim(text, speed, newline=True):
    for i in text:
        print(i, end="", flush=True)
        time.sleep(speed)
    if newline:
        print()


def writeFile(file, lol):
    for n in range(lol):
        file.write(os.urandom(MiB))


def progressBar(current, total, barlen=50):
    percent = float(current) * 100 / total
    arrow = '-' * int(percent / 100 * barlen - 1) + '>'
    spaces = ' ' * (barlen - len(arrow))
    print('Progress: [%s%s] %d %%' % (arrow, spaces, percent), end='\r')


def threadfunc(fName, choice):
    global file
    file = open(fName, "wb")
    for progress in range(int(choice)):
        writeFile(file, 1)
        progressBar(progress, int(choice))
    time.sleep(1)
    os.system('cls')
    file.close()


def main():
    os.system("title " + 'Big File Generator by EinsKatze²#9444')
    typeAnim("Please enter the file name.", 0.05)
    fName = input('Filename > ')
    typeAnim("Please enter the file size.", 0.05)
    choice = input('Mibibytes > ')
    if int(choice) <= 0:
        print("Invalid. Try again.")
        main()
    writeFileThread = threading.Thread(target=threadfunc, args=(fName, choice,))
    writeFileThread.start()
    typeAnim("Generating file ...", 0.025)
    print('\n')


if __name__ == '__main__':
    main()
