from django.contrib import admin
from .models import Todo
# Register your models here.


@admin.register(Todo)
class TodoAdmin(admin.ModelAdmin):

    list_display = [

        'title','user',
        'published_at','updated_at'
    ]

    list_display_links = ['title']
    list_filter = [

        'published_at','updated_at'
    ]

    date_hierarchy = 'published_at'
    list_max_show_all = 120
    list_per_page = 120
    search_fields = ['user']
    list_select_related = ['user']

    def user_name(self,obj):

        return obj.user.username