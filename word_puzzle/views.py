from django.views.decorators.csrf import csrf_exempt

from django.shortcuts import get_object_or_404, render

from django.http import HttpResponse, JsonResponse
from django.template import loader

import json

def login(request):
    template = loader.get_template("word_puzzle/login.html")
    context = {}
    return HttpResponse(template.render(context, request))

def main(request, nickname):
    from word_puzzle.models import Field

    template = loader.get_template("word_puzzle/main.html")

    field = get_object_or_404(Field, pk=1)
    field_values = [field.contents[i:i+field.width] for i in range(0, len(field.contents), field.width)]

    context = {
        'nickname': nickname,
        'field': field_values,
        'field_height': field.height,
        'field_width': field.width,
    }
    return HttpResponse(template.render(context, request))

def state_query(request, nickname):
    from word_puzzle.models import UserProgress

    user_progress = UserProgress.objects.get_or_create(nickname=nickname)
    solved_words = [{
        'order': w.order,
        'word': w.word,
        'start': {'x': w.x_start, 'y': w.y_start},
        }
        for w in user_progress[0].solved_words.all()
    ]

    return JsonResponse({'solved_words': solved_words})

@csrf_exempt
def submit_word(request, nickname):
    from word_puzzle.models import Word, UserProgress

    query_word = json.loads(request.body)

    # Check if the word is in the field
    def word_js_to_order(word_json):
        retval = ''
        word_json = word_json['word']
        for position_1, position_2 in zip(word_json[:-1], word_json[1:]):
            retval += 'r' if position_1['y'] != position_2['y'] else 'd'
        return retval

    same_word_from_db = Word.objects.filter(
        x_start=query_word['word'][0]['x'],
        y_start=query_word['word'][0]['y'],
        order=word_js_to_order(query_word)).first()

    word_is_correct = same_word_from_db is not None

    if word_is_correct:
        # Also check if the user hasn't solved this word yet
        user_progress = UserProgress.objects.get_or_create(nickname=nickname)[0]
        if user_progress.solved_words.filter(id=same_word_from_db.id).exists():
            word_is_new_for_user = False
        else:
            word_is_new_for_user = True
            user_progress.solved_words.add(same_word_from_db)
    else:
        word_is_new_for_user = False

    return HttpResponse(status=201 if word_is_correct and word_is_new_for_user else 200)
