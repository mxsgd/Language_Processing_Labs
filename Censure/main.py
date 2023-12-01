
def Censure():
    linecount = 0
    f = open("letter.txt", "r")
    fc = open("letterC.txt", "w")
    lines = f.readlines()
    newlines = []
    for line in lines:
        linecount += 1
        if "kocham" not in line.split() and "Kocham" not in line.split():
            if linecount % 3 == 0:
                newlines.append('*' * len(line)+'\n')
            else:
                newlines.append(line)
        else:
            newlines.append('*' * len(line)+'\n')

    fc.writelines(newlines)

Censure()