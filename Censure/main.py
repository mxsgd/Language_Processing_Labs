import re

with open('text.txt', 'r', ) as file:
    f = file.readlines()
fc = open("censured.txt", "w")

curses = ['kurwa', 'kurwy', 'kurwe', 'kurwo', 'kurwą', 'kurew', 'chuja', 'chuje', 'chuju', 'chuj', 'jebany', 'pierdol']
newlines = []

for line in f:

    for curse in curses:
        line = re.sub(curse, '---', line)
        line = re.sub("\[\'", '', line)
        line = re.sub("\'\]", '', line)

    newlines.append(line)

fc.writelines(newlines)