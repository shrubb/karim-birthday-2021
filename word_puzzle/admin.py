from django.contrib import admin

# Register your models here.
from .models import Word, Field, UserProgress

admin.site.register(Field)
admin.site.register(Word)
admin.site.register(UserProgress)