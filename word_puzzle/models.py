from django.db import models

# Create your models here.

class Field(models.Model):
    from django.core.validators import MinValueValidator

    height = models.IntegerField(
        validators=[MinValueValidator(1)]
    )
    width = models.IntegerField(
        validators=[MinValueValidator(1)]
    )
    contents = models.TextField()

    def __str__(self):
        return f"{self.height} x {self.width} letter field"

    def save(self, *args, **kwargs):
        if not self.pk and Field.objects.exists():
            raise ValidationError("There can be only one Field instance")
        return super().save(*args, **kwargs)

class Word(models.Model):
    from django.core.validators import MinValueValidator

    field = models.ForeignKey(Field, on_delete=models.PROTECT)

    x_start = models.IntegerField(validators=[MinValueValidator(0)])
    y_start = models.IntegerField(validators=[MinValueValidator(0)])
    order = models.TextField()
    word = models.TextField()

    def __str__(self):
        return f"Word {self.word}, {self.order} from ({self.x_start}, {self.y_start})"

class UserProgress(models.Model):
    nickname = models.TextField()
    solved_words = models.ManyToManyField(Word, blank=True)

    def __str__(self):
        return f"{self.nickname}: {len(self.solved_words.all())} words"
