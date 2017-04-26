from django.contrib import admin
from .models import DocumentType, Filling, userdata, worker, Field, Value, Category, UploadFileForm, UserDoc#, Post

#admin.site.register(Post)
admin.site.register(DocumentType)
admin.site.register(Filling)
admin.site.register(userdata)
admin.site.register(worker)
admin.site.register(Field)
admin.site.register(Value)
admin.site.register(Category)
admin.site.register(UploadFileForm)
admin.site.register(UserDoc)

# Register your models here.
