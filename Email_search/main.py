import re

f = open("text.txt", "r")
fw = open("found.txt", "w")

lines = f.readlines()
found_mails = []
for line in lines:
    match = re.search(r'[\w.+-]+@[\w-]+\.[\w.-]+', line)
    found_mails.append(str(match))

fw.writelines(found_mails)