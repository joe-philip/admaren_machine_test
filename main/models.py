from django.db import models

# Create your models here.


class Tags(models.Model):
    title = models.CharField(max_length=50, unique=True)

    class Meta:
        db_table = 'tags'
        verbose_name = 'Tag'

    def __str__(self) -> str: return self.title
