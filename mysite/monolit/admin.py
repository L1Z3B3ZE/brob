from django.contrib import admin
from .models import *

# Register your models here.

admin.site.register(User)


@admin.register(Product)
class PostAdminView(admin.ModelAdmin):
    display = ('title', 'date_create')