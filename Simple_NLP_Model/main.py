
import spacy
def analyze(sentence):

    nlp = spacy.load("pl_core_news_sm")
    doc = nlp(sentence)
    IMPT_X=-1

    for sent in doc.sents:
        for index, token in enumerate(sent):
            if(token.tag_ == 'IMPT'):
                IMPT_X=index
        if IMPT_X != -1:
            IMP = sent[IMPT_X]
            OBJ = sent[IMPT_X+1:len(sent)]
            print(f"action: \"{IMP}\", object: \"{OBJ}\"")


analyze("posprzątaj zlew")