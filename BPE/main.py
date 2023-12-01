from collections import Counter, defaultdict

def get_vocab(text):
    vocab = Counter(text.split())
    return {word: freq for word, freq in vocab.items()}

def get_stats(vocab):
    pairs = defaultdict(int)
    for word, freq in vocab.items():
        symbols = word.split()
        for i in range(len(symbols) - 1):
            pairs[symbols[i], symbols[i+1]] += freq
    return pairs

def merge_vocab(pair, vocab):
    new_vocab = {}
    bigram = ' '.join(pair)
    replacement = ''.join(pair)
    for word in vocab:
        new_word = word.replace(bigram, replacement)
        new_vocab[new_word] = vocab[word]
    return new_vocab

text = "Hurry on Harry"

vocab = get_vocab(text)
vocab = {' '.join(word): freq for word, freq in vocab.items()}
print("Initial vocabulary:", vocab)

num_merges = 2

for i in range(num_merges):
    pairs = get_stats(vocab)
    if not pairs:
        break
    best_pair = max(pairs, key=pairs.get)
    vocab = merge_vocab(best_pair, vocab)
    print(vocab)