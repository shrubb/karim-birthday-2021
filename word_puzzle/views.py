from django.shortcuts import get_object_or_404, render

from django.http import HttpResponse
from django.template import loader

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
    