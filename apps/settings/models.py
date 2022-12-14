from django.db import models

# Create your models here.
class Setting(models.Model):
    title = models.CharField(max_length=100, verbose_name="Название сайта")
    description = models.TextField(verbose_name="Описание сайта")
    logo = models.ImageField(upload_to = 'logo/', verbose_name="Логотип сайта")
    phone = models.CharField(max_length=255, verbose_name="Телефонный номер")
    address = models.CharField(max_length=255, verbose_name="Адрес", blank = True, null = True)
    email = models.EmailField(max_length=150, verbose_name="Электронная почта сайта")
    facebook = models.URLField(blank = True, null=True, verbose_name="Ссылка на facebook")
    twitter = models.URLField(blank = True, null=True, verbose_name="Ссылка на twitter")
    youtube = models.URLField(blank = True, null=True, verbose_name="Ссылка на youtube")
    instagram = models.URLField(blank = True, null=True, verbose_name="Ссылка на instagram")

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = "Настройка"
        verbose_name_plural = "Настройки"

class ItRunLogo(models.Model):
    title = models.CharField(max_length=100)
    it_run_logo = models.ImageField(upload_to = 'logo/', verbose_name="Логотип")

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = "Логотип"
        verbose_name_plural = "Логотипы"


class Reguest(models.Model):
    name = models.CharField(max_length=255)
    email = models.EmailField(max_length=255)
    subject = models.TextField(max_length=100)
    phone = models.CharField(max_length=100)
    text = models.TextField()

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "Запрос"
        verbose_name_plural = "Запросы"
