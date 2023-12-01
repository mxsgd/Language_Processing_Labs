
def isCons(letter):
    if letter == 'a' or letter == 'e' or letter == 'i' or letter == 'o' or letter == 'u':
        return False
    else:
        return True

def isConsonant(word, i):
    letter = word[i]
    if isCons(letter):
        if letter == 'y' and isCons(word[i - 1]):
            return False
        else:
            return True
    else:
        return False

def isVowel( word, i):
    return not(isConsonant(word, i))

def endsWith(stem, letter):
    if stem.endswith(letter):
        return True
    else:
        return False

def containsVowel(stem):
    for i in stem:
        if not isCons(i):
            return True
    return False

def doubleCons(stem):
    if len(stem) >= 2:
        if isConsonant(stem, -1) and isConsonant(stem, -2):
            return True
        else:
            return False
    else:
        return False

def getForm(word):
    form = []
    formStr = ''
    for i in range(len(word)):
        if isConsonant(word, i):
            if i != 0:
                prev = form[-1]
                if prev != 'C':
                    form.append('C')
            else:
                form.append('C')
        else:
            if i != 0:
                prev = form[-1]
                if prev != 'V':
                    form.append('V')
            else:
                form.append('V')
    for j in form:
        formStr += j
    return formStr

def getM(word):
    form = getForm(word)
    m = form.count('VC')
    return m

def cvc(word):
    if len(word) >= 3:
        f = -3
        s = -2
        t = -1
        third = word[t]
        if isConsonant(word, f) and isVowel(word, s) and isConsonant(word, t):
            if third != 'w' and third != 'x' and third != 'y':
                return True
            else:
                return False
        else:
            return False
    else:
        return False

def replace(orig, rem, rep):
    result = orig.rfind(rem)
    base = orig[:result]
    replaced = base + rep
    return replaced

def replaceM0(orig, rem, rep):
    result = orig.rfind(rem)
    base = orig[:result]
    if getM(base) > 0:
        replaced = base + rep
        return replaced
    else:
        return orig

def replaceM1(orig, rem, rep):
    result = orig.rfind(rem)
    base = orig[:result]
    if getM(base) > 1:
        replaced = base + rep
        return replaced
    else:
        return orig

def step1a( word):
    if word.endswith('sses'):
        word = replace(word, 'sses', 'ss')
    elif word.endswith('ies'):
        word = replace(word, 'ies', 'i')
    elif word.endswith('ss'):
        word = replace(word, 'ss', 'ss')
    elif word.endswith('s'):
        word = replace(word, 's', '')
    else:
        pass
    return word

def step1b(word):
    flag = False
    if word.endswith('eed'):
        result = word.rfind('eed')
        base = word[:result]
        if getM(base) > 0:
            word = base
            word += 'ee'
    elif word.endswith('ed'):
        result = word.rfind('ed')
        base = word[:result]
        if containsVowel(base):
            word = base
            flag = True
    elif word.endswith('ing'):
        result = word.rfind('ing')
        base = word[:result]
        if containsVowel(base):
            word = base
            flag = True
    if flag:
        if word.endswith('at') or word.endswith('bl') or word.endswith('iz'):
            word += 'e'
        elif doubleCons(word) and not endsWith(word, 'l') and not endsWith(word, 's') and not endsWith(word, 'z'):
            word = word[:-1]
        elif getM(word) == 1 and cvc(word):
            word += 'e'
        else:
            pass
    else:
        pass
    return word

def step1c(word):
    if word.endswith('y'):
        result = word.rfind('y')
        base = word[:result]
        if containsVowel(base):
            word = base
            word += 'i'
    return word

