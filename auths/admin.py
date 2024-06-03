from django.contrib import admin
from .models import CustomUser
# Register your models here.

@admin.register(CustomUser)
class CustomUserAdmin(admin.ModelAdmin):

    list_display = [

        'username','email',
        'age','phone'
    ]

    list_display_links = ['username']

    list_max_show_all = 120
    list_per_page = 120

    list_display_links = ['username']
