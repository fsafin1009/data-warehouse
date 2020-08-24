from django.db import models
from django.urls import reverse

# Create your models here.


class Report(models.Model):

    title = models.CharField(max_length=150, verbose_name="Имя статьи")
    content = models.TextField(blank=True, verbose_name="Контент")
    updated_at = models.DateTimeField(auto_now=True, verbose_name="Дата обновления")
    category = models.ForeignKey('Category', on_delete=models.PROTECT, null=True)
    created_at = models.DateTimeField(auto_now_add=True, verbose_name="Дата создания")
    is_published = models.BooleanField(default=True, verbose_name="Опубликовано")

    def get_absolute_url(self):
        return reverse('view_reports', kwargs={'report_id': self.pk})

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = "Отчет"
        verbose_name_plural = "Отчеты"
        ordering = ['-created_at']


class Category(models.Model):
    title = models.CharField(max_length=150, db_index=True, verbose_name='Название категори')

    def get_absolute_url(self):
        return reverse('category', kwargs={"category_id": self.pk})

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = "Категория"
        verbose_name_plural = "Категории"
        ordering = ['title']

