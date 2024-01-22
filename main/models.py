from django.db import models

# Create your models here.


class Tags(models.Model):
    title = models.CharField(max_length=50, unique=True)

    class Meta:
        db_table = 'tags'
        verbose_name = 'Tag'

    def __str__(self) -> str: return self.title


class TextSnippets(models.Model):
    slug = models.SlugField(unique=True)
    title = models.CharField(max_length=50)
    snippet = models.TextField()
    tags = models.ManyToManyField(Tags)
    created_at = models.DateTimeField(auto_now_add=True)
    created_user = models.ForeignKey('auth.User', on_delete=models.CASCADE)

    class Meta:
        db_table = 'text_snippets'
        verbose_name = 'Text snippet'

    def __str__(self) -> str: return self.title
