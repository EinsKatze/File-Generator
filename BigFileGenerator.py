import os

MiB = 1024 * 1024


def writeFile(file, size):
    file = open(fName, "wb")
    for n in range(int(size)):
        file.write(os.urandom(MiB))
        progressBar(n, int(size))
    file.close()


def progressBar(current, total, barlen=50):
    percent = float(current) * 100 / total
    arrow = '-' * int(percent / 100 * barlen - 1) + '>'
    spaces = ' ' * (barlen - len(arrow))
    print('Progress: [%s%s] %d %%' % (arrow, spaces, percent), end='\r')


def main():
    print("Please enter the file name.", 0.05)
    fName = input('Filename > ')
    print("Please enter the file size.", 0.05)
    choice = input('Mibibytes > ')
    if int(choice) <= 0:
        print("Invalid. Try again.")
        main()
    print("Generating file ...\n\n")
    writeFile(fName, choice)
    print("\n\n")


if __name__ == '__main__':
    main()
