from django.db import models

from config import settings

NULLABLE = {
    'null': True,
    'blank': True
}


class Announcement(models.Model):
    title = models.CharField(max_length=128,)
    price = models.IntegerField()
    description = models.TextField()
    author = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE,)
    created_at = models.DateTimeField(auto_now_add=True,)

    class Meta:
        verbose_name = "Объявление"
        verbose_name_plural = "Объявления"
        ordering = ("-created_at",)

    def __str__(self):
        return f"{self.author} | {self.title}"


class Comment(models.Model):
    text = models.CharField(max_length=255,)
    author = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE,)
    ad = models.ForeignKey(to=Announcement, on_delete=models.CASCADE,)
    created_at = models.DateTimeField(auto_now_add=True,)

    class Meta:
        verbose_name = "Комментарий"
        verbose_name_plural = "Комментарии"

    def __str__(self):
        return f"{self.author.name} | {self.ad.name} | {self.text}"
