import re

with open('text.txt', 'r', ) as file:
    f = file.readlines()
fc = open("censured.txt", "w")

curses = ['kurwa', 'kurwy', 'kurwe', 'kurwo', 'kurwą', 'kurew', 'chuja', 'chuje', 'chuju', 'chuj', 'jebany', 'pierdol']
r = str(f)
print(r)
for curse in curses:
    r = re.sub(curse, '---', r)
    r = re.sub("\[\'", '', r)
    r = re.sub("\'\]", '', r)

fc.writelines(r)