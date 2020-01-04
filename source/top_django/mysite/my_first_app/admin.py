from django.contrib import admin

# Register your models here.
from .models import Question, Boy

admin.site.register(Question)
admin.site.register(Boy)