#download file used in code  http://zil.ipipan.waw.pl/PoliMorf
def load_dict(file_path):

    dict = set()
    with open("PoliMorf-0.6.7.tab", encoding="utf-8") as f:
        for line in f:
            parts = line.split("\t")
            word = parts[0].strip()
            dict.add(word)
    return dict

def max_match(sentence, dictionary):
    words = []

    while sentence:

        for i in range(len(sentence), 0, -1):
            part = sentence[:i]
            if part in dictionary:
                words.append(part)
                sentence = sentence[i:]
                break
        else:
            words.append(sentence[0])
            sentence = sentence[1:]

    return words


custom_dict = load_dict("custom_dict.txt")

sentence = "Alamakota"

segmented_sentence = max_match(sentence, custom_dict)

print("Oryginalne zdanie:", sentence)
print("Podzielone zdanie:", " ".join(segmented_sentence))