"""
Here is a very simple example. Adapt it to your needs.
The field in this example is:

QDJL
ZXAN
TNNG
TACO

There's one target word, "DJANGO", and one "extra" word, "TACO".
"""

height = 4
width = 4
# all rows concatenated
letters = "QDJLZXANTNNGTACO"

field_chars = [letters[i:i+width] for i in range(0, len(letters), width)]

def check_word(start_x, start_y, word, order, field_chars):
    order += 'x'
    for letter, step in zip(word, order):
        assert field_chars[start_x][start_y].lower() == letter, word

        if step == 'r':
            start_y += 1
        else:
            start_x += 1

from word_puzzle.models import Field, Word
field = Field.objects.first()

words = [
    (0, 1, 'django', 'rddrd', True),
    (3, 0, 'taco', 'rrr', False),
]

for x, y, word, order, is_target_word in words:
    assert len(word) == len(order) + 1, word
    check_word(x, y, word, order, field_chars)

for x, y, word, order, is_target_word in words:
    Word(field=field, x_start=x, y_start=y, word=word, order=order, is_target_word=is_target_word).save()
