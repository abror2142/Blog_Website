from django.db import models


# Create your models here.
class Category(models.Model):
    title = models.CharField(max_length=50, verbose_name='Kategoriya')
    created_at = models.DateTimeField(auto_now_add=True, verbose_name="Yuklangan vaqti")

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Kategoriya'
        verbose_name_plural = 'Kategoriyalar'
        ordering = ('title', )


class Post(models.Model):
    title = models.CharField(max_length=255, verbose_name='Sarlavha')
    content = models.TextField(verbose_name='Maqola matni')
    created = models.DateTimeField(auto_now_add=True, verbose_name='Yuklangan vaqti')
    updated = models.DateTimeField(auto_now=True, verbose_name='Yangilangan vaqti')
    published = models.BooleanField(default=True, verbose_name='Saytga chiqarilgan vaqti')
    category = models.ForeignKey(Category, on_delete=models.CASCADE)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Maqola'
        verbose_name_plural = 'Maqolalar'
        ordering = ('created',)