from django.db import models
from django.contrib.auth.models import User
from django.db.models import ForeignKey, OneToOneField


class Field(models.Model):
    """Описание полей различных категорий документов"""
    name = models.CharField(max_length=30)
    category = models.ForeignKey('Category', on_delete=models.CASCADE)
    types = models.CharField(max_length=30)

    class Meta:
        verbose_name = "Описание поля"
        verbose_name_plural = " Описания полей"


class Value(models.Model):
    """Значение полей документов"""
    field = models.ForeignKey('Field', on_delete=models.CASCADE)
    value = models.TextField()
    user = models.ForeignKey('auth.User')


class Category(models.Model):
    """категория документов"""
    name = models.CharField(max_length=30)


class UploadFileForm(models.Model):
    """
    загруженные администратором шаблоны документов в формате docx 
    предназначены для заполнения из данных пользователя
    """
    title = models.CharField(max_length=30)
    file = models.FileField()


class Userdata(models.Model):
    """Данные пользователя"""
    user = models.OneToOneField('auth.User')
    name = models.CharField(max_length=30, verbose_name="Имя")
    surname = models.CharField(max_length=30, verbose_name="Фамилия")
    second_name = models.CharField(max_length=30, verbose_name="Отчество")
    email = models.CharField(max_length=30, verbose_name="Элекронная почта")
    number = models.CharField(max_length=30, null=True, verbose_name="Номер телефона")


class Worker(models.Model):
    """Данные сотрудника"""
    organization = ForeignKey('Organization', related_name='workers')
    name = models.CharField(max_length=30, verbose_name="Имя")
    surname = models.CharField(max_length=30, verbose_name="Фамилия")
    second_name = models.CharField(max_length=30, verbose_name="Отчество")
    position = models.CharField(max_length=30, verbose_name="Должность")


class Organization(models.Model):
    """Данные организации"""
    author = models.ForeignKey('auth.User')
    inn = models.CharField("ИНН", max_length=12)
    ogrn = models.CharField("ОГРН", max_length=13)
    name = models.CharField("Наименование организации", max_length=100)
    city = models.CharField("Населенный пункт", max_length=30)
    fact_address = models.CharField("Фактический адрес", max_length=100, blank=True)
    reg_address = models.CharField("Юридический адрес", max_length=100, blank=True)
    post_address = models.CharField("Почтовый адрес", max_length=100, blank=True)
    chief = ForeignKey('Worker', blank=True, null=True, related_name='chief', verbose_name="Руководитель")
    # chief_name = models.CharField(max_length=30, default='some string', verbose_name="Имя")
    # chief_surname = models.CharField(max_length=30, default='some string', verbose_name="Фамилия")
    # chief_secondname = models.CharField(max_length=30, default='some string', verbose_name="Отчество")
    # chief_fullposition = models.CharField(max_length=30, default='some string', verbose_name="Должность")
