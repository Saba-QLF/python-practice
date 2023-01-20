import os

class ArrayStack:

    def __init__(self):
        self._items = []

    def push(self, x):
        self._items.append(x)

    def pop(self):
        return self._items.pop()

    def __len__(self):
        return len(self._items)

    def __repr__(self):
        sent = ' '.join(self._items)
        return (f'Sentence is: {sent}')


# one of applications that we can be made by stacks is 'Undo'

options = {
    0: ['I went to ', ['a restaurant', 'a shop', 'the forest', 'the beach', 'my university', 'harry styles concert',
                       'a library']],
    1: ['with ', ['a plane', 'a broom', 'my dad', 'smelly cloths', 'my college', 'a wiki on my neck', 'motorcycle']],
    2: ['for ', ['buying cookies', 'swimming', 'dancing to death', 'practicing German', 'use the bathroom',
                 'eating noodles']],
    3: ['.Then saw ', ['the president', 'bts Jungkook', 'Neymar', 'the handsome teacher', "mafia's chief", 'my ex',
                      'my next bf']],
    4: ['there. Then we ', ['kissed', 'danced', 'shook hands', 'shook our hips', 'played chess', 'fucked',
                            'ate icecreams']],
    5: ['.Cus I ', ['was happy!', 'was mad!', 'lost control!', 'wanted to!', 'he looks ugly!', 'was horny!',
                    'was bored!']]
}
print("Welcome To 'Funny Sentence Maker' App :)")
print("Lets start :)")
sentence = ArrayStack()

while len(sentence) < 6:
    print(sentence)
    word_id = len(sentence)
    n = input(f"choose an number between {len(options[word_id][1])}. Enter 'u' to Undo: \n")
    if n == 'u':
        if word_id == 0:
            pass
        else:
            sentence.pop()
    elif int(n) in range(1, len(options[word_id][1])+1):
        words = options[word_id][0] + options[word_id][1][int(n)-1]
        sentence.push(words)
    _ = os.system('cls')

print(sentence)