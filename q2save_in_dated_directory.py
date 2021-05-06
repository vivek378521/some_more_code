import os
import string
import random
from datetime import date


def getDate(format):
    today = date.today()
    return today.strftime(format)


def getRandomName():
    return ''.join(random.choices(string.ascii_uppercase + string.digits, k=10))


def writeToTextFile(file_input):
    filename = checkDirectory() + "/" + str(getRandomName()) + ".txt" # pointing file to the directory
    with open(filename, 'w') as file:
        file.write(file_input)
    return "Input Written to "+filename


def checkDirectory():
    try:
        os.makedirs(getDate("%d-%m-%Y"))
    except FileExistsError:
        pass
    return getDate("%d-%m-%Y")


if __name__ == "__main__":
    fileinput = input("Please enter file contents: ")
    print(writeToTextFile(fileinput))
