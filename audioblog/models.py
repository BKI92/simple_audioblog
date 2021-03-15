from django.db import models


class Song(models.Model):
    title = models.CharField(max_length=50, unique=True)
    artist = models.CharField(max_length=50, blank=True, null=True)
    audio_file = models.FileField()
    tags = models.ManyToManyField(
        'Tag', related_name='song_tags', verbose_name='Тэги', blank=True,
    )
    year = models.DateField(blank=True, null=True)

    class Meta:
        verbose_name = 'Аудиозапись'
        verbose_name_plural = 'Аудиозаписи'

    def __str__(self):
        return self.title


class Tag(models.Model):
    RED = 'red'
    BLUE = 'blue'
    BLACK = 'black'
    ORANGE = 'orange'
    GREEN = 'green'
    YELLOW = 'yellow'
    CYAN = 'cyan'
    PURPLE = 'purple'
    VIOLET = 'violet'
    COLORS = (
        (RED, 'red'),
        (BLUE, 'blue'),
        (BLACK, 'black'),
        (ORANGE, 'orange'),
        (GREEN, 'green'),
        (YELLOW, 'yellow'),
        (CYAN, 'cyan'),
        (PURPLE, 'purple'),
        (VIOLET, 'violet'),
    )
    title = models.CharField('Название', unique=True, max_length=15)
    style = models.CharField('Стиль', max_length=30, null=False,
                             default='green', choices=COLORS)

    class Meta:
        verbose_name = 'Тэг'
        verbose_name_plural = 'Тэги'

    def __str__(self):
        return self.title
