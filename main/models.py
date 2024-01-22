from django.db import models

from root.utils.utils import slug_generate

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

    def save(self, *args, **kwargs) -> None:
        if not self.slug:
            self.slug = slug_generate()
        return super().save(*args, **kwargs)
