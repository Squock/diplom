from django.contrib import admin
from .models import Organization, Userdata, Worker, Field, Value, Category, UploadFileForm

admin.site.register(Organization)
admin.site.register(Userdata)
admin.site.register(Worker)
admin.site.register(Field)
admin.site.register(Value)
admin.site.register(Category)
admin.site.register(UploadFileForm)