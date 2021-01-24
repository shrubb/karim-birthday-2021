# "easy" board (obsolete)

"""
from word_puzzle.models import Field, Word

# 12 x 13
# АБВГДЕЁЖРИЙККСЕБУЫТЗЫАЩМЫЫКЕГЧУРИЪЗЪНЫКАОРИХЕОЗАЁГЫУЙФОМЫУГИФБЩКТЙЦУКЕНОЛЬНИСАБЦСИЛЩЧЕКДКПГОЬЕХАЦЦЗЮУПЦРМОЛОЛЕЕЦЫВАЕЯБОВАЯЁПБРАУГЗПСОСКМЛЯЙТЕШЬФЫВААРОЛДИШКА

field = Field.objects.first()

for x, y, word, order in [
    (1, 0, 'себучим', 'rrrddd'),
    (1, 0, 'скайфом', 'dddrrr'),
    (1, 5, 'треугольник', 'dddrdrrrrd'),
    (0, 8, 'разъёбщик', 'ddrddrdd'),
    (3, 7, 'заёбщик', 'rrdrdd'),
    (0, 12, 'кык', 'dd'),
    (6, 0, 'бомбовая', 'dddrrrr'),
    (10, 1, 'соска', 'rrrd'),
    (7, 6, 'цепляйте', 'dddrrrr'),
    (9, 7, 'братишка', 'rrddrrr'),
    (6, 12, 'грязь', 'dddd'),
    (6, 2, 'сила', 'rrd'),
]:
    Word(field=field, x_start=x, y_start=y, word=word, order=order).save()
"""

# "hard" board

height = 14
width = 15
letters = "КУВГКПОИНТНККЫЫСЕБУЛЁЁПТКЕРНЫККЕГЧУТЗРУЛЙЫАККАОРИБРЕАЗАРМШЫКЙФОММПУВЪЁОССЫЫНГУПОЕГОЛБЩЕЪКСЕККЕЗРВСЬНИЪЪЧАТЧУРДЦЕЛУУКСАРВБПСИРОПЧЁТЫЙДПСОБЬЛАВЛЯШБРЕЫЦЯМБОРЦУХЙКИАТГРЯЖИВАЯУЁТЕПАИШКЗИНЬВЫСОЦМИЦСААЬРАФЕНОСКАРАНЛАМ"

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
    (1, 0, 'себучим', 'rrrddd', True),
    (1, 0, 'скайфом', 'dddrrr', True),
    (2, 5, 'треугольник', 'drddrrdrrd', True),
    (2, 7, 'разъёбщик', 'drdrdrdd', True),
    (3, 8, 'заёбщик', 'rddrdd', True),
    (2, 13, 'кык', 'dr', True),
    (8, 0, 'бомбовая', 'ddrrdrr', True),
    (12, 5, 'соска', 'rdrr', True),
    (7, 5, 'цепляйте', 'rddrddr', True),
    (9, 9, 'братишка', 'rdrdrrd', True),
    (10, 12, 'грязь', 'rrdd', True),
    (8, 2, 'сила', 'rdr', True),
    (11, 7, 'тема', 'rdd', True),
    (0, 5, 'пётр', 'ddd', False),
    (1, 7, 'правосл', 'dddddd', False),
    (0, 5, 'поинткла', 'rrrrddd', False),
    (0, 10, 'нейросе', 'ddddrd', False),
    (0, 11, 'крым', 'ddd', False),
    (1, 12, 'наш', 'dd', False),
    (5, 13, 'кчр', 'dd', False),
    (4, 9, 'ёбнутый', 'ddddrr', False),
    (5, 14, 'савс', 'ddd', False),
    (8, 13, 'пцр', 'dd', False),
    (7, 13, 'рпц', 'dd', False),
    (10, 14, 'язь', 'dd', False),
    (12, 11, 'салам', 'rdrr', False),
    (11, 9, 'пацан', 'rddr', False),
    (13, 5, 'оскар', 'rrrr', False),
    (5, 3, 'поздравляшки', 'rddddrrrrdr', False),
    (9, 6, 'ляшки', 'rrdr', False),
    (10, 1, 'борцух', 'rrrrr', False),
    (11, 0, 'живая', 'rrrr', False),
    (11, 0, 'жираф', 'ddrr', False),
    (5, 1, 'гкчп', 'ddd', False),
    (1, 0, 'скайнет', 'dddddd', False),
    (8, 0, 'бомж', 'ddd', False),
    (6, 2, 'керил', 'rddd', False),
    (6, 2, 'кусь', 'ddd', False),
    (4, 1, 'фомм', 'rrr', False),
    (0, 4, 'клуб', 'ddd', False),
    (0, 3, 'гучи', 'ddd', False),
    (8, 2, 'сироп', 'rrrr', False),
    (8, 12, 'дпс', 'rr', False),
    (1, 6, 'ёпт', 'rr', False),
    (11, 9, 'пир', 'dd', False),
    (8, 7, 'чёты', 'rrr', False),
    (7, 12, 'адыг', 'ddd', False),
]

for x, y, word, order, is_target_word in words:
    assert len(word) == len(order) + 1, word
    check_word(x, y, word, order, field_chars)

for x, y, word, order, is_target_word in words:
    Word(field=field, x_start=x, y_start=y, word=word, order=order, is_target_word=is_target_word).save()

