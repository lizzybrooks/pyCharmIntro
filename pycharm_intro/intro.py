from random import shuffle

def shuffle_word(word):
    word = list(word)
    shuffle(word)
    return ''.join(word)

new = shuffle_word("lizzy brooks")
print(new)