from django.contrib import admin

# Register your models here.
from django.contrib.auth.models import User
from .models import *
# from parler.admin import TranslatableAdmin
admin.site.register(Book)

admin.site.register(Category)
admin.site.register(chat_model)

admin.site.register(ChatMessage)
@admin.register(Profile)
class ProfileAdmin(admin.ModelAdmin):
    list_display = ['user', 'date_of_birth']


