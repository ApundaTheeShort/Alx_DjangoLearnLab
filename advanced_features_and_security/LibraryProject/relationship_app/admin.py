from django.contrib import admin

# Register your models here.
from . import models

admin.site.register(models.Author)
admin.site.register(models.Book)
admin.site.register(models.Librarian)
admin.site.register(models.Library)


class CustomUserModel(admin.ModelAdmin):
    list_display = ('email', 'username', 'is_active',
                    'is_staff', 'date_joined')
    search_fields = ('email', 'username')
    list_filter = ('is_active', 'is_staff', 'date_joined')


admin.site.register(models.CustomUser, CustomUserModel)
