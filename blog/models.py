from django.db import models
from django.utils import timezone
from django.contrib import auth
from django.contrib.auth.models import User
from django.db.models import OneToOneField, ForeignKey, CASCADE


class Field(models.Model):
    """Описание полей различных категорий документов"""
    name = models.CharField(max_length=30)
    category = models.ForeignKey('Category', on_delete=models.CASCADE)
    types = models.CharField(max_length=30)

    class Meta():
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
    """загрузка документов администратором"""
    title = models.CharField(max_length=30)
    file = models.FileField()
    #field = ForeignKey('Field')
class UserDoc(models.Model):
    """документы пользователя"""
    user = ForeignKey('auth.User')
    userFile = models.FileField(upload_to='uploads/')

class orgdata(models.Model):#Переименовать класс!
    user = ForeignKey('auth.User')
    doc = models.ForeignKey('Filling', on_delete=models.CASCADE)

"""class Post(models.Model):

    author = models.ForeignKey('auth.User')

    #author = models.OneToOneField('auth.User')
    title = models.CharField(max_length=200)
    text = models.TextField()
    created_date = models.DateTimeField(
            default=timezone.now)
    published_date = models.DateTimeField(
            blank=True, null=True)

    def publish(self):
        self.published_date = timezone.now()
        self.save()

    def __str__(self):
        return self.title"""


class userdata(models.Model): #Переименовать класс!
    """Данные пользователя"""
    #u = User.objects.get(username__exact="username")
    user = models.ForeignKey('auth.User')
    #user = models.OneToOneField(User)
    #attr = models.ForeignKey('Attribut')
    first_name = models.CharField(max_length=30)
    last_name =  models.CharField(max_length=30)
    second_name = models.CharField(max_length=30)
    email = models.CharField(max_length=30)
    number = models.CharField(max_length=30, null=True)

class worker(models.Model): #Переименовать класс!
    """Данные сотрудника"""
    author_id = models.ForeignKey('auth.User')
    w_name = models.CharField(max_length=30)
    w_surname = models.CharField(max_length=30)
    w_lastname = models.CharField(max_length=30)
    position = models.CharField(max_length=30)

class DocumentType(models.Model):
    name = models.CharField(max_length=30)
    description = models.TextField(blank=True)

class Filling(models.Model): #Переименовать класс!
    """Данные организации"""
    author_id = models.ForeignKey('auth.User')
    #attr = models.ForeignKey('Attribut')
    inn = models.IntegerField()
    ogrn = models.IntegerField()
    name = models.CharField(max_length=30)
    city = models.CharField(max_length=30)
    address = models.CharField(max_length=30)

"""class Attribut(models.Model):
    name = models.CharField(max_length=30)
    type_choise = models.CharField(max_length=30)"""


#    created_date = models.DateTimeField(
#            default=timezone.now)
#    published_date = models.DateTimeField(
#               blank=True, null=True)

#    def publish(self):
#        self.published_date = timezone.now()
#        self.save()

#    def __str__(self):
#        return self.title