def step2( word):
    if word.endswith('ational'):
        word = replaceM0(word, 'ational', 'ate')
    elif word.endswith('tional'):
        word = replaceM0(word, 'tional', 'tion')
    elif word.endswith('enci'):
        word = replaceM0(word, 'enci', 'ence')
    elif word.endswith('anci'):
        word = replaceM0(word, 'anci', 'ance')
    elif word.endswith('izer'):
        word = replaceM0(word, 'izer', 'ize')
    elif word.endswith('abli'):
        word = replaceM0(word, 'abli', 'able')
    elif word.endswith('alli'):
        word = replaceM0(word, 'alli', 'al')
    elif word.endswith('entli'):
        word = replaceM0(word, 'entli', 'ent')
    elif word.endswith('eli'):
        word = replaceM0(word, 'eli', 'e')
    elif word.endswith('ousli'):
        word = replaceM0(word, 'ousli', 'ous')
    elif word.endswith('ization'):
        word = replaceM0(word, 'ization', 'ize')
    elif word.endswith('ation'):
        word = replaceM0(word, 'ation', 'ate')
    elif word.endswith('ator'):
        word = replaceM0(word, 'ator', 'ate')
    elif word.endswith('alism'):
        word = replaceM0(word, 'alism', 'al')
    elif word.endswith('iveness'):
        word = replaceM0(word, 'iveness', 'ive')
    elif word.endswith('fulness'):
        word = replaceM0(word, 'fulness', 'ful')
    elif word.endswith('ousness'):
        word = replaceM0(word, 'ousness', 'ous')
    elif word.endswith('aliti'):
        word = replaceM0(word, 'aliti', 'al')
    elif word.endswith('iviti'):
        word = replaceM0(word, 'iviti', 'ive')
    elif word.endswith('biliti'):
        word = replaceM0(word, 'biliti', 'ble')
    return word

def step3( word):
    if word.endswith('icate'):
        word = replaceM0(word, 'icate', 'ic')
    elif word.endswith('ative'):
        word = replaceM0(word, 'ative', '')
    elif word.endswith('alize'):
        word = replaceM0(word, 'alize', 'al')
    elif word.endswith('iciti'):
        word = replaceM0(word, 'iciti', 'ic')
    elif word.endswith('ful'):
        word = replaceM0(word, 'ful', '')
    elif word.endswith('ness'):
        word = replaceM0(word, 'ness', '')
    return word

def step4( word):
    if word.endswith('al'):
        word = replaceM1(word, 'al', '')
    elif word.endswith('ance'):
        word = replaceM1(word, 'ance', '')
    elif word.endswith('ence'):
        word = replaceM1(word, 'ence', '')
    elif word.endswith('er'):
        word = replaceM1(word, 'er', '')
    elif word.endswith('ic'):
        word = replaceM1(word, 'ic', '')
    elif word.endswith('able'):
        word = replaceM1(word, 'able', '')
    elif word.endswith('ible'):
        word = replaceM1(word, 'ible', '')
    elif word.endswith('ant'):
        word = replaceM1(word, 'ant', '')
    elif word.endswith('ement'):
        word = replaceM1(word, 'ement', '')
    elif word.endswith('ment'):
        word = replaceM1(word, 'ment', '')
    elif word.endswith('ent'):
        word = replaceM1(word, 'ent', '')
    elif word.endswith('ou'):
        word = replaceM1(word, 'ou', '')
    elif word.endswith('ism'):
        word = replaceM1(word, 'ism', '')
    elif word.endswith('ate'):
        word = replaceM1(word, 'ate', '')
    elif word.endswith('iti'):
        word = replaceM1(word, 'iti', '')
    elif word.endswith('ous'):
        word = replaceM1(word, 'ous', '')
    elif word.endswith('ive'):
        word = replaceM1(word, 'ive', '')
    elif word.endswith('ize'):
        word = replaceM1(word, 'ize', '')
    elif word.endswith('ion'):
        result = word.rfind('ion')
        base = word[:result]
        if getM(base) > 1 and (endsWith(base, 's') or endsWith(base, 't')):
            word = base
        word = replaceM1(word, '', '')
    return word

def step5a(word):
    if word.endswith('e'):
        base = word[:-1]
        if getM(base) > 1:
            word = base
        elif getM(base) == 1 and not cvc(base):
            word = base
    return word

def step5b(word):
    if getM(word) > 1 and doubleCons(word) and endsWith(word, 'l'):
        word = word[:-1]
    return word

def stem( word):
    word = step1a(word)
    word = step1b(word)
    word = step1c(word)
    word = step2(word)
    word = step3(word)
    word = step4(word)
    word = step5a(word)
    word = step5b(word)
    return word

word = "running"
print(stem(word))